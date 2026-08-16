"""
Execution Verifier and Sandbox for ARC-AGI Solvers.
Memvalidasi kandidat fungsi Python terhadap seluruh contoh training sebuah Task.
"""

from typing import Dict, Any, Tuple, Optional, Callable
import traceback
import numpy as np
from src.core.grid import Task, Grid, Example


class TaskVerifier:
    """
    Eksekusi dan evaluasi kandidat transformasi terhadap Task.
    """
    
    @staticmethod
    def verify_callable(transform_fn: Callable[[Grid], Grid], task: Task) -> Tuple[bool, float, Dict[str, Any]]:
        """
        Menguji callable function terhadap semua contoh training.
        Returns:
            - is_perfect_match (bool): True jika 100% tepat pada semua training pair.
            - score (float): Rata-rata kemiripan (0.0 s/d 1.0).
            - details (dict): Rincian per contoh (error, shape match, pixel match).
        """
        total_examples = len(task.train)
        perfect_count = 0
        pixel_accuracies = []
        details = []
        
        for idx, ex in enumerate(task.train):
            try:
                pred_grid = transform_fn(ex.input_grid)
                if not isinstance(pred_grid, Grid):
                    pred_grid = Grid(pred_grid)
                    
                target = ex.output_grid
                
                # Check exact equality
                if pred_grid == target:
                    perfect_count += 1
                    pixel_accuracies.append(1.0)
                    details.append({
                        "example_idx": idx,
                        "success": True,
                        "shape_match": True,
                        "pixel_acc": 1.0
                    })
                else:
                    # Hitung kemiripan parsial
                    shape_match = (pred_grid.shape == target.shape)
                    if shape_match:
                        acc = np.mean(pred_grid.array == target.array)
                    else:
                        acc = 0.0
                    pixel_accuracies.append(float(acc))
                    details.append({
                        "example_idx": idx,
                        "success": False,
                        "shape_match": shape_match,
                        "pixel_acc": float(acc),
                        "pred_shape": pred_grid.shape,
                        "target_shape": target.shape
                    })
            except Exception as e:
                pixel_accuracies.append(0.0)
                details.append({
                    "example_idx": idx,
                    "success": False,
                    "error": str(e),
                    "traceback": traceback.format_exc()
                })
                
        is_perfect = (perfect_count == total_examples)
        avg_score = float(np.mean(pixel_accuracies)) if pixel_accuracies else 0.0
        
        return is_perfect, avg_score, {"perfect_count": perfect_count, "total": total_examples, "examples": details}

    @staticmethod
    def verify_python_code(code_str: str, task: Task, entrypoint: str = "solve") -> Tuple[bool, float, Dict[str, Any]]:
        """
        Mengeksekusi kode Python string di lingkungan terisolasi dan menguji hasilnya.
        """
        # Lingkup eksekusi lokal dengan modul dasar yang aman
        exec_globals = {
            "np": np,
            "numpy": np,
            "Grid": Grid,
        }
        exec_locals = {}
        
        try:
            exec(code_str, exec_globals, exec_locals)
            if entrypoint not in exec_locals:
                return False, 0.0, {"error": f"Fungsi entrypoint '{entrypoint}' tidak ditemukan pada kode."}
            
            fn = exec_locals[entrypoint]
            
            # Bungkus jika fungsi menerima input berupa list atau numpy alih-alih Grid
            def wrapped_fn(grid: Grid) -> Grid:
                res = fn(grid.array) if not hasattr(fn, "__annotations__") or fn.__annotations__.get("grid") != Grid else fn(grid)
                return Grid(res) if not isinstance(res, Grid) else res
            
            return TaskVerifier.verify_callable(wrapped_fn, task)
            
        except Exception as e:
            return False, 0.0, {
                "error": f"Syntax / Compile Error: {str(e)}",
                "traceback": traceback.format_exc()
            }
