class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


class BuildTree:
    def __init__(self,values):
        try:
            self.values = values
            self.it = iter(values)
        except Exception as e:
            print("Error is :",e)
    
    def PreOrderInput(self):  #this method is for preorder input like (1 2 3 -1 -1 4 5 -1 -1 -1 -1)
        try:
           val = next(self.it)
        except StopIteration:
            return None
        
        if val == -1:
            return None
        
        node = Node(val)
        node.left = self.PreOrderInput()
        node.right = self.PreOrderInput()

        return node
    
    def Preorder_Display(self,root):
        if root:
            print(root.data,end=" ")
            self.Preorder_Display(root.left)
            self.Preorder_Display(root.right)
            
