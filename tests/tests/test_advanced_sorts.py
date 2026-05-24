import pytest
import random
from src.sorting.advanced import merge_sort, quick_sort, heap_sort

@pytest.fixture(params=[merge_sort, quick_sort, heap_sort])
def adv_sort_func(request):
    return request.param

def test_adv_sort_empty(adv_sort_func):
    arr = []
    adv_sort_func(arr)
    assert arr == []

def test_adv_sort_single(adv_sort_func):
    arr = [42]
    adv_sort_func(arr)
    assert arr == [42]

def test_adv_sort_already_sorted(adv_sort_func):
    arr = list(range(1, 6))
    adv_sort_func(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_adv_sort_reverse(adv_sort_func):
    arr = list(range(5, 0, -1))
    adv_sort_func(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_adv_sort_duplicates(adv_sort_func):
    arr = [3, 1, 3, 2, 1, 4]
    adv_sort_func(arr)
    assert arr == [1, 1, 2, 3, 3, 4]

def test_adv_sort_negative_numbers(adv_sort_func):
    arr = [0, -5, 10, -1, 3]
    adv_sort_func(arr)
    assert arr == [-5, -1, 0, 3, 10]

def test_adv_sort_inplace_modification(adv_sort_func):
    arr = [9, 2, 7]
    original_id = id(arr)
    adv_sort_func(arr)
    assert id(arr) == original_id
    assert arr == [2, 7, 9]

def test_adv_sort_large_random(adv_sort_func):
    random.seed(42)
    arr = [random.randint(-1000, 1000) for _ in range(500)]
    adv_sort_func(arr)
    assert arr == sorted(arr)