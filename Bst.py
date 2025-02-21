import sys

class Node:
    def __init__(self, data = 0):
        self.left = None
        self.data = 0
        self.right = None
        print(f'Node with data {data} created')

class Bst:
    def __init__(self):
        self.root = None
        print('an empty Bst is created')

    def add_node(self):
        data = int(input('Enter data of the new node: '))
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        temp1 = self.root
        temp2 = None
        while temp1 is not None:
            temp2 = temp1
            if data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if data < temp2.data:
            temp2.left = node
        else:
            temp2.right = node

    
    def delete_node(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.delete_node(root.left, key)
        elif key > root.data:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)
        return root
    
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')            
            
    def search_node(self):
        if self.root is None:
            print('Tree is empty')
            return
        data = int(input('Enter data to be searched: '))
        temp = self.root
        level = 1
        while temp is not None:
            if temp.data == data:
                print(f'Node with data {data} found at level-{level}')
                return
            elif data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
            level += 1
        print(f'Node with data {data} not found')

class Menu:
    def invalid_choice(self):
        print('Invalid choice entered')
    
    def end_of_program(self):
        sys.exit('End of Program')

    def match_user_choice(self, choice, bst):
        match choice:
            case 1 :
                bst.add_node()
            case 2 : 
                if bst.root is None:
                    print('Tree is empty')
                else:
                    key = int(input('Enter data of the node to delete: '))
                    bst.root = bst.delete_node(bst.root, key)
            case 3 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.inorder(bst.root)
            case 4 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.preorder(bst.root)
            case 5 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.postorder(bst.root)
            case 6 :
                if bst.root is None:
                    print('Tree is empty')
                else:
                    bst.search_node()
            case 7 :
                self.end_of_program()
            case _ :
                self.invalid_choice()

    def run_menu(self):
        bst = Bst()
        while True:
            choice = int(input('\n1:Add 2:Delete 3:InOrder 4:PreOrder 5:PostOrder 6:Search 7:Exit.  Your choice: '))
            self.match_user_choice(choice, bst)

def start_app():
    menu = Menu()
    menu.run_menu()

start_app()