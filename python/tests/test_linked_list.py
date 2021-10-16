from linked_list.linked_list import *
 
# test import
def test_import():
    assert LinkedList

# test create node
def test_node():
    node=Node("test")
    actual=node.data
    assert actual =="test"

# test string node in linked list
def test_string_linked_list():
    node = Node("x") 
    assert node.data == "x"

# test create node in linked list
def test_insert_linked_list():
    linked_l=LinkedList()
    linked_l.insert(3)
    new_node=linked_l.head
    assert new_node.data == 3
    
    # test create multiple nodes in linked list
def test_insert_multiple_linked_list():
    l_l=LinkedList()
    new_node= l_l.insert(3)
    new_node=l_l.insert(5)
    new_nod1=l_l.head
    # new_node0=l_l.
    # assert new_node.data == 5
    # assert new_node0. == 3