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

    def enqueue(self,value):
        self.stack1.push(value)


    def dequeue(self):
        if self.stack1 is None:
            raise Exception("queue is empty")
        while self.stack1 is not None :
            self.poped_data= self.stack1.pop()
            self.stack2.push(self.poped_data)
        
        self.de_q=self.stack2.pop()

        while self.stack2 is not None :
            self.poped_data= self.stack2.pop()
            self.stack1.push(self.poped_data)
            
        return self.de_q