# create class for create node
class Node:
    """
   class for create a node
    """
    def __init__(self,data,next_=None):
        self.data=data
        self.next=next_
        
    
# linkedlist class 
class LinkedList:
    """
   create linked list
    """

    def __init__(self):
        # its empty linked list
        self.head=None
    
    def insert(self,value):    
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            data=self.head
            self.head=new_node
            self.head.next=data
        # # self.head = Node(value, self.head)
    #     new_node = Node(value)
         
    #    # 3. Make next of new Node as head
    #     new_node.next = self.head
         
    #     # 4. Move the head to point to new Node
    #     self.head = new_node
