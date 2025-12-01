def EnqueAtEnd(rear):
    if rear >= len(queue):
        print("End is Full")
        return rear
    else:
        n = int(input("Enter the Element:"))
        queue[rear] = n
        print(f"Enqueued At End : {n} in index {rear}")
        rear += 1
        return rear
    
def EnqueAtFront(front):
    if front == 0:
        print("Front is Full")
        return front
    else:
        n = int(input("Enter the Element:"))
        queue[front-1] = n
        print(f"Enqueued At Front : {n} in index {front-1}")
        front -= 1
        return front

def DequeAtFront(front):
    if rear == front:
        print("Queue is empty")
        return front
    else:
        front += 1
        print("Dequeued")
        return front

def DequeAtEnd(rear):
    if rear == front:
        print("Queue is empty")
        return rear
    else:
        rear -= 1
        print("Dequeued")
        return rear

def display(front,rear):
    if rear == front:
        print("Queue is empty")
    else:
        for i in range(front,rear):
            print(queue[i],end=" ")

front = 0
rear = 0 
y = int(input("Enter the size of the Queue: "))
queue = [0]*y

while(1):
    x = int(input("\nEnter the option 1(EnqueAtEnd), 2(EnqueAtFront), 3(DequeAtFront), 4(DequeAtEnd), 5(Display), 6(To End): "))
    if x == 1:
        rear = EnqueAtEnd(rear)
    elif x == 2:
        front = EnqueAtFront(front)
    elif x == 3:
        front = DequeAtFront(front)
    elif x == 4:
        rear = DequeAtEnd(rear)        
    elif x == 5:
        display(front,rear)
    elif x == 6:
        print("Process ended......")
        break