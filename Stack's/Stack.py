#Stack : Stack works on the principle of LIFO - last entered will go out last

def push(n,top,stack):
    if len(stack) < top:
        print("Stack overflow.")
        return top
    else:
        top += 1
        stack[top] = n
        return top

def pop(top):
    if len(stack) == -1:
        print("Stack is underflow.")
        return top
    else:
        top-=1
        return top
    
def peek(top):
    if len(stack) == -1:
        print("Stack is underflow.")
        return top
    else:
        print("Top Element:",stack[top])

def display(top):
    print("Stack :")
    for i in range(top+1):
        print(stack[i])

m = int(input("Enter the size of the stack:"))
top = -1 
stack = [0]*m

while(1):
    y = int(input("Enter 1(push),2(pop),3(peek),4(display),5(To End):"))
    if y == 5:
        break
    else:
        match(y):
            case 1:
                n = int(input("Enter the Number to Push:"))
                top = push(n,top,stack)
                print(f"Pushed {n} to index {top}")
            case 2:
                top = pop(top)
                print(f"Popped {stack[top+1]}")
            case 3:
                peek(top)
            case 4:
                display(top)
