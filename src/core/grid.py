"""
ARC-AGI Core Data Structures and Utilities.
Provides representations for Grids, Objects, Tasks, and Serialization.
"""

from dataclasses import dataclass
from typing import List, Tuple, Dict, Any, Optional, Set
import numpy as np
import json


# 10 Warna Standar ARC (0-9)
COLOR_NAMES = {
    0: "black",
    1: "blue",
    2: "red",
    3: "green",
    4: "yellow",
    5: "grey",
    6: "magenta",
    7: "orange",
    8: "azure",
    9: "maroon"
}

# Hex codes untuk visualisasi
COLOR_HEX = {
    0: "#000000",
    1: "#0074D9",
    2: "#FF4136",
    3: "#2ECC40",
    4: "#FFDC00",
    5: "#AAAAAA",
    6: "#F012BE",
    7: "#FF851B",
    8: "#7FDBFF",
    9: "#870C25"
}


@dataclass(frozen=True)
class Object:
    """
    Representasi objek diskret pada grid.
    Menyimpan koordinat, warna, bounding box, dan bentuk.
    """
    color: int
    pixels: Tuple[Tuple[int, int], ...]  # Tuple of (row, col) coordinates
    
    @property
    def size(self) -> int:
        return len(self.pixels)
    
    @property
    def bbox(self) -> Tuple[int, int, int, int]:
        """Returns (min_row, min_col, max_row, max_col)"""
        rows = [r for r, _ in self.pixels]
        cols = [c for _, c in self.pixels]
        return min(rows), min(cols), max(rows), max(cols)
    
    @property
    def height(self) -> int:
        min_r, _, max_r, _ = self.bbox
        return max_r - min_r + 1
    
    @property
    def width(self) -> int:
        _, min_c, _, max_c = self.bbox
        return max_c - min_c + 1
    
    def as_subgrid(self, background: int = 0) -> np.ndarray:
        """Mengonversi objek menjadi array 2D terisolasi sesuai bounding box."""
        min_r, min_c, max_r, max_c = self.bbox
        h, w = self.height, self.width
        sub = np.full((h, w), background, dtype=int)
        for r, c in self.pixels:
            sub[r - min_r, c - min_c] = self.color
        return sub


class Grid:
    """
    Wrapper untuk 2D NumPy array dengan utilitas abstraksi spasial & objek.
    """
    def __init__(self, data: Any):
        if isinstance(data, (list, tuple)):
            self.array = np.array(data, dtype=int)
        elif isinstance(data, np.ndarray):
            self.array = data.astype(int)
        elif isinstance(data, Grid):
            self.array = data.array.copy()
        else:
            raise ValueError(f"Tipe data tidak valid untuk Grid: {type(data)}")
            
        assert self.array.ndim == 2, "Grid harus berbentuk matriks 2D"
        
    @property
    def height(self) -> int:
        return self.array.shape[0]
    
    @property
    def width(self) -> int:
        return self.array.shape[1]
    
    @property
    def shape(self) -> Tuple[int, int]:
        return self.array.shape
    
    @property
    def unique_colors(self) -> Set[int]:
        return set(np.unique(self.array).tolist())
    
    def color_counts(self) -> Dict[int, int]:
        colors, counts = np.unique(self.array, return_counts=True)
        return dict(zip(colors.tolist(), counts.tolist()))
    
    def extract_objects(self, background: int = 0, connectivity: int = 8) -> List[Object]:
        """
        Mengekstrak objek terhubung (Connected Components).
        connectivity: 4 (atas/bawah/kiri/kanan) atau 8 (termasuk diagonal).
        """
        visited = np.zeros_like(self.array, dtype=bool)
        objects = []
        
        # Arah tetangga
        if connectivity == 4:
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        else:
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
            
        for r in range(self.height):
            for c in range(self.width):
                color = int(self.array[r, c])
                if color == background or visited[r, c]:
                    continue
                
                # Flood fill BFS
                pixels = []
                queue = [(r, c)]
                visited[r, c] = True
                
                while queue:
                    curr_r, curr_c = queue.pop(0)
                    pixels.append((curr_r, curr_c))
                    
                    for dr, dc in neighbors:
                        nr, nc = curr_r + dr, curr_c + dc
                        if 0 <= nr < self.height and 0 <= nc < self.width:
                            if not visited[nr, nc] and self.array[nr, nc] == color:
                                visited[nr, nc] = True
                                queue.append((nr, nc))
                                
                objects.append(Object(color=color, pixels=tuple(sorted(pixels))))
                
        return objects
    
    def to_list(self) -> List[List[int]]:
        return self.array.tolist()
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Grid):
            return np.array_equal(self.array, other.array)
        elif isinstance(other, (list, np.ndarray)):
            return np.array_equal(self.array, np.array(other))
        return False

    def __repr__(self) -> str:
        return f"Grid(shape={self.shape}, colors={list(self.unique_colors)})\n{self.array}"


@dataclass
class Example:
    """Satu pasang contoh input-output training."""
    input_grid: Grid
    output_grid: Grid


@dataclass
class Task:
    """
    Satu tugas ARC lengkap:
    - train: List pasangan (input, output)
    - test: List pasangan (input, output_opsional)
    """
    task_id: str
    train: List[Example]
    test: List[Example]
    
    @classmethod
    def from_dict(cls, task_id: str, data: Dict[str, Any]) -> "Task":
        train_examples = [
            Example(
                input_grid=Grid(pair["input"]),
                output_grid=Grid(pair["output"])
            )
            for pair in data.get("train", [])
        ]
        
        test_examples = [
            Example(
                input_grid=Grid(pair["input"]),
                output_grid=Grid(pair["output"]) if "output" in pair else Grid([[0]])
            )
            for pair in data.get("test", [])
        ]
        
        return cls(task_id=task_id, train=train_examples, test=test_examples)
    
    @classmethod
    def load_json(cls, file_path: str) -> Dict[str, "Task"]:
        """Memuat file kumpulan task ARC format JSON."""
        with open(file_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
            
        tasks = {}
        for task_id, task_data in raw_data.items():
            tasks[task_id] = cls.from_dict(task_id, task_data)
        return tasks
