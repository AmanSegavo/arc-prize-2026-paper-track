"""
Domain-Specific Language (DSL) Primitives for ARC-AGI-2 Static Grid Reasoning.
Fungsi-fungsi transformasi modular untuk geometri, warna, topologi, dan manipulasi objek.
"""

from typing import List, Tuple, Dict, Any, Callable, Optional
import numpy as np
from src.core.grid import Grid, Object


# ==========================================
# 1. Geometric & Symmetry Primitives
# ==========================================

def rot90(grid: Grid) -> Grid:
    """Rotasi grid 90 derajat searah jarum jam."""
    return Grid(np.rot90(grid.array, k=-1))

def rot180(grid: Grid) -> Grid:
    """Rotasi grid 180 derajat."""
    return Grid(np.rot90(grid.array, k=2))

def rot270(grid: Grid) -> Grid:
    """Rotasi grid 270 derajat searah jarum jam (90 derajat berlawanan)."""
    return Grid(np.rot90(grid.array, k=1))

def flip_h(grid: Grid) -> Grid:
    """Refleksi horizontal (kiri-kanan)."""
    return Grid(np.fliplr(grid.array))

def flip_v(grid: Grid) -> Grid:
    """Refleksi vertikal (atas-bawah)."""
    return Grid(np.flipud(grid.array))

def transpose(grid: Grid) -> Grid:
    """Transpose matriks grid."""
    return Grid(grid.array.T)


# ==========================================
# 2. Color & Filter Primitives
# ==========================================

def replace_color(grid: Grid, old_color: int, new_color: int) -> Grid:
    """Mengganti semua piksel dengan old_color menjadi new_color."""
    arr = grid.array.copy()
    arr[arr == old_color] = new_color
    return Grid(arr)

def filter_color(grid: Grid, target_color: int, background: int = 0) -> Grid:
    """Menyisakan hanya target_color, sisanya diubah menjadi background."""
    arr = np.full_like(grid.array, background)
    mask = (grid.array == target_color)
    arr[mask] = target_color
    return Grid(arr)

def most_frequent_color(grid: Grid, exclude_background: bool = True, background: int = 0) -> int:
    """Mencari warna yang paling banyak muncul."""
    counts = grid.color_counts()
    if exclude_background and background in counts and len(counts) > 1:
        del counts[background]
    return max(counts, key=counts.get)

def least_frequent_color(grid: Grid, exclude_background: bool = True, background: int = 0) -> int:
    """Mencari warna yang paling sedikit muncul."""
    counts = grid.color_counts()
    if exclude_background and background in counts and len(counts) > 1:
        del counts[background]
    return min(counts, key=counts.get)


# ==========================================
# 3. Cropping, Scaling & Tiling Primitives
# ==========================================

def crop_bbox(grid: Grid, min_r: int, min_c: int, max_r: int, max_c: int) -> Grid:
    """Memotong area subgrid tertentu."""
    return Grid(grid.array[min_r:max_r+1, min_c:max_c+1])

def crop_nonzero(grid: Grid, background: int = 0) -> Grid:
    """Memotong grid hanya pada area yang berisi objek non-background."""
    nonzeros = np.argwhere(grid.array != background)
    if len(nonzeros) == 0:
        return Grid([[background]])
    min_r, min_c = nonzeros.min(axis=0)
    max_r, max_c = nonzeros.max(axis=0)
    return crop_bbox(grid, min_r, min_c, max_r, max_c)

def scale_up(grid: Grid, factor: int) -> Grid:
    """Memperbesar (upscale) ukuran setiap piksel menjadi blok factor x factor."""
    assert factor >= 1
    return Grid(np.repeat(np.repeat(grid.array, factor, axis=0), factor, axis=1))

def tile(grid: Grid, repeat_r: int, repeat_c: int) -> Grid:
    """Mengulang pola grid sebanyak repeat_r baris dan repeat_c kolom."""
    return Grid(np.tile(grid.array, (repeat_r, repeat_c)))


# ==========================================
# 4. Topological & Morphology Primitives
# ==========================================

def outline(grid: Grid, background: int = 0, outline_color: Optional[int] = None) -> Grid:
    """
    Mengekstrak garis batas (boundary/outline) dari semua objek.
    """
    arr = grid.array
    h, w = arr.shape
    out = np.full((h, w), background, dtype=int)
    
    for r in range(h):
        for c in range(w):
            if arr[r, c] != background:
                # Periksa apakah bertetangga dengan background atau tepi
                is_boundary = False
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < h and 0 <= nc < w) or arr[nr, nc] == background:
                        is_boundary = True
                        break
                if is_boundary:
                    out[r, c] = outline_color if outline_color is not None else arr[r, c]
    return Grid(out)

