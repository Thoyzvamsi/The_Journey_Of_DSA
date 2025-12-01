#Doubly linked lists :it is a chain of nodes , a contains value , the address of next node
# and the address of previous node

class Node:
    def __init__(self,value,next=None,pre=None):
        self.value = value
        self.next = next
        self.pre = pre

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        new_node.pre = curr
        curr.next = new_node

    def printLL(self):
        temp = self.head
        print("None <-> ",end="")
        while temp:
            print(temp.value,end=" <-> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.printLL()