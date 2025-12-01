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


    def insertAtFront(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.head.pre = new_node
            new_node.next = self.head
            self.head = new_node


    def length_list(self):
        temp = self.head
        i = 0
        while temp:
            i+=1
            temp = temp.next
        return i


    def insertAtpostion(self,pos,value):
        new_node = Node(value)
        x=ll.length_list()
        if pos == 0:
            ll.insertAtFront(value)
        elif pos == x:
            ll.insertAtEnd(value)
        else:
            for i in range(pos):
                if i == 0:
                    temp = self.head
                else:
                    temp = temp.next
            new_node.next = temp.next
            new_node.pre = temp
            temp.next.pre = new_node
            temp.next = new_node


    def print(self):
        temp = self.head
        print("None <-> ",end="")
        while temp:
            print(temp.value,end=" <-> ")
            temp = temp.next
        print("None")


    def deleteAtfront(self):
        if self.head is None:
            print("List is empty.")
            return
        else:
            self.head = self.head.next


    def deleteAtEnd(self):
        if self.head is None:
            print("List is empty.")
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.pre.next = None

ll = LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.insertAtEnd(5)
ll.insertAtFront(0)
ll.insertAtpostion(0,10)
ll.deleteAtfront()
ll.deleteAtEnd()
ll.print()