#Stack With Linked List
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,value):
        new_Node = Node(value)

        if self.head is None:
            self.head = new_Node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_Node

    def pop(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
    
    def Display(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.value,end=" -> ")
                temp = temp.next
            print("None")

stack = LinkedList()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
stack.Display()