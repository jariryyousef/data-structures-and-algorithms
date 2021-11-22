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


#####################################CodeChallange31#######################################

def test_repeated_word():
	
	assert HashTable().repeated_word("Once upon a time, there was a brave princess who...") == 'a'

	assert HashTable().repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == 'it'
	
	assert HashTable().repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == 'summer'

	assert HashTable().repeated_word("yousef jariry, Jariry") == 'jariry'