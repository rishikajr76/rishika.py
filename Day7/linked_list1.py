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

    def add_at_position(self, data, pos):
        new = Node(data)
        if pos == 0:
            new.next = self.head
            self.head = new
            return
        current = self.head
        for _ in range(pos - 1):
            if current is None:
                print("Position is out of range.")
                return
            current = current.next
        new.next = current.next
        current.next = new

    def del_at_position(self, pos):
        if self.head is None:
            print("Position is out of range.")
        if pos == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(pos - 1):
            if current is None or current.next is None:
                print("Position is out of range.")
            current = current.next
        current.next = current.next.next   


    def reverse_display(self, node):
        if node:
            self.reverse_display(node.next)
            print(node.data, end="  ")

l1 = Linled_list()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(50)
l1.add_at_position(40, 1)
l1.add_at_position(60, 3)
l1.del_at_position(2) 
print("Reverse linked list:")
l1.reverse_display(l1.head)
