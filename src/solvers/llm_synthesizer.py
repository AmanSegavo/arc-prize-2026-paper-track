"""
LLM Code Synthesizer & Reflexion Loop for ARC-AGI-2 Static Grid Reasoning.
Menghasilkan solusi program Python menggunakan LLM dengan mekanisme verifikasi dan self-correction.
"""

from typing import List, Dict, Any, Optional, Tuple
import re
from src.core.grid import Task, Grid
from src.evaluator.verifier import TaskVerifier


ARC_SYSTEM_PROMPT = """You are an expert AI researcher specializing in the Abstraction and Reasoning Corpus (ARC-AGI-2).
Your goal is to discover the underlying transformation rule from the given training pairs and write a robust Python function `solve(grid: np.ndarray) -> np.ndarray`.

Core Principles of ARC:
1. Objectness: Cohesive objects, connected components, boundaries, shapes.
2. Goal-directedness: Alignment, gravity, containment, intersection.
3. Basic Geometry & Topology: Rotation, reflection, symmetry, scaling, enclosed areas.
4. Counting & Ordering: Sorting by size, count of colors, majority/minority colors.

Instructions:
- Write clean, fully self-contained Python code.
- Define a function `def solve(grid: np.ndarray) -> np.ndarray:`.
- Include reasoning comments explaining the hypothesis.
- Enclose your code strictly inside ```python ... ``` markdown blocks.
"""


def format_task_prompt(task: Task) -> str:
    """Format satu task ARC menjadi string prompt untuk LLM."""
    prompt_lines = [f"Task ID: {task.task_id}", "\n## Training Examples:"]
    
    for idx, ex in enumerate(task.train):
        prompt_lines.append(f"\n### Example {idx + 1}:")
        prompt_lines.append(f"Input ({ex.input_grid.height}x{ex.input_grid.width}):")
        prompt_lines.append(str(ex.input_grid.to_list()))
        prompt_lines.append(f"Output ({ex.output_grid.height}x{ex.output_grid.width}):")
        prompt_lines.append(str(ex.output_grid.to_list()))
        
    prompt_lines.append("\n## Test Inputs to Solve:")
    for idx, ex in enumerate(task.test):
        prompt_lines.append(f"\n### Test {idx + 1}:")
        prompt_lines.append(f"Input ({ex.input_grid.height}x{ex.input_grid.width}):")
        prompt_lines.append(str(ex.input_grid.to_list()))
        
    prompt_lines.append("\nProvide your step-by-step reasoning and Python `solve` function:")
    return "\n".join(prompt_lines)


def format_feedback_prompt(task: Task, candidate_code: str, verification_details: Dict[str, Any]) -> str:
    """Format feedback pesan kesalahan untuk siklus perbaikan (Reflexion)."""
    feedback_lines = [
        "Your previous Python code did NOT perfectly solve all training examples.",
        "\n### Previous Code:",
        f"```python\n{candidate_code}\n```",
        "\n### Execution Feedback on Training Examples:"
    ]
    
    for ex_info in verification_details.get("examples", []):
        idx = ex_info.get("example_idx", 0) + 1
        if ex_info.get("success"):
            feedback_lines.append(f"- Example {idx}: PASSED (100% pixel match)")
        elif "error" in ex_info:
            feedback_lines.append(f"- Example {idx}: FAILED with Exception: {ex_info['error']}")
        else:
            acc = ex_info.get("pixel_acc", 0.0) * 100
            pred_shape = ex_info.get("pred_shape")
            target_shape = ex_info.get("target_shape")
            feedback_lines.append(
                f"- Example {idx}: FAILED ({acc:.1f}% pixel accuracy). "
                f"Predicted shape: {pred_shape}, Expected shape: {target_shape}"
            )
            
    feedback_lines.append("\nPlease re-analyze the geometric/topological rules, correct the mistakes, and provide a revised `solve` function.")
    return "\n".join(feedback_lines)


def extract_python_code(response_text: str) -> Optional[str]:
    """Mengekstrak blok kode Python dari response LLM."""
    match = re.search(r"```python\n(.*?)\n```", response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    match = re.search(r"```(.*?)```", response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None
