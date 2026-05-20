# src/structures/queue.py
from typing import Generic, TypeVar, Optional
from .linked_list import SinglyNode

T = TypeVar("T")

class ArrayQueue(Generic[T]):
    """Queue using Python list. O(1) enqueue, O(n) dequeue (shifts elements)."""
    def __init__(self) -> None:
        self._items: list[T] = []

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)  # O(n) - intentional for comparison

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"ArrayQueue({self._items})"

class LinkedQueue(Generic[T]):
    """Queue using singly linked list. O(1) enqueue & dequeue."""
    def __init__(self) -> None:
        self._head: Optional[SinglyNode[T]] = None
        self._tail: Optional[SinglyNode[T]] = None
        self._size: int = 0

    def enqueue(self, item: T) -> None:
        new_node = SinglyNode(item)
        if self._tail:
            self._tail.next = new_node
        else:
            self._head = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self) -> T:
        if not self._head:
            raise IndexError("dequeue from empty queue")
        data = self._head.data
        self._head = self._head.next
        if not self._head:
            self._tail = None  # Queue became empty
        self._size -= 1
        return data

    def peek(self) -> T:
        if not self._head:
            raise IndexError("peek from empty queue")
        return self._head.data

    def is_empty(self) -> bool:
        return self._size == 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        items = []
        curr = self._head
        while curr:
            items.append(curr.data)
            curr = curr.next
        return f"LinkedQueue({items})"