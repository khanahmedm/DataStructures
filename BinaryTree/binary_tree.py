class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            queue = [self.root]
            

            while queue:
                current = queue.pop(0)
                if not current.left:
                    current.left = Node(data)
                    return
                else:
                    queue.append(current.left)
                
                if not current.right:
                    current.right = Node(data)
                    return
                else:
                    queue.append(current.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end = ' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end = ' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end = ' ')

    def levelorder(self):
        if not self.root:
            print('tree is empty.')
        else:
            queue = [self.root]
            
            while queue:
                current = queue.pop(0)
                print(current.data, end = ' ')

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

                
                

t = BinaryTree(1)
t.insert(2)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(6)
t.insert(7)
print('Inorder:')
t.inorder(t.root)
print()
print('Preorder:')
t.preorder(t.root)
print()
print('Postorder:')
t.postorder(t.root)
print()
print('Levelorder:')
t.levelorder()