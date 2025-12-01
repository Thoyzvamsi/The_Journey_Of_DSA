#Array operations basic level adding at back and deleting at back 
#Ai usage : high,  errors:very high

lis = [0]*10
top = -1

def insertionAtEnd(n):
    global top
    if top == 9:
        print("list is Full")
    else:
        top += 1
        lis[top] = n

def DeleteAtEnd():
    global top
    if top == -1:
        print("List is empty")
    else:
        top-=1

def display():
    global top
    if top == -1:
        print("List is empty")
    else:
        for i in range(top+1):
            print(lis[i],end=" ")

insertionAtEnd(1)
insertionAtEnd(2)
insertionAtEnd(3)
insertionAtEnd(4)
DeleteAtEnd()
display()
