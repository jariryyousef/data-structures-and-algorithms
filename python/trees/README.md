# Trees
+ Binary Search Tree is a node-based binary tree data structure which has the following properties:  
1- The left subtree of a node contains only nodes with keys lesser than the node’s key.  
2- The right subtree of a node contains only nodes with keys greater than the node’s key.  
3- The left and right subtree each must also be a binary search tree.  
## Challenge
+ Node  
1- Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

+ Binary Tree  
+ Create a Binary Tree class  
Define a method for each of the depth first traversals:  
pre order    
in order
post order 

+ Binary Search Tree  
1- Add method  
Arguments: value  
Adds a new node with that value in the correct location in the binary search tree.  
2- Contains
Argument: value  
Returns: boolean indicating whether or not the value is in the tree at least once.  

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
pre order : O(n)    
in order : O(n)  
post order : O(n)  

add : O(logN)  
contains : O(logN)
