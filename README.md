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
