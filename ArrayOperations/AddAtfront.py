#Array operations -2 (adding at front, deleting at front and deleting at particular position)
#Ai usage : very low , error : mid

def AddinAtfront(n):
    global top
    if top == 9:
        print("Array is full")
    else:
        top += 1
        for i in range(top,-1,-1):
            if i == 0:
                lis[i] = n
                break
            else:
                lis[i] = lis[i-1]

def deleteAtFront():
    global top
    global front
    if top == -1:
        print("Array is empty")
    else:
        for i in range(top):
            lis[i] = lis[i+1]
        top -= 1

def display():
    for i in range(front,top+1):
        print(lis[i],end=" ")
    print()


m = int(input("Enter the size of : "))
lis = [0]*m
top = -1
front = 0

x = 0
while x != -1:
    print("For Adding(1),removing(2),display(3),ToEnd(-1):")
    x = int(input())
    match x:
        case 1:
            n = int(input("Enter the element:"))
            AddinAtfront(n)
        case 2:
            deleteAtFront()
        case 3:
            display()
        case -1:
            break
        case _:
            print("Invaild") 