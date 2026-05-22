# 🐍 Algo Playground

My Python algorithms learning journey, documented and tested.

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]"

# 📘 Algorithm Learning Journey

## Week 1: Foundations & Core Data Structures
### Day 2: Linked Lists Implementation
- 🎯 Goal: Build Singly & Doubly Linked Lists with O(1)/O(n) guarantees
- 📐 Algorithms: `insert_head`, `insert_tail`, `delete`, `search`, `__iter__`
- ⏱️ Time/Space Complexity:
  | Operation      | Singly | Doubly |
  |----------------|--------|--------|
  | Insert Head    | O(1)   | O(1)   |
  | Insert Tail    | O(n)   | O(1)*  |
  | Delete         | O(n)   | O(n)   |
  | Search         | O(n)   | O(n)   |
  | Space/Node     | 2 refs | 3 refs |
  *Doubly tracks `_tail` pointer
- 🐛 Pitfall & Fix: Forgetting to update `prev`/`next` when deleting head/tail. Fixed by checking edge cases first before pointer reassignment.
- 🔍 Book Reference: Hetland Ch. 3 (Linked Structures, Invariants)
- 📈 Benchmark: Pending (will compare with `collections.deque` & `list`)

### Day 4: Basic Sorting Algorithms
- 🎯 Goal: Implement Bubble, Insertion, Selection sorts with step tracing & in-place guarantees
- 📐 Algorithms: O(n²) comparison sorts, early-exit optimization, loop invariants
- ⏱️ Complexity:
  | Algorithm      | Best   | Avg    | Worst  | Space | Stable? | Notes                  |
  |----------------|--------|--------|--------|-------|---------|------------------------|
  | Bubble Sort    | O(n)   | O(n²)  | O(n²)  | O(1)  | ✅      | Early exit on `swapped`|
  | Insertion Sort | O(n)   | O(n²)  | O(n²)  | O(1)  | ✅      | Best for <50 elements  |
  | Selection Sort | O(n²)  | O(n²)  | O(n²)  | O(1)  | ❌      | Minimizes swaps only   |
- 🐛 Pitfall & Fix: Selection sort swaps non-adjacent elements → breaks stability. Documented tradeoff: use only when write operations are expensive. Insertion sort's `while j >= 0 and arr[j] > key` must use strict `>` to preserve equal-element order.
- 🔍 Book Reference: Hetland Ch. 4 (Loop Invariants, Comparison-Based Lower Bounds)
- 📈 Benchmark: Pending (will run `timeit` on n=10³, 10⁴ vs Python's Timsort)