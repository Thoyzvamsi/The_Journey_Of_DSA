#Singly linked lists : It has a chain of nodes , A node contains value and address of Next Node

class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
    
    def insertAtfront(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = None
            return
        new_node.next = self.head
        self.head = new_node
    
    def insertAtPosition(self,pos,value):
        new_node = Node(value)
        i = 1
        curr = self.head
        while i != pos:
             curr = curr.next
             i+=1
        new_node.next = curr.next
        curr.next = new_node


    def DeleteAtEnd(self):
        curr = self.head
        if curr is None:
            print("Linked list empty.")
            return
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None

    def DeleteAtFront(self):
        if self.head is None:
            print("Linked list empty.")
            return
        else:
            self.head = self.head.next
        

    def PrintList(self):
        if self.head is None:
            print("List is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.value,end=" -> ")
                temp = temp.next
            print("None")

ll = Linkedlist()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtfront(4)
ll.insertAtfront(5)
ll.DeleteAtEnd()
ll.insertAtPosition(2,0)
ll.DeleteAtFront()
ll.insertAtPosition(3,3)

ll.PrintList()
