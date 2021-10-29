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


###### 
@pytest.mark.parametrize(
    "input,expected_value",
    [
        (-5, "Negative number not acceptable"),
        (10, "index not found"),
        (0, 15),
        (1, 10),
        (2, 5),
    ],
)
def test_kth_from_end(input, expected_value, llt):

    output = llt.kthFromEnd(input)
    assert output == expected_value

def test_kthFromEnd_of_empty_linkedList():
    empty_ll = LinkedList()
    assert empty_ll.kthFromEnd(1) == "empty List"

    ############
def test_link_list_zip_1(list_test_1, list_test_2):
        assert str(zipLists(list_test_1, list_test_2)) == ' {2} ->  {7} ->  {9} ->  {4} -> NULL'


def test_link_list_zip_3(list_test_5, list_test_6):
    assert str(zipLists(list_test_5, list_test_6)) == ' {2} ->  {5} ->  {3} ->  {6} ->  {4} ->  {1} ->  {9} -> NULL'


def test_link_list_zip_2(list_test_3, list_test_4):
    assert str(zipLists(list_test_3, list_test_4)) == ' {2} ->  {5} ->  {3} ->  {6} ->  {4} -> NULL'


@pytest.fixture
def list_test_1():
    linked_list1 = LinkedList()
    linked_list1.append(2)
    linked_list1.append(9)
    return linked_list1


@pytest.fixture
def list_test_2():
    linked_list2 = LinkedList()
    linked_list2.append(7)
    linked_list2.append(4)
    return linked_list2


@pytest.fixture
def list_test_3():
    linked_list3 = LinkedList()
    linked_list3.append(2)
    linked_list3.append(3)
    linked_list3.append(4)
    return linked_list3


@pytest.fixture
def list_test_4():
    linked_list4 = LinkedList()
    linked_list4.append(5)
    linked_list4.append(6)
    return linked_list4


@pytest.fixture
def list_test_5():
    linked_list5 = LinkedList()
    linked_list5.append(2)
    linked_list5.append(3)
    linked_list5.append(4)
    return linked_list5


@pytest.fixture
def list_test_6():
    linked_list6 = LinkedList()
    linked_list6.append(5)
    linked_list6.append(6)
    linked_list6.append(1)
    linked_list6.append(9)
    return linked_list6