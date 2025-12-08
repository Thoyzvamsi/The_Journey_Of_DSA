# BST : Binary Search Tree where smaller element added to left side of the parent and
# Bigger elment is added to the right side of the parent

#Creating a Binary Search Tree
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def insert(root,value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)

    return root

#Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,end=" ")
        inorder(root.right)

#Preorder Traversal
def preorder(root):
    if root:
        print(root.value,end=" ")
        preorder(root.left)
        preorder(root.right)

#Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value,end=" ")

ls = list(map(int,input("Enter elements of the tree:").split()))
root = None

for i in ls:
    root = insert(root,i)

inorder(root)
print("")
preorder(root)
print("")
postorder(root)