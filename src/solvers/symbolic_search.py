"""
Symbolic DSL Search Solver for ARC-AGI-2.
Mencari kombinasi fungsi transformasi DSL secara sistematis untuk memecahkan task grid.
"""

from typing import List, Tuple, Dict, Any, Optional, Callable
from src.core.grid import Task, Grid
from src.evaluator.verifier import TaskVerifier
import src.dsl.primitives as dsl


class SymbolicSearchSolver:
    """
    Solver pencarian program simbolik berbasis DSL.
    """
    def __init__(self, max_depth: int = 2):
        self.max_depth = max_depth
        
        # Koleksi fungsi atomik 1-argumen
        self.unary_primitives: Dict[str, Callable[[Grid], Grid]] = {
            "identity": lambda g: g,
            "rot90": dsl.rot90,
            "rot180": dsl.rot180,
            "rot270": dsl.rot270,
            "flip_h": dsl.flip_h,
            "flip_v": dsl.flip_v,
            "transpose": dsl.transpose,
            "anti_transpose": dsl.anti_transpose,
            "crop_nonzero": dsl.crop_nonzero,
            "remove_empty_lines": dsl.remove_empty_lines,
            "crop_largest_object": dsl.crop_largest_object,
            "crop_smallest_object": dsl.crop_smallest_object,
            "outline": dsl.outline,
            "gravity_down": lambda g: dsl.apply_gravity(g, "down"),
            "gravity_up": lambda g: dsl.apply_gravity(g, "up"),
            "gravity_left": lambda g: dsl.apply_gravity(g, "left"),
            "gravity_right": lambda g: dsl.apply_gravity(g, "right"),
            "scale_up_2x": lambda g: dsl.scale_up(g, 2),
            "scale_up_3x": lambda g: dsl.scale_up(g, 3),
            "tile_2x2": lambda g: dsl.tile(g, 2, 2),
            "tile_3x3": lambda g: dsl.tile(g, 3, 3),
        }

    def solve(self, task: Task) -> Optional[Tuple[Callable[[Grid], Grid], str]]:
        """
        Mencari fungsi transformasi yang menghasilkan 100% akurasi pada training set.
        Returns (solution_fn, program_description) jika ditemukan, atau None.
        """
        # 1. Cek primitive 1 langkah (Depth 1)
        for name, fn in self.unary_primitives.items():
            is_perfect, score, _ = TaskVerifier.verify_callable(fn, task)
            if is_perfect:
                return fn, f"{name}(grid)"
                
        # 2. Cek transformasi warna (Color permutation / substitution)
        all_colors = list(range(10))
        input_colors = set()
        output_colors = set()
        for ex in task.train:
            input_colors.update(ex.input_grid.unique_colors)
            output_colors.update(ex.output_grid.unique_colors)
            
        for c_in in input_colors:
            for c_out in output_colors:
                if c_in == c_out:
                    continue
                color_fn = lambda g, ci=c_in, co=c_out: dsl.replace_color(g, ci, co)
                is_perfect, score, _ = TaskVerifier.verify_callable(color_fn, task)
                if is_perfect:
                    return color_fn, f"replace_color(grid, {c_in}, {c_out})"

        # 3. Cek fill enclosed
        for c in output_colors:
            fill_fn = lambda g, col=c: dsl.fill_enclosed(g, col)
            is_perfect, score, _ = TaskVerifier.verify_callable(fill_fn, task)
            if is_perfect:
                return fill_fn, f"fill_enclosed(grid, {c})"

        # 4. Cek komposisi 2 langkah (Depth 2) jika diizinkan
        if self.max_depth >= 2:
            for name1, fn1 in self.unary_primitives.items():
                for name2, fn2 in self.unary_primitives.items():
                    if name1 == "identity" or name2 == "identity":
                        continue
                    composed_fn = lambda g, f1=fn1, f2=fn2: f2(f1(g))
                    is_perfect, score, _ = TaskVerifier.verify_callable(composed_fn, task)
                    if is_perfect:
                        return composed_fn, f"{name2}({name1}(grid))"

        return None
