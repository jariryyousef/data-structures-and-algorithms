class Node:
   
    def __init__(self, value,next=None):
        self.value=value
        self.next=next

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

class Pseudo_queue:
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,value=None):
        if value == None:
            return 'no value'
        self.stack1.push(value)

    def dequeue(self):
        
        if not self.stack1.top:
            return 'The Queue is empty'
           
        while self.stack1.top:
            
       
            self.stack2.push(self.stack1.pop())

        dequeue_value = self.stack2.pop()

        while self.stack2.top:
        
    
            self.stack1.push(self.stack2.pop())

        return dequeue_value

