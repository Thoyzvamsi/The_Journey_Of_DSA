#There are three Insert , delete and search
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

def search(root,key):
    if root.value == key:
        print(f"Value : {key} Found")
        return root
    if key < root.value:
        search(root.left,key)
    else:
        search(root.right,key)

def minvalue(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root,key):
    if root is None:
        return root
    if key < root.value:
        root.left = delete(root.left,key)
    elif key > root.value:
        root.right = delete(root.right,key)
    else:
        if root.right is None:
            return root.left
        elif root.left is None:
            return root.right
        
        temp = minvalue(root.right)
        root.value = temp.value
        root.right = delete(root.right,temp.value)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value,end=" ")
        inorder(root.right)


root = None

root = insert(root,3)
root = insert(root,4)
root = insert(root,5)
root = insert(root,6)
root = insert(root,1)
root = insert(root,2)
search(root,4)
inorder(root)
root = delete(root,2)
print("")
inorder(root)