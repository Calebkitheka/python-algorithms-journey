# src/structures/stack.py
from typing import Generic, TypeVar, Optional
from .linked_list import SinglyNode

T = TypeVar("T")

class ArrayStack(Generic[T]):
    """Stack using Python list (dynamic array). O(1) amortized push/pop."""
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"ArrayStack({self._items})"

class LinkedStack(Generic[T]):
    """Stack using singly linked list. O(1) push/pop."""
    def __init__(self) -> None:
        self._top: Optional[SinglyNode[T]] = None
        self._size: int = 0

    def push(self, item: T) -> None:
        new_node = SinglyNode(item, self._top)
        self._top = new_node
        self._size += 1

    def pop(self) -> T:
        if not self._top:
            raise IndexError("pop from empty stack")
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data

    def peek(self) -> T:
        if not self._top:
            raise IndexError("peek from empty stack")
        return self._top.data

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        items = []
        curr = self._top
        while curr:
            items.append(curr.data)
            curr = curr.next
        return f"LinkedStack({items})"