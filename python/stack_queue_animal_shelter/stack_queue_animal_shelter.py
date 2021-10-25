class Node:
   
    def __init__(self, value,next=None):
        self.value=value
        self.next=next


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


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
        self.counter = 0

    def enqueue(self, animal, type):
        if type == 'cat':
            self.counter += 1
            return self.cat.enqueue(animal)
        elif type == 'dog':
            self.counter += 1
            return self.dog.enqueue(animal)
        else:
            return 'This not cat or dog'

    def dequeue(self, pref):
        if pref == 'dog':
            return self.dog.dequeue()
        if pref == 'cat':
            return self.cat.dequeue()
        else:
            return 'This not cat or dog'

    def is_empty(self):
        if self.counter > 0:
            return False
        else:
            return True
