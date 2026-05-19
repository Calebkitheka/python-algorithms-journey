import pytest
from src.structures.linked_list import SinglyLinkedList, DoublyLinkedList

@pytest.fixture
def empty_singly():
    return SinglyLinkedList()

@pytest.fixture
def filled_singly():
    lst = SinglyLinkedList()
    for x in [1, 2, 3]:
        lst.insert_tail(x)
    return lst

@pytest.fixture
def empty_doubly():
    return DoublyLinkedList()

@pytest.fixture
def filled_doubly():
    lst = DoublyLinkedList()
    for x in [1, 2, 3]:
        lst.insert_tail(x)
    return lst

# === SINGLY LINKED LIST TESTS ===
def test_singly_empty_init(empty_singly):
    assert empty_singly.is_empty()
    assert len(empty_singly) == 0

def test_singly_insert_head(empty_singly):
    empty_singly.insert_head(5)
    assert list(empty_singly) == [5]
    assert len(empty_singly) == 1

def test_singly_insert_tail(filled_singly):
    filled_singly.insert_tail(4)
    assert list(filled_singly) == [1, 2, 3, 4]

def test_singly_delete_head(filled_singly):
    filled_singly.delete(1)
    assert list(filled_singly) == [2, 3]

def test_singly_delete_tail(filled_singly):
    filled_singly.delete(3)
    assert list(filled_singly) == [1, 2]

def test_singly_delete_middle(filled_singly):
    filled_singly.delete(2)
    assert list(filled_singly) == [1, 3]

def test_singly_delete_not_found(empty_singly):
    with pytest.raises(ValueError):
        empty_singly.delete(99)

def test_singly_search(filled_singly):
    assert filled_singly.search(2) is True
    assert filled_singly.search(99) is False

def test_singly_duplicates():
    lst = SinglyLinkedList()
    for _ in range(3):
        lst.insert_tail(7)
    assert len(lst) == 3
    lst.delete(7)
    assert list(lst) == [7, 7]

# === DOUBLY LINKED LIST TESTS ===
def test_doubly_empty_init(empty_doubly):
    assert empty_doubly.is_empty()
    assert len(empty_doubly) == 0

def test_doubly_insert_head(empty_doubly):
    empty_doubly.insert_head(5)
    assert list(empty_doubly) == [5]
    assert empty_doubly._tail.data == 5

def test_doubly_insert_tail(filled_doubly):
    filled_doubly.insert_tail(4)
    assert list(filled_doubly) == [1, 2, 3, 4]

def test_doubly_delete_head(filled_doubly):
    filled_doubly.delete(1)
    assert list(filled_doubly) == [2, 3]
    assert filled_doubly._head.data == 2

def test_doubly_delete_tail(filled_doubly):
    filled_doubly.delete(3)
    assert list(filled_doubly) == [1, 2]
    assert filled_doubly._tail.data == 2

def test_doubly_delete_middle(filled_doubly):
    filled_doubly.delete(2)
    assert list(filled_doubly) == [1, 3]

def test_doubly_search_both_directions(filled_doubly):
    assert filled_doubly.search_forward(2) is True
    assert filled_doubly.search_backward(2) is True
    assert filled_doubly.search_forward(99) is False