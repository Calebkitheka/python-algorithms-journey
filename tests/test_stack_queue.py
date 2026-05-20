import pytest
from src.structures.stack import ArrayStack, LinkedStack
from src.structures.queue import ArrayQueue, LinkedQueue

# === STACK FIXTURES ===
@pytest.fixture
def empty_array_stack(): return ArrayStack()
@pytest.fixture
def empty_linked_stack(): return LinkedStack()

# === QUEUE FIXTURES ===
@pytest.fixture
def empty_array_queue(): return ArrayQueue()
@pytest.fixture
def empty_linked_queue(): return LinkedQueue()

# === STACK TESTS ===
@pytest.mark.parametrize("stack_cls", [ArrayStack, LinkedStack])
def test_stack_empty_init(stack_cls):
    s = stack_cls()
    assert s.is_empty()
    assert len(s) == 0
    with pytest.raises(IndexError): s.pop()
    with pytest.raises(IndexError): s.peek()

@pytest.mark.parametrize("stack_cls", [ArrayStack, LinkedStack])
def test_stack_push_pop(stack_cls):
    s = stack_cls()
    s.push(10)
    s.push(20)
    assert len(s) == 2
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty()

@pytest.mark.parametrize("stack_cls", [ArrayStack, LinkedStack])
def test_stack_peek(stack_cls):
    s = stack_cls()
    s.push(5)
    assert s.peek() == 5
    assert len(s) == 1

# === QUEUE TESTS ===
@pytest.mark.parametrize("queue_cls", [ArrayQueue, LinkedQueue])
def test_queue_empty_init(queue_cls):
    q = queue_cls()
    assert q.is_empty()
    assert len(q) == 0
    with pytest.raises(IndexError): q.dequeue()
    with pytest.raises(IndexError): q.peek()

@pytest.mark.parametrize("queue_cls", [ArrayQueue, LinkedQueue])
def test_queue_enqueue_dequeue(queue_cls):
    q = queue_cls()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    assert len(q) == 3
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    assert q.dequeue() == "c"
    assert q.is_empty()

@pytest.mark.parametrize("queue_cls", [ArrayQueue, LinkedQueue])
def test_queue_peek(queue_cls):
    q = queue_cls()
    q.enqueue(42)
    assert q.peek() == 42
    assert len(q) == 1

def test_queue_single_element_dequeue_resets_tail():
    q = LinkedQueue()
    q.enqueue(1)
    assert q.dequeue() == 1
    assert q._head is None
    assert q._tail is None