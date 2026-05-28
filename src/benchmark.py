# scripts/benchmark.py
import time
import random
import csv
import copy
from pathlib import Path
from src.sorting import (bubble_sort, insertion_sort, selection_sort,
                         merge_sort, quick_sort, heap_sort)

PATTERNS = {
    "random": lambda n: [random.randint(1, 10000) for _ in range(n)],
    "sorted": lambda n: list(range(1, n + 1)),
    "reverse": lambda n: list(range(n, 0, -1)),
    "few_unique": lambda n: [random.choice([1, 2, 3]) for _ in range(n)],
}

SORTS = {
    "bubble": bubble_sort, "insertion": insertion_sort, "selection": selection_sort,
    "merge": merge_sort, "quick": quick_sort, "heap": heap_sort,
}

def run_benchmark(sizes=(100, 500, 1000, 2000), repeats=3):
    Path("benchmarks").mkdir(exist_ok=True)
    output_file = "benchmarks/sort_results.csv"
    print(f"🚀 Running benchmarks. Results saved to {output_file}\n")

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["size", "pattern", "algorithm", "time_ms"])

        for size in sizes:
            for pat_name, gen_func in PATTERNS.items():
                base_data = gen_func(size)
                for algo_name, sort_func in SORTS.items():
                    times = []
                    for _ in range(repeats):
                        arr = copy.deepcopy(base_data)
                        start = time.perf_counter()
                        sort_func(arr)
                        end = time.perf_counter()
                        times.append((end - start) * 1000)
                    avg_ms = sum(times) / len(times)
                    writer.writerow([size, pat_name, algo_name, f"{avg_ms:.3f}"])
                    print(f"✅ {algo_name:12} | {pat_name:10} | n={size:5} | {avg_ms:.3f}ms")
    print("\n📊 Benchmark complete!")