def fill_enclosed(grid: Grid, fill_color: int, background: int = 0) -> Grid:
    """
    Mengisi rongga atau area background yang terkurung sepenuhnya (enclosed holes).
    """
    arr = grid.array.copy()
    h, w = arr.shape
    visited_exterior = np.zeros((h, w), dtype=bool)
    
    # BFS dari batas luar grid untuk menandai background eksterior
    queue = []
    for r in range(h):
        for c in [0, w - 1]:
            if arr[r, c] == background and not visited_exterior[r, c]:
                visited_exterior[r, c] = True
                queue.append((r, c))
    for c in range(w):
        for r in [0, h - 1]:
            if arr[r, c] == background and not visited_exterior[r, c]:
                visited_exterior[r, c] = True
                queue.append((r, c))
                
    while queue:
        cr, cc = queue.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < h and 0 <= nc < w:
                if not visited_exterior[nr, nc] and arr[nr, nc] == background:
                    visited_exterior[nr, nc] = True
                    queue.append((nr, nc))
                    
    # Area background yang TIDAK terjangkau dari eksterior berarti terkurung (enclosed)
    for r in range(h):
        for c in range(w):
            if arr[r, c] == background and not visited_exterior[r, c]:
                arr[r, c] = fill_color
                
    return Grid(arr)

def apply_gravity(grid: Grid, direction: str = "down", background: int = 0) -> Grid:
    """
    Menerapkan efek gravitasi pada piksel non-background ('down', 'up', 'left', 'right').
    """
    arr = grid.array.copy()
    h, w = arr.shape
    
    if direction == "down":
        for c in range(w):
            col = arr[:, c]
            nonzeros = col[col != background]
            new_col = np.full(h, background, dtype=int)
            if len(nonzeros) > 0:
                new_col[-len(nonzeros):] = nonzeros
            arr[:, c] = new_col
    elif direction == "up":
        for c in range(w):
            col = arr[:, c]
            nonzeros = col[col != background]
            new_col = np.full(h, background, dtype=int)
            if len(nonzeros) > 0:
                new_col[:len(nonzeros)] = nonzeros
            arr[:, c] = new_col
    elif direction == "left":
        for r in range(h):
            row = arr[r, :]
            nonzeros = row[row != background]
            new_row = np.full(w, background, dtype=int)
            if len(nonzeros) > 0:
                new_row[:len(nonzeros)] = nonzeros
            arr[r, :] = new_row
    elif direction == "right":
        for r in range(h):
            row = arr[r, :]
            nonzeros = row[row != background]
            new_row = np.full(w, background, dtype=int)
            if len(nonzeros) > 0:
                new_row[-len(nonzeros):] = nonzeros
            arr[r, :] = new_row
            
    return Grid(arr)


def anti_transpose(grid: Grid) -> Grid:
    """Anti-diagonal transpose."""
    return Grid(np.fliplr(np.flipud(grid.array.T)))

def remove_empty_lines(grid: Grid, background: int = 0) -> Grid:
    """Menghapus baris dan kolom yang seluruhnya terdiri dari background."""
    arr = grid.array
    non_empty_rows = ~np.all(arr == background, axis=1)
    non_empty_cols = ~np.all(arr == background, axis=0)
    if not np.any(non_empty_rows) or not np.any(non_empty_cols):
        return Grid([[background]])
    return Grid(arr[non_empty_rows][:, non_empty_cols])

def crop_largest_object(grid: Grid, background: int = 0) -> Grid:
    """Mengekstrak bounding box dari objek terbesar."""
    objects = grid.extract_objects(background=background)
    if not objects:
        return grid
    largest = max(objects, key=lambda obj: obj.size)
    min_r, min_c, max_r, max_c = largest.bbox
    return crop_bbox(grid, min_r, min_c, max_r, max_c)

def crop_smallest_object(grid: Grid, background: int = 0) -> Grid:
    """Mengekstrak bounding box dari objek terkecil."""
    objects = grid.extract_objects(background=background)
    if not objects:
        return grid
    smallest = min(objects, key=lambda obj: obj.size)
    min_r, min_c, max_r, max_c = smallest.bbox
    return crop_bbox(grid, min_r, min_c, max_r, max_c)


# ==========================================
# 5. Composition & Overlay Primitives
# ==========================================

def overlay(base: Grid, top: Grid, background: int = 0) -> Grid:
    """
    Menimpa grid top di atas base (piksel top non-background menggantikan base).
    Jika dimensi berbeda, disesuaikan ke ukuran maksimum.
    """
    h = max(base.height, top.height)
    w = max(base.width, top.width)
    
    out = np.full((h, w), background, dtype=int)
    out[:base.height, :base.width] = base.array
    
    top_mask = (top.array != background)
    out[:top.height, :top.width][top_mask] = top.array[top_mask]
    
    return Grid(out)
