# create class for create node
class Node:
    def __init__(self,value,next_=None):
        self.value=value
        self.next=next_
        
    
# linkedlist class 
class LinkedList:

    def __init__(self):
        # its empty linked list
        self.head=None
    """
    Arguments: value
    Returns: nothing
    Adds a new node with that value to the head of the list with an O(1) Time performance.
    """
    def insert(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
    
    """
    Arguments: value
    Returns: Boolean
    Indicates whether that value exists as a Node’s value somewhere within the list.
    
    """
    def include(self,value):
        if self.head == None:
            return False
        else:
            temp=self.head
            while temp is not None:
                if temp.value==value:
                    return True
                temp=temp.next
            return False


    """
    Arguments: none
    Returns: a string representing all the values in the Linked List, formatted as:
    "{ a } -> { b } -> { c } -> NULL"

    """
    def t0_string(self):
        temp =self.head
        r =''
        while temp is not None:
            r += "{ " + str(temp.value)+ " } -> "
            temp = temp.next
        r += 'NULL'
        return r