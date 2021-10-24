from linked_list_temp import __version__


def test_version():
    assert __version__ == '0.1.0'

# from linked_list.linked_list import Node ,LinkedList
from linked_list_temp.linked_list_temp import Node, LinkedList
# test import
def test_import():
    assert LinkedList

# test create node
def test_node():
    node=Node("test")
    actual=node.value
    assert actual =="test"

# test string node in linked list
def test_string_linked_list():
    node = Node("x") 
    assert node.value == "x"

# test create node in linked list
def test_insert_linked_list():
    linked_l=LinkedList()
    linked_l.insert(3)
    new_node=linked_l.head
    assert new_node.value == 3
    
# The head property will properly point to the first node in the linked list
def test_head():
    new_node=Node(5)
    linked_l = LinkedList()
    linked_l.head=new_node
    assert linked_l.head == new_node
# test create multiple nodes in linked list

def test_insert_multiple_nodes():
    new_node=Node(1)
    linked_l = LinkedList()
    linked_l.head=new_node
    linked_l.insert(2)
    assert linked_l.head.value == 2
    linked_l.insert(3)
    assert linked_l.head.value == 3
    linked_l.insert(4)
    assert linked_l.head.value == 4

# Will return true when finding a value within the linked list that exists

def test_include_linked_list_true():
    linked_l=LinkedList()
    linked_l.insert(20)
    excepted=True
    actual=linked_l.include(20)
    assert excepted==actual

# Will return false when searching for a value in the linked list that does not exist
def test_include_linked_list_false():
    linked_l=LinkedList()
    linked_l.insert(20)
    excepted=False
    actual=linked_l.include(2)
    assert excepted==actual

def test_to_string():
    linked_l = LinkedList()
    new_node= linked_l.insert("orange")
    new_node= linked_l.insert("potato")
    new_node= linked_l.insert("tomato")

    assert linked_l.t0_string() == "{ tomato } -> { potato } -> { orange } -> NULL"