"""
This Module defines Node , Binary Tree and Binary Search Tree
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)


class BinaryTrees:
  def __init__(self):
      self.root = None

  def binary_tree(self):
      queue = Queue()
      queue.enqueue(self.root)

      item = []
      while queue.peek():
          front = queue.dequeue()
          item += [front.data]

          if front.left is not None:
              queue.enqueue(front.left)

          if front.right is not None:
              queue.enqueue(front.right)

      return item

  def pre_order(self):
      list_of_items = []

      def walk(node):
          if node:
              list_of_items.append(node.data)
              walk(node.left)
              walk(node.right)

      walk(self.root)
      return list_of_items

  def in_order(self):

      list_of_items = []

      def walk(node):
          if node:
              walk(node.left)
              list_of_items.append(node.data)
              walk(node.right)

      walk(self.root)
      return list_of_items

  def post_order(self):

      list_item = []

      def walk(node):
          if node:
              walk(node.left)
              walk(node.right)
              list_item.append(node.data)

      walk(self.root)
      return list_item

################## code challange 16: tree-max ######################
  def max_tree(self):
    node_tree = self.post_order()
    maximum = self.root.data
    for i in node_tree:
      if i > maximum :
        maximum = i

    return maximum
 ################## code challange 17: breadth_first ######################

  def breadth_first(self):
      queue = Queue()
      queue.enqueue(self.root)

      item = []
      while queue.peek():
          front = queue.dequeue()
          item += [front.data]
  
          if front.left:
              queue.enqueue(front.left)

          if front.right:
              queue.enqueue(front.right)

      return item

class Binary_Search_Tree(BinaryTrees):
  """
  This class have toe method:
  1- Add node to the tree
  2- Searching for node in tree
  """
  def __init__(self):
      self.root = None


  def add(self,data):

    """
  
    add node to the tree

    """

    # node = Node

    # if the tree dont have any node 
    if not self.root:
      self.root = Node(data)
    # if the tree have nodes , walk into the node
    else:
      def walk(root):
        if data <= root.data:
          if root.left :
            walk(root.left)
          else:
            root.left = Node(data)
        elif data >= root.data:
          if root.right:
            walk(root.right)
          else : root.right = Node(data)
        # walk(self.root)
      return walk(self.root)

    
  def contains(self, data):
    """
    searching for node in tree
    """
    if self.root == None:
        return False

    def walk(root):
        if root:
          if data == root.data:
            return True

          elif root.data != data:

            if walk(root.left): 
              return True 
            
            if walk(root.right): 
              return True

          return False
    return walk(self.root)

