import pytest
from src.sorting.basic import bubble_sort, insertion_sort, selection_sort

@pytest.fixture(params=[bubble_sort, insertion_sort, selection_sort])
def sort_func(request):
    return request.param

def test_sort_empty(sort_func):
    arr = []
    sort_func(arr)
    assert arr == []

def test_sort_single(sort_func):
    arr = [42]
    sort_func(arr)
    assert arr == [42]

def test_sort_already_sorted(sort_func):
    arr = [1, 2, 3, 4, 5]
    sort_func(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_sort_reverse(sort_func):
    arr = [5, 4, 3, 2, 1]
    sort_func(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_sort_duplicates(sort_func):
    arr = [3, 1, 3, 2, 1, 4]
    sort_func(arr)
    assert arr == [1, 1, 2, 3, 3, 4]

def test_sort_negative_numbers(sort_func):
    arr = [0, -5, 10, -1, 3]
    sort_func(arr)
    assert arr == [-5, -1, 0, 3, 10]

def test_sort_inplace_modification(sort_func):
    arr = [9, 2, 7]
    original_id = id(arr)
    sort_func(arr)
    assert id(arr) == original_id  # Must mutate, not return new list
    assert arr == [2, 7, 9]