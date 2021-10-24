from stack_and_queue.node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front==None:
            raise Exception ("The queue is empty")
        temp=self.front
        self.front = temp.next
        temp.next = None
        return temp.value


    def peek(self):
        if self.front == None:
            raise Exception ("The queue is empty")
        return self.front.value

    def is_empty(self):
        return not self.rear
        
