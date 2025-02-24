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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

def converge_node(head1, head2):
    nodes_set = set()
    cur1 = head1
    cur2 = head2

    while cur1:
        nodes_set.add(cur1)
        cur1 = cur1.next

    while cur2:
        if cur2 in nodes_set:
            return cur2
        cur2 = cur2.next

    return None

l1 = Linled_list()
l1.append(10)
l1.append(20)
l1.append(30)

l2 = Linled_list()
l2.append(40)
l2.append(50)

com_node = Node(60)
l1.head.next.next.next = com_node
l2.head.next.next = com_node

l1.display()  
l2.display()


converge = converge_node(l1.head, l2.head)
if converge:
    print("\n Converge at node with data:", converge.data)  
else:
    print("No Converge found.")
