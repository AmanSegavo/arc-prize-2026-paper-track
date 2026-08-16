"""
ARC Benchmark Runner & Evaluation Harness.
Menjalankan solver pada kumpulan task ARC asli, mengukur akurasi, waktu eksekusi,
dan menghasilkan laporan statistik untuk paper/write-up.
"""

import os
import sys
import time
from typing import Dict, Any, List

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.core.dataset import ARCDataset
from src.core.grid import Task, Grid
from src.solvers.symbolic_search import SymbolicSearchSolver
from src.evaluator.verifier import TaskVerifier


def run_benchmark(split: str = "training", limit: int = 50, max_depth: int = 2) -> Dict[str, Any]:
    print(f"\n=======================================================")
    print(f"[*] Menjalankan Benchmark ARC-AGI-2 ({split.upper()} SET)")
    print(f"[*] Jumlah task: {limit} | Solver Max Depth: {max_depth}")
    print(f"=======================================================\n")
    
    if split == "training":
        dataset = ARCDataset.load_training(limit=limit)
    else:
        dataset = ARCDataset.load_evaluation(limit=limit)
        
    solver = SymbolicSearchSolver(max_depth=max_depth)
    
    solved_tasks = []
    failed_tasks = []
    total_time = 0.0
    task_times = []
    
    start_total = time.time()
    
    for idx, (task_id, task) in enumerate(dataset.tasks.items(), 1):
        t0 = time.time()
        result = solver.solve(task)
        elapsed = time.time() - t0
        task_times.append(elapsed)
        
        if result is not None:
            fn, desc = result
            solved_tasks.append({
                "task_id": task_id,
                "solution": desc,
                "time_sec": elapsed,
                "train_examples": len(task.train)
            })
            print(f"[{idx:03d}/{len(dataset):03d}] Task {task_id} -> [SOLVED in {elapsed:.3f}s]: {desc}", flush=True)
        else:
            failed_tasks.append(task_id)
            print(f"[{idx:03d}/{len(dataset):03d}] Task {task_id} -> [UNSOLVED in {elapsed:.3f}s]", flush=True)
            
    total_time = time.time() - start_total
    accuracy = (len(solved_tasks) / len(dataset)) * 100 if dataset else 0.0
    avg_time = sum(task_times) / len(task_times) if task_times else 0.0
    
    print("\n" + "=" * 55)
    print("                HASIL BENCHMARK")
    print("=" * 55)
    print(f"Total Tasks Diuji      : {len(dataset)}")
    print(f"Berhasil Diselesaikan  : {len(solved_tasks)}")
    print(f"Akurasi Sempurna       : {accuracy:.2f}% ({len(solved_tasks)}/{len(dataset)})")
    print(f"Rata-rata Waktu / Task : {avg_time * 1000:.2f} ms")
    print(f"Total Waktu Eksekusi   : {total_time:.2f} detik")
    print("=" * 55)
    
    if solved_tasks:
        print("\nContoh Solusi yang Berhasil Ditemukan:")
        for st in solved_tasks[:10]:
            print(f" - {st['task_id']}: {st['solution']} ({st['time_sec']:.3f}s)")
            
    return {
        "split": split,
        "total": len(dataset),
        "solved_count": len(solved_tasks),
        "accuracy_pct": accuracy,
        "avg_time_ms": avg_time * 1000,
        "solved_tasks": solved_tasks,
        "failed_tasks": failed_tasks
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run ARC-AGI-2 Benchmark")
    parser.add_argument("--split", choices=["training", "evaluation"], default="training")
    parser.add_argument("--limit", type=int, default=50, help="Number of tasks to evaluate")
    parser.add_argument("--depth", type=int, default=2, help="Solver search depth")
    args = parser.parse_args()
    
    run_benchmark(split=args.split, limit=args.limit, max_depth=args.depth)
