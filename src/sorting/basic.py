# src/sorting/basic.py
from typing import List, Any

def bubble_sort(arr: List[Any], trace: bool = False) -> None:
    """O(n^2) stable sort. Optimized with early-exit flag."""
    n = len(arr)
    comparisons = swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
                if trace:
                    print(f"[Bubble] Swap {arr[j+1]} ↔ {arr[j]} | {arr}")
        if not swapped:
            break
    if trace:
        print(f"[Bubble] Complete. Comparisons: {comparisons}, Swaps: {swaps}")

def insertion_sort(arr: List[Any], trace: bool = False) -> None:
    """O(n^2) stable sort. Highly efficient for nearly-sorted or small arrays."""
    n = len(arr)
    shifts = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
            if trace:
                print(f"[Insertion] Shift right | {arr}")
        arr[j + 1] = key
        if trace:
            print(f"[Insertion] Insert {key} | {arr}")
    if trace:
        print(f"[Insertion] Complete. Shifts: {shifts}")

def selection_sort(arr: List[Any], trace: bool = False) -> None:
    """O(n^2) unstable sort. Minimizes swaps, poor cache locality."""
    n = len(arr)
    comparisons = swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            if trace:
                print(f"[Selection] Swap {arr[i]} ↔ {arr[min_idx]} | {arr}")
    if trace:
        print(f"[Selection] Complete. Comparisons: {comparisons}, Swaps: {swaps}")