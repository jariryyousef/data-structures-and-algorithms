"""
The implementation of Node class, Linked list class, and Hashmap class. 
"""
import re

class Node:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initalization of Hash table
        
        """
        self._size = size
        self.buckets = [None] * size

    def _hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value paris in a Node at that index.
        """
        value = 0
        for char in key:
          value += ord(char)
          index = (value*7)%self._size
        return index



    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value 
        Return : No return value
        """

        index = self._hash(key)

        if not self.buckets[index]:
          self.buckets[index] = LinkedList()

        my_value = [key,value]
        self.buckets[index].insert(my_value)

    def get(self, key):
      """
      Retrieve the most recent value of in oour hasmap for the given key

      :param key str
      :rvalue any
      """
      # calculate index
      index = self._hash(key)
      # check if there is a non empty bucket at the index
      if self.buckets[index]:
        # iterate over linked list
        linked_list = self.buckets[index]
        current = linked_list.head
        while current:
          # check if the key in each node matches
          if current.value[0] == key: 
            # return the value of the node with the mathcing key
            return current.value[1]
          current = current.next
        
      # return None
      return None
    def contains(self,key):
      """
      check if the key exists in the table already.
      Arguments: key
      Returns: Boolean
      """
      index = self._hash(key)
      if self.buckets[index]:
        linked_list = self.buckets[index]
        current = linked_list.head

        while current:
          # check if the key in each node matches
          if current.value[0] == key:
            return True
          current = current.next

      return False
  
#####################################CodeChallange31#######################################
    def repeated_word(self,string):
      """
      finds the first word to occur more than once in a string
      Arguments: string
      Return: string
      """
      
      hash_table = HashTable()
      string = re.sub('[^A-z ]+', '', string).split(" ")
      for i in string:
        i = i.lower()
        if i and hash_table.contains(i):return i
        hash_table.add(i,i)


#####################################CodeChallange33#######################################

    def left_join(hash1, hash2):

        arr = []
        for i in hash1.buckets:
            if i:
                if hash2.contains(i.head.value[0]):
                    right_item = hash2.get(i.head.value[0])
                    arr.append([i.head.value[0], i.head.value[1],right_item])
                else:
                    arr.append([i.head.value[0], i.head.value[1],'Null'])
        return arr