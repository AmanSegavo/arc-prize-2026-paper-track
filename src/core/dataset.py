"""
ARC Dataset Loader and Manager.
Memuat, memfilter, dan mengelola koleksi task dari direktori training dan evaluation.
"""

import os
import json
import glob
from typing import Dict, List, Optional, Iterator
from src.core.grid import Task, Example, Grid


class ARCDataset:
    """
    Manajer Dataset ARC-AGI untuk memuat koleksi task dari direktori atau file JSON.
    """
    def __init__(self, tasks: Dict[str, Task]):
        self.tasks = tasks
        
    def __len__(self) -> int:
        return len(self.tasks)
    
    def __getitem__(self, task_id: str) -> Task:
        return self.tasks[task_id]
    
    def __iter__(self) -> Iterator[Task]:
        return iter(self.tasks.values())
    
    @property
    def task_ids(self) -> List[str]:
        return list(self.tasks.keys())
    
    @classmethod
    def from_directory(cls, dir_path: str, limit: Optional[int] = None) -> "ARCDataset":
        """
        Memuat semua file JSON individual dalam direktori.
        """
        json_files = glob.glob(os.path.join(dir_path, "*.json"))
        if limit is not None:
            json_files = json_files[:limit]
            
        tasks = {}
        for file_path in json_files:
            task_id = os.path.splitext(os.path.basename(file_path))[0]
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            tasks[task_id] = Task.from_dict(task_id, data)
            
        return cls(tasks)
    
    @classmethod
    def load_training(cls, data_root: Optional[str] = None, limit: Optional[int] = None) -> "ARCDataset":
        if data_root is None:
            data_root = os.path.join(os.path.dirname(__file__), "..", "..", "data", "arc")
        train_dir = os.path.join(data_root, "training")
        return cls.from_directory(train_dir, limit=limit)
    
    @classmethod
    def load_evaluation(cls, data_root: Optional[str] = None, limit: Optional[int] = None) -> "ARCDataset":
        if data_root is None:
            data_root = os.path.join(os.path.dirname(__file__), "..", "..", "data", "arc")
        eval_dir = os.path.join(data_root, "evaluation")
        return cls.from_directory(eval_dir, limit=limit)
    
    def filter_by_grid_size(self, max_height: int = 15, max_width: int = 15) -> "ARCDataset":
        """Menyaring task di mana semua input/output tidak melebihi dimensi tertentu."""
        filtered = {}
        for tid, task in self.tasks.items():
            valid = True
            for ex in task.train:
                if ex.input_grid.height > max_height or ex.input_grid.width > max_width:
                    valid = False
                    break
                if ex.output_grid.height > max_height or ex.output_grid.width > max_width:
                    valid = False
                    break
            if valid:
                filtered[tid] = task
        return ARCDataset(filtered)
