from hashing.hash_table import HashTable
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
	actual = hashtable._HashTable__hash("a")
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
	actual =  hashtable._HashTable__hash("yousef")
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