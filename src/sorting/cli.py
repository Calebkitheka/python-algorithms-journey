# src/sorting/cli.py
import argparse
import time
import random
import copy
from src.sorting import (bubble_sort, insertion_sort, selection_sort,
                         merge_sort, quick_sort, heap_sort)

SORTS = {
    "bubble": bubble_sort, "insertion": insertion_sort, "selection": selection_sort,
    "merge": merge_sort, "quick": quick_sort, "heap": heap_sort,
}

def main():
    parser = argparse.ArgumentParser(description="Algo Playground Sorting CLI")
    parser.add_argument("--sort", choices=SORTS.keys(), required=True, help="Algorithm to run")
    parser.add_argument("--size", type=int, default=1000, help="Input size")
    parser.add_argument("--pattern", choices=["random", "sorted", "reverse"], default="random", help="Input pattern")
    args = parser.parse_args()

    if args.pattern == "random":
        data = [random.randint(1, 10000) for _ in range(args.size)]
    elif args.pattern == "sorted":
        data = list(range(1, args.size + 1))
    else:
        data = list(range(args.size, 0, -1))

    arr = copy.deepcopy(data)
    start = time.perf_counter()
    SORTS[args.sort](arr)
    elapsed = (time.perf_counter() - start) * 1000

    print(f"✅ {args.sort} | {args.pattern} | n={args.size} | {elapsed:.3f}ms")

if __name__ == "__main__":
    main()