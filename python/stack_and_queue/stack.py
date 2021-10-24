from stack_and_queue.node import Node
class Stack:
    def __init__(self):
        self.top=None

    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        if self.top==None:
            raise Exception ("The stack is empty")
        temp=self.top
        self.top=self.top.next
        self.next=None
        return temp.value
    
    
    def peek(self):
        if self.top==None:
            raise Exception ("The stack is empty")
        return self.top.value

    def is_empty(self):
        if self.top==None:
            return False
        else:
            return True


