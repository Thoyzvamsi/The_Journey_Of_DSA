from PreOrder_Input import BuildTree

values = list(map(int ,input().split()))
x = BuildTree(values)
root = x.PreOrderInput()
print(x.Preorder_Display(root))

