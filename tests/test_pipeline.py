import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
from src.core.grid import Grid, Task, Example, Object
from src.dsl import primitives as dsl
from src.evaluator.verifier import TaskVerifier
from src.solvers.symbolic_search import SymbolicSearchSolver
from src.solvers.llm_synthesizer import format_task_prompt, extract_python_code, ARC_SYSTEM_PROMPT


def test_grid_and_objects():
    # Grid 5x5 dengan 1 kotak warna 2 (red) ukuran 2x2
    arr = [
        [0, 0, 0, 0, 0],
        [0, 2, 2, 0, 0],
        [0, 2, 2, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3]
    ]
    grid = Grid(arr)
    assert grid.height == 5 and grid.width == 5
    assert grid.unique_colors == {0, 2, 3}
    
    objects = grid.extract_objects(background=0, connectivity=4)
    assert len(objects) == 2  # Objek 2x2 merah dan 1 piksel hijau
    print("[PASS] Grid and object extraction test passed.")


def test_dsl_rotations_and_gravity():
    arr = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]
    ]
    grid = Grid(arr)
    r90 = dsl.rot90(grid)
    assert r90.array[0, 2] == 1
    
    # Gravitasi ke bawah
    grav_down = dsl.apply_gravity(grid, "down")
    assert grav_down.array[2, 0] == 1
    assert grav_down.array[2, 1] == 2
    assert grav_down.array[2, 2] == 3
    print("[PASS] DSL geometric and gravity primitives test passed.")


def test_fill_enclosed():
    # Cincin tertutup 3x3 dengan lubang di tengah
    ring = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    grid = Grid(ring)
    filled = dsl.fill_enclosed(grid, fill_color=4)
    assert filled.array[1, 1] == 4
    print("[PASS] Topological fill_enclosed test passed.")


def test_symbolic_solver():
    # Task rotasi 90 derajat
    ex1_in = Grid([[1, 2], [3, 4]])
    ex1_out = Grid([[3, 1], [4, 2]])
    
    ex2_in = Grid([[5, 6], [7, 8]])
    ex2_out = Grid([[7, 5], [8, 6]])
    
    task = Task(
        task_id="test_rot90_task",
        train=[Example(ex1_in, ex1_out), Example(ex2_in, ex2_out)],
        test=[Example(ex1_in, ex1_out)]
    )
    
    solver = SymbolicSearchSolver(max_depth=1)
    res = solver.solve(task)
    assert res is not None, "Solver should have found a solution"
    fn, desc = res
    print(f"[PASS] Symbolic solver found solution: {desc}")
    
    # Verifikasi dengan Verifier
    is_perfect, score, _ = TaskVerifier.verify_callable(fn, task)
    assert is_perfect and score == 1.0
    print("[PASS] TaskVerifier verification test passed.")


def test_llm_code_verifier():
    ex1_in = Grid([[1, 0], [0, 0]])
    ex1_out = Grid([[1, 1], [1, 1]])
    
    task = Task(
        task_id="test_llm_code_task",
        train=[Example(ex1_in, ex1_out)],
        test=[Example(ex1_in, ex1_out)]
    )
    
    code = """
import numpy as np

def solve(grid: np.ndarray) -> np.ndarray:
    return np.full_like(grid, 1)
"""
    is_perfect, score, _ = TaskVerifier.verify_python_code(code, task)
    assert is_perfect and score == 1.0
    print("[PASS] Python string code verification test passed.")


if __name__ == "__main__":
    print("--- Running Pipeline Tests ---")
    test_grid_and_objects()
    test_dsl_rotations_and_gravity()
    test_fill_enclosed()
    test_symbolic_solver()
    test_llm_code_verifier()
    print("--- All Tests Passed Successfully! ---")
