# src/structures/linked_list.py
from typing import Any, Iterator, Optional, Generic, TypeVar

T = TypeVar("T")

class SinglyNode(Generic[T]):
    """Node for singly linked list."""
    def __init__(self, data: T, next_node: Optional["SinglyNode[T]"] = None):
        self.data = data
        self.next = next_node

class SinglyLinkedList(Generic[T]):
    """Singly linked list with O(1) head operations and O(n) tail/search/delete."""
    def __init__(self) -> None:
        self._head: Optional[SinglyNode[T]] = None
        self._size: int = 0

    def insert_head(self, data: T) -> None:
        new_node = SinglyNode(data, self._head)
        self._head = new_node
        self._size += 1

    def insert_tail(self, data: T) -> None:
        new_node = SinglyNode(data)
        if not self._head:
            self._head = new_node
        else:
            curr = self._head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self._size += 1

    def delete(self, data: T) -> None:
        if not self._head:
            raise ValueError(f"{data} not found in empty list")
        if self._head.data == data:
            self._head = self._head.next
        else:
            prev, curr = self._head, self._head.next
            while curr and curr.data != data:
                prev, curr = curr, curr.next
            if not curr:
                raise ValueError(f"{data} not found in list")
            prev.next = curr.next
        self._size -= 1

    def search(self, data: T) -> bool:
        curr = self._head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def __iter__(self) -> Iterator[T]:
        curr = self._head
        while curr:
            yield curr.data
            curr = curr.next

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def __repr__(self) -> str:
        return f"SinglyLinkedList({list(self)})"


class DoublyNode(Generic[T]):
    """Node for doubly linked list."""
    def __init__(self, data: T, next_node: Optional["DoublyNode[T]"] = None,
                 prev_node: Optional["DoublyNode[T]"] = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList(Generic[T]):
    """Doubly linked list with O(1) head/tail operations and bidirectional traversal."""
    def __init__(self) -> None:
        self._head: Optional[DoublyNode[T]] = None
        self._tail: Optional[DoublyNode[T]] = None
        self._size: int = 0

    def insert_head(self, data: T) -> None:
        new_node = DoublyNode(data, self._head, None)
        if self._head:
            self._head.prev = new_node
        else:
            self._tail = new_node
        self._head = new_node
        self._size += 1

    def insert_tail(self, data: T) -> None:
        new_node = DoublyNode(data, None, self._tail)
        if self._tail:
            self._tail.next = new_node
        else:
            self._head = new_node
        self._tail = new_node
        self._size += 1

    def delete(self, data: T) -> None:
        curr = self._head
        while curr and curr.data != data:
            curr = curr.next
        if not curr:
            raise ValueError(f"{data} not found in list")
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self._head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        else:
            self._tail = curr.prev
        self._size -= 1

    def search(self, data: T) -> bool:
        return self.search_forward(data) or self.search_backward(data)

    def search_forward(self, data: T) -> bool:
        curr = self._head
        while curr:
            if curr.data == data:
                return True
            curr = curr.next
        return False

    def search_backward(self, data: T) -> bool:
        curr = self._tail
        while curr:
            if curr.data == data:
                return True
            curr = curr.prev
        return False

    def __iter__(self) -> Iterator[T]:
        curr = self._head
        while curr:
            yield curr.data
            curr = curr.next

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def __repr__(self) -> str:
        return f"DoublyLinkedList({list(self)})"