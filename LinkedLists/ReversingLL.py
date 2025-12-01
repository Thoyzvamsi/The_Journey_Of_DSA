#Reversing linked list personally my choice will a recursion in singly linkedlists
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

    def print_reverse(self, node):
        if node is None:
            return
        self.print_reverse(node.next)
        print(node.value, end=" -> ")


i = 0
ll = Linkedlist()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.print_reverse(ll.head)
