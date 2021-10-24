# from stack_and_queue.node import Node
from stack_and_queue.queue import Queue


# Can successfully enqueue into a queue
def test_enqueue_0():
    queue=Queue()
    queue.enqueue("Hello")
    actual=queue.rear.value
    excepted="Hello"
    assert actual==excepted

# Can successfully enqueue multiple values into a queue
def test_enqueue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("potato")
    actual=queue.rear.value
    excepted="potato"
    assert actual==excepted

# Can successfully dequeue out of a queue the expected value
def test_dequeue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(10)
    actual= queue.dequeue()
    expected=1
    assert actual == expected

# Can successfully peek into a queue, seeing the expected value
def test_peek():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("potato")
    actual= queue.peek()
    expected=1
    assert actual == expected

# Can successfully empty a queue after multiple dequeues
def test_is_empty_1():
    queue=Queue()
    queue.enqueue("anything")
    queue.enqueue("nothing")
    queue.dequeue()
    queue.dequeue()
    actual = queue.front
    expected = None
    assert actual==expected


# Can successfully instantiate an empty queue
def test_is_empty():
    queue=Queue()
    assert queue.is_empty() == True

