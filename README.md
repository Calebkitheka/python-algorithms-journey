# 🐍 Algo Playground

My Python algorithms learning journey, documented and tested.

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e ".[dev]."

# 📘 Algorithm Learning Journey

## Week 1: Foundations & Core Data Structures
### Day 2: Linked Lists Implementation
- 🎯 Goal: Build Singly & Doubly Linked Lists with O(1)/O(n) guarantees
- 📐 Algorithms: `insert_head`, `insert_tail`, `delete`, `search`, `__iter__.`
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

### Day 5: Advanced Sorting Algorithms
- 🎯 Goal: Implement Merge, Quick, Heap sorts; analyze divide & conquer & heap properties
- 📐 Algorithms: `merge_sort` (stable, O(n) space), `quick_sort` (Lomuto, in-place), `heap_sort` (max-heap, in-place)
- ⏱️ Complexity:
  | Algorithm      | Best   | Avg    | Worst  | Space | Stable? | Notes                  |
  |----------------|--------|--------|--------|-------|---------|------------------------|
  | Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)  | ✅      | Predictable, external merge friendly |
  | Quick Sort     | O(n log n) | O(n log n) | O(n²)  | O(log n)| ❌    | Cache-friendly, worst-case on sorted/pivot |
  | Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)  | ❌    | Guaranteed O(n log n), poor locality   |
- 🐛 Pitfall & Fix: QuickSort with Lomuto degrades to O(n²) on already-sorted arrays (pivot = last element). Fix: random pivot or median-of-three (deferred to Week 3). Heap sort's `_heapify` recursion can hit limits on huge arrays; iterative heapify is preferred for production. Merge sort's `<=` in the merge step preserves stability.
- 🔍 Book Reference: Hetland Ch. 5 (Divide & Conquer, Partitioning, Heapsort, Comparison Sort Lower Bounds)
- 📈 Benchmark: Pending (will compare all 6 sorts across 4 input patterns)

### Day 6: Benchmarking & CLI Polish
- 🎯 Goal: Build an automated benchmark runner, a CLI tool, and a visualization notebook
- 📐 Algorithms: Empirical runtime analysis across 4 input patterns (random, sorted, reverse, few-unique)
- ⏱️ Complexity vs Reality:
  | Observation                          | Theory vs Practice Insight                          |
  |--------------------------------------|-----------------------------------------------------|
  | Insertion sort beats Quick on n<100  | Low constant factors & cache locality outweigh O(n²)|
  | Quick sort degrades on sorted input  | Lomuto pivot = last element → worst-case O(n²)      |
  | Python's `sorted()` wins overall     | Timsort hybridizes Insertion + Merge + pattern detection|
  | Heap sort memory-efficient but slow  | Poor cache locality from random pointer jumps       |
- 🐛 Pitfall & Fix: In-place sorts mutate test data between repetitions. Fixed with `copy.deepcopy()` before each run. Also learned `time.perf_counter()` is more accurate than `time.time()` for microbenchmarks.
- 🔍 Book Reference: Hetland Ch. 5 (Empirical Analysis, Cache Effects, Python's Sorting Strategy)
- 📈 Benchmark: `benchmarks/sort_results.csv` generated, visualized in `notebooks/.`
