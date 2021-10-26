from linked_list_insertions.linked_list_insertions import *
import pytest


@pytest.fixture
def llt():
    linked_list = LinkedList()
    linked_list.insert(15)
    linked_list.insert(10)
    linked_list.insert(5)
    return linked_list

    
def test_linked_append(llt):
    llt.append(6)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{15}} ->  {{6}} -> NULL'


def test_linked_multiple_append(llt):
    llt.append(4)
    llt.append(7)
    llt.append(11)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{15}} ->  {{4}} ->  {{7}} ->  {{11}} -> NULL'



def test_linked_insert_before(llt):
    llt.insert_before(5,3)
    assert str(llt) == f' {{3}} ->  {{5}} ->  {{10}} ->  {{15}} -> NULL'


def test_linked_insert_before_first(llt):
    llt.insert_before(15,7)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{7}} ->  {{15}} -> NULL'



def test_linked_insert_after(llt):
    llt.insert_after(10,8)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{8}} ->  {{15}} -> NULL'



def test_linked_insert_after_last(llt):
    llt.insert_after(15,20)
    assert str(llt) == f' {{5}} ->  {{10}} ->  {{15}} ->  {{20}} -> NULL'


def test_linked_values(llt):
    assert str(llt) == f" {{5}} ->  {{10}} ->  {{15}} -> NULL"