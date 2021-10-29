class Node:
    def __init__(self, value=""):
        self.value = value
        self.next = None

    def __add__(self, other):
        return Node(self.value + other.value)

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def includes(self, value):
        is_last = False
        current = self.head
        print(current)
        while not is_last:
            if str(current) == str(value):
                return True

            if current.next == None:
                is_last = True
            current = current.next
        return False




    def insert(self, value):
        node = Node(value)

        if self.head:
            node.next = self.head
        self.head = node



    def append(self, value):
        node = Node(value)
        if self.head==None:
            self.head=node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node



    def insert_before(self,value,new_value):
        node = Node(new_value)
        current_node=self.head
        if current_node.value==value:
             node.next = self.head
             self.head = node
        else:
            while current_node.next:
                if current_node.next.value==value:
                    node.next=current_node.next
                    current_node.next=node
                    break
                current_node=current_node.next





    def insert_after(self,value,new_value):
        node = Node(new_value)
        current_node=self.head
        while current_node:
            if current_node.value==value:
                temp=current_node.next
                current_node.next=node
                node.next=temp
                break
            current_node=current_node.next





    def __str__(self) -> str:
        string = ""
        current = self.head

        while current:
            string += f" {'{'}{str(current.value)}{'}'} -> "
            current = current.next
        string += "NULL"
        return string
