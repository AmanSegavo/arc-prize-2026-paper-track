"""
ASCII and Terminal Visualizer for ARC Tasks and Predictions.
Membantu visualisasi grid input, output, dan prediksi solver secara langsung di konsol.
"""

import os
import sys
from typing import Optional

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.grid import Grid, Task, COLOR_NAMES
from src.core.dataset import ARCDataset
from src.solvers.symbolic_search import SymbolicSearchSolver


# Simbol visual terminal untuk tiap warna (0-9)
COLOR_SYMBOLS = {
    0: " . ",  # Black / Background
    1: " 1 ",  # Blue
    2: " 2 ",  # Red
    3: " 3 ",  # Green
    4: " 4 ",  # Yellow
    5: " 5 ",  # Grey
    6: " 6 ",  # Magenta
    7: " 7 ",  # Orange
    8: " 8 ",  # Azure
    9: " 9 "   # Maroon
}


def render_grid_ascii(grid: Grid, title: str = "") -> str:
    lines = []
    if title:
        lines.append(f"[{title}] Shape: {grid.height}x{grid.width}")
    
    border = "+---" * grid.width + "+"
    lines.append(border)
    for row in grid.array:
        row_str = "|" + "".join(f" {val} |" if val != 0 else " . |" for val in row)
        lines.append(row_str)
        lines.append(border)
        
    return "\n".join(lines)


def display_task(task: Task, solver: Optional[SymbolicSearchSolver] = None):
    print(f"\n=======================================================")
    print(f" TASK: {task.task_id} (Train: {len(task.train)}, Test: {len(task.test)})")
    print(f"=======================================================")
    
    for idx, ex in enumerate(task.train, 1):
        print(f"\n--- [Train Example {idx}] ---")
        in_str = render_grid_ascii(ex.input_grid, f"Input {idx}").split("\n")
        out_str = render_grid_ascii(ex.output_grid, f"Target Output {idx}").split("\n")
        
        max_lines = max(len(in_str), len(out_str))
        in_width = max(len(l) for l in in_str)
        
        for i in range(max_lines):
            left = in_str[i] if i < len(in_str) else " " * in_width
            right = out_str[i] if i < len(out_str) else ""
            print(f"{left.ljust(in_width + 4)} =>    {right}")
            
    if solver:
        print("\n--- [Solver Inference] ---")
        res = solver.solve(task)
        if res:
            fn, desc = res
            print(f"[+] SOLVED! Ditemukan transformasi: {desc}")
            for idx, ex in enumerate(task.test, 1):
                pred = fn(ex.input_grid)
                print(render_grid_ascii(pred, f"Test Prediction {idx}"))
        else:
            print("[-] Solver belum menemukan solusi langsung dengan primitive saat ini.")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--task_id", type=str, default="00d62c1b", help="Task ID to visualize")
    parser.add_argument("--split", type=str, default="training")
    args = parser.parse_args()
    
    dataset = ARCDataset.load_training() if args.split == "training" else ARCDataset.load_evaluation()
    if args.task_id in dataset.tasks:
        display_task(dataset[args.task_id], solver=SymbolicSearchSolver())
    else:
        print(f"Task {args.task_id} tidak ditemukan.")
