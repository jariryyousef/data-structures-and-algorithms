import pytest
from stack_and_queue_pseudo.stack_and_queue_pseudo import *

def test_enqueue_Expected_failure(queue_values):
    actual = queue_values.__str__()
    expected = '( 9 ) -> ( r ) -> ( -4 )'
    assert actual != expected

def test_enqueue_edge_case():
    queue = Pseudo_queue()
    actual = queue.enqueue()
    expected = 'no value'
    assert actual == expected


def test_dequeue_Expected_failure(queue_values):
    dequeue_value = queue_values.dequeue()
    actual = queue_values.__str__()
    expected = '( 1 ) -> ( r ) -> ( -2 ) -> ( 3 )'
    assert actual != expected
    assert dequeue_value != -2

def test_dequeue_edge_case():
    queue = Pseudo_queue()
    actual = queue.dequeue()
    expected = 'The Queue is empty'
    assert actual == expected


@pytest.fixture
def queue_values():
    queue = Pseudo_queue()
    queue.enqueue(3)
    queue.enqueue(-2)
    queue.enqueue("r")
    queue.enqueue(1)
    return queue