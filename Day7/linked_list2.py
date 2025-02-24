class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linled_list:
    def __init__(self):
        self.head= None

    def append(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new   
        