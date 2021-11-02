from trees.trees import Node ,BinaryTrees ,Binary_Search_Tree
import pytest

# Can successfully instantiate an empty tree
def test_binary_tree_0():
    tree = BinaryTrees()
    assert tree

# Can successfully instantiate a tree with a single root node
def test_binary_tree():
    tree = BinaryTrees()
    tree.root = Node('A')
    assert ['A'] == tree.binary_tree()


    
# Can successfully add a left child and right child to a single root node   
def test_binary_tree2():
    tree=BinaryTrees()

    node1 = Node('1')
    node2 = Node('2')
    node3 = Node('3')
    node4 = Node('4')
    node5 = Node('5')

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right=node5
    tree.root = node1

    expected = ['1','2','3','4','5']
    actual = tree.binary_tree()
    assert expected == actual

# Can successfully return a collection from a preorder traversal
def test_pre_order():
    tree=BinaryTrees()

    node1 = Node('1')
    node2 = Node('2')
    node3 = Node('3')
    node4 = Node('4')
    
    node1.left = node2
    node1.right = node3
    node2.left = node4

    tree.root = node1

    expected = ['1','2','4','3']
    actual = tree.pre_order()
    assert expected == actual

#   Can successfully return a collection from an inorder traversal
def test_in_order():
    tree=BinaryTrees()

    node1 = Node('1')
    node2 = Node('2')
    node3 = Node('3')
    node4 = Node('4')
    
    node1.left = node2
    node1.right = node3
    node2.left = node4

    tree.root = node1

    expected = ['4','2','1','3']
    actual = tree.in_order()
    assert expected == actual

#  Can successfully return a collection from a postorder traversal
def test_post_order():
    tree=BinaryTrees()

    node1 = Node('1')
    node2 = Node('2')
    node3 = Node('3')
    node4 = Node('4')
    
    node1.left = node2
    node1.right = node3
    node2.left = node4

    tree.root = node1

    expected = ['4','2','3','1']
    actual = tree.post_order()
    assert expected == actual



def test_to_the_root():
    tree = Binary_Search_Tree()
    tree.add('7')
    assert tree.root.data == '7'



def test_add_multiple():
    tree = Binary_Search_Tree()
    items = [15,7,2,5,20]
    for item in items:
        tree.add(item)

    actual = tree.root.data
    expected = 15
    assert actual == expected

    actual = tree.root.left.data
    expected = 7
    assert actual == expected

    actual = tree.root.left.left.data
    expected = 2
    assert actual == expected

    actual = tree.root.left.left.right.data
    expected = 5
    assert actual == expected

    actual = tree.root.right.data
    expected = 20
    assert actual == expected


def test_contains():
    tree = Binary_Search_Tree()
    
    items = [15,7,2,5,20]
    for item in items:
        tree.add(item)


    assert tree.contains(15) == True
    assert tree.contains(7) == True
    assert tree.contains(2) == True
    assert tree.contains(20) == True
    assert tree.contains(5) == True
    assert tree.contains(1) == False


################## code challange 16: tree-max ######################

def test_max_tree():
    tree=BinaryTrees()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right=node5
    tree.root = node1

    expected = tree.max_tree()
    actual = 5
    assert expected == actual


################## code challange 17: breadth_first ######################

def test_breadth_first():
    tree=BinaryTrees()

    node1 = Node('1')
    node2 = Node('2')
    node3 = Node('3')
    node4 = Node('4')
    node5 = Node('5')

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right=node5
    tree.root = node1

    expected = ['1','2','3','4','5']
    actual = tree.breadth_first()
    assert expected == actual