# from trees.trees import Node,BinaryTrees
from hashing.hash_table import HashTable

class Node():
  def __init__(self,value='',left=None,right=None):
      self.value = value
      self.left = left
      self.right = right
      self.next = None

  def __str__(self):
      return str(self.value)

class BinaryTree():
  def __init__(self, node=None):
      self.root = node

  def pre_order(self):
    pre_order_output = []

    def walk(root):
      pre_order_output.append(root.value)
      if (root.left): walk(root.left)
      if (root.right): walk(root.right)

    walk(self.root)
    return pre_order_output

def tree_intersection(tree1,tree2):
  # tree1 = BinaryTree()
  # tree2 = BinaryTree()
  
  tree1_list = tree1.pre_order()
  tree2_list = tree2.pre_order()
  hash_table = HashTable()
  result = []
  
  for i in tree1_list:
    hash_table.add(i,i)
  
  for i in tree2_list:
    if hash_table.contains(i):
      result.append(i)

  return result

# tree1= [1,2,3,5,6]
# tree2 = [1,2,5,7,6] 
# print(tree_intersection(tree1,tree2))