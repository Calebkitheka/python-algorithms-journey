# src/sorting/advanced.py
from typing import List, Any

def merge_sort(arr: List[Any]) -> None:
    """Stable O(n log n) divide & conquer. Uses O(n) extra space via slicing."""
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # <= ensures stability
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def _lomuto_partition(arr: List[Any], low: int, high: int) -> int:
    """Partition scheme: pivot = arr[high]. Returns final pivot index."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def _quick_sort_recursive(arr: List[Any], low: int, high: int) -> None:
    if low < high:
        pi = _lomuto_partition(arr, low, high)
        _quick_sort_recursive(arr, low, pi - 1)
        _quick_sort_recursive(arr, pi + 1, high)


def quick_sort(arr: List[Any]) -> None:
    """Unstable O(n log n) avg, O(n²) worst. In-place, cache-friendly."""
    _quick_sort_recursive(arr, 0, len(arr) - 1)


def _heapify(arr: List[Any], n: int, i: int) -> None:
    """Maintain max-heap property for subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


def heap_sort(arr: List[Any]) -> None:
    """Unstable O(n log n). In-place, but poor cache locality."""
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)