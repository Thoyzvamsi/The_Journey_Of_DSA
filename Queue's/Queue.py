#Queue works on the principle of LILO - last entered element will go out last

def enque(rear):
    if rear >= len(queue):
        print("Queue is Full")
        return rear
    else:
        n = int(input("Enter the Element:"))
        queue[rear] = n
        print(f"Enqueued : {n} in index {rear}")
        rear += 1
        return rear
def deque(front):
    if rear == front:
        print("Queue is empty")
        return front
    else:
        if rear == front:
            print("Queue is empty")
        else:
            front += 1
            print("Dequeued")
            return front

def display(front,rear):
    for i in range(front,rear):
        print(queue[i],end=" ")

front = 0
rear = 0 
y = int(input("Enter the size of the Queue: "))
queue = [0]*y

while(1):
    x = int(input("\nEnter the option 1(Enque), 2(Deque), 3(Display), 4(To End): "))
    if x == 1:
        rear = enque(rear)
    elif x == 2:
        front = deque(front)
    elif x == 3:
        display(front,rear)
    elif x == 4:
        print("Process ended......")
        break
 