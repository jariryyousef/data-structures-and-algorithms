from hashing.hash_table import HashTable
from hashing.tree_intersection import tree_intersection ,BinaryTree , Node 
# from trees.trees import Node, BinaryTree
import pytest

@pytest.fixture
def hashtable():
	return HashTable()

def test_hash(hashtable):
	"""
	a ==> 97
	97* 7 ==> 679
	679 % 1024 ==> 679
	"""
	expected = 679
	actual = hashtable._hash("a")
	assert actual == expected

def test_hash_word(hashtable):
	"""
	y ==> 121
	o ==> 111
	u ==> 117 
	s ==> 115
	e ==> 101
	f ==> 102
	121 +111 +117 +115 + 101 +102 ==> 667
	667*7 ==> 5446
	4669 % 1024 ==> 573
	"""
	expected = 573
	actual =  hashtable._hash("yousef")
	assert actual == expected

def test_adding_a_key_and_value_to_hashtable():
  hash_table = HashTable()
  hash_table.add('yousef','25')
  assert hash_table.get('yousef') == '25'


def test_retrieving_based_on_a_key_returns_the_value_stored():
  hash_table = HashTable()
  hash_table.add('hello','2')
  assert hash_table.get('hello') == '2'


def test_returns_null_for_a_key_that_does_not_exist_in_the_hashtable():
  hash_table = HashTable()
  assert hash_table.get('test') == None

# Successfully retrieve a value from a bucket within the hashtable that has a collision
def test_handle_a_collision_within_the_hashtable():
    hash_table = HashTable()
    hash_table.add('yousef', 1)
    hash_table.add('jariry', 1)
    assert hash_table.get('jariry') == 1 and hash_table.get('yousef') ==1


#####################################CodeChallange31#######################################

def test_repeated_word():
	
	assert HashTable().repeated_word("Once upon a time, there was a brave princess who...") == 'a'

	assert HashTable().repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == 'it'
	
	assert HashTable().repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == 'summer'

	assert HashTable().repeated_word("yousef jariry, Jariry") == 'jariry'


	
#####################################CodeChallange32#######################################


def test_tree_intersection():

	node1 = Node('150')
	node2 = Node('100')
	node3 = Node('250')
	node4 = Node('75')
	node5 = Node('160')
	node6 = Node('200')
	node7 = Node('350')
	node8 = Node('125')
	node9 = Node('175')
	node10 = Node('300')
	node11 = Node('500')
	binary_tree1=BinaryTree()
	binary_tree1.root=node1
	node1.left = node2
	node1.right = node3
	node2.left = node4
	node2.right = node5
	node3.left = node6
	node3.right = node7
	node5.left = node8
	node5.right = node9
	node7.left = node10
	node7.right = node11

	node_one = Node('42')
	node_two = Node('100')
	node_three = Node('600')
	node_four = Node('15')
	node_five = Node('160')
	node_six = Node('200')
	node_seven = Node('350')
	node_eight = Node('125')
	node_nine = Node('175')
	node_ten = Node('4')
	node_eleven = Node('500')
	binary_tree2=BinaryTree()
	binary_tree2.root=node_one
	node_one.left = node_two
	node_one.right = node_three
	node_two.left = node_four
	node_two.right = node_five
	node_three.left = node_six
	node_three.right = node_seven
	node_five.left = node_eight
	node_five.right = node_nine
	node_seven.left = node_ten
	node_seven.right = node_eleven
	actual = tree_intersection(binary_tree1,binary_tree2)
	excepted = ['100', '160', '125', '175', '200', '350', '500']
	assert actual == excepted



def test_left_join():
    hash1 = HashTable()
    hash1.add('yousef','jariry')
    hash2 = HashTable()
    hash2.add('yousef','j')
    assert HashTable.left_join(hash1, hash2) == [['yousef', 'jariry', 'j']]
