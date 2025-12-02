#Circular Linked lists: where the last element is connected to the first element
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def insertAtRear(self,value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        self.rear.next = self.head

    def insertAtfront(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        new_node.next = self.head
        self.head = new_node

    #writing only delete at Front because both logics are same
    def deleteAtfront(self):
        self.head = self.head.next
        self.rear.next = self.head

    def printing(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while (1):
            print(temp.value,end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print(f"Points back to {self.head.value}")

ll = LinkedList()
ll.insertAtRear(1)
ll.insertAtRear(2)
ll.insertAtRear(3)
ll.insertAtfront(0)
ll.printing()
ll.deleteAtfront()
ll.printing()