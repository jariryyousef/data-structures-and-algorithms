from trees.trees import Node ,BinaryTrees

def test_binary_tree():
    tree = BinaryTrees()

    node_1 = Node('A')
    node_2 = Node('B')
    node_3 = Node('C')
    node_4 = Node('D')

    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4

    tree.root = node_1

    expected = ['A','B','C','D']
    actual = tree.binary_tree()
    assert expected == actual

