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
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value paris in a Node at that index.
        """
        value = 0
        for char in key:
          value += ord(char)
          index = (value*7)%self.__size
        return index

        # return sum([ord(char) for char in key]) * 7 % self.__size


    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value 
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()

        my_value = [key,value]
        self.__buckets[index].insert(my_value)

    def get(self, key):
      """
      Retrieve the most recent value of in oour hasmap for the given key

      :param key str
      :rvalue any
      """
      # calculate index
      index = self.__hash(key)
      # check if there is a non empty bucket at the index
      if self.__buckets[index]:
        # iterate over linked list
        linked_list = self.__buckets[index]
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
      index = self.__hash(key)
      if self.__buckets[index]:
        linked_list = self.__buckets[index]
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


#####################################CodeChallange32#######################################

# from trees.trees import Node,BinaryTrees

# class Node():
#   def __init__(self,value='',left=None,right=None):
#       self.value = value
#       self.left = left
#       self.right = right
#       self.next = None

#   def __str__(self):
#       return str(self.value)

# class BinaryTree():
#   def __init__(self, node=None):
#       self.root = node

#   def pre_order(self):
#     pre_order_output = []

#     def walk(root):
#       pre_order_output.append(root.value)
#       if (root.left): walk(root.left)
#       if (root.right): walk(root.right)

#     walk(self.root)
#     return pre_order_output





# def tree_intersection(tree1,tree2):
#   # tree1 = BinaryTree()
#   # tree2 = BinaryTree()
  
#   tree1_list = tree1.pre_order()
#   tree2_list = tree2.pre_order()
#   hash_table = HashTable()
#   result = []
  
#   for i in tree1_list:
#     hash_table.add(i,i)
  
#   for i in tree2_list:
#     if hash_table.contains(i):
#       result.append(i)

#   return result

# # tree1= [1,2,3,5,6]
# # tree2 = [1,2,5,7,6] 
# # print(tree_intersection(tree1,tree2))