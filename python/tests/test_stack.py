from stack_and_queue.node import Node
from stack_and_queue.stack import Stack
import pytest


#1-Can successfully push onto a stack
def test_push_0():
    stack=Stack()
    stack.push(1)
    actual=stack.top.value
    expected=1
    assert actual == expected
# 2-Can successfully push multiple values onto a stack
def test_push(stack):
    actual=stack.top.value
    expected="tomato"
    assert actual == expected

# 3-Can successfully pop off the stack
def test_pop(stack):
    actual= stack.pop()
    expected="tomato"
    assert actual == expected
    
# 4-Can successfully empty a stack after multiple pops

def test_pop_0():
    stack=Stack()
    stack.push(1)
    stack.push(4)
    stack.pop()
    stack.pop()
    actual= stack.top
    expected=None
    assert actual == expected
# 5-Can successfully peek the next item on the stack
def test_peek(stack):
    actual= stack.peek()
    expected="tomato"
    assert actual == expected
# 6-Can successfully instantiate an empty stack
def test_is_empty(stack):
    assert stack.is_empty() == True

@pytest.fixture
def stack():
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push("tomato")
    return stack