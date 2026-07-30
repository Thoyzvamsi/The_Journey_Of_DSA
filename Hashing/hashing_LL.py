#The main idea of hashing is to reduce the search time
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Hash_Table:
    def hashing(self,key):
        return key % 10
    
    def inserting(self,key,value,hash_table):
        index = self.hashing(key)
        
        new_Node = Node(key,value)
        curr = hash_table[index]
        if curr is None:
            hash_table[index] = new_Node
            return hash_table

        while curr.next:
            curr = curr.next

        curr.next = new_Node

        return hash_table
    
    def delete(self,key,hash_table):
        index = self.hashing(key)
        before_node = None

        if hash_table[index].key == key:
            hash_table[index] = hash_table[index].next
            return hash_table
        
        curr =  hash_table[index]
        before_node = curr

        while curr.next:
            curr = curr.next

            if curr.key == key:
                before_node.next = curr.next
                return hash_table
            else:
                before_node = curr

        if curr.key == key:
            before_node.next = None
            return hash_table
        
    def display(self,hash_table):
        for i in range(10):
            curr = hash_table[i]
            while curr:
                print(f"{curr.key} -> {curr.value}",end=" ")
                curr = curr.next
            print("\n")
            

hash_table = [None]*10

h = Hash_Table()
hash_table = h.inserting(100,283,hash_table)
hash_table = h.inserting(253,183,hash_table)
hash_table = h.inserting(302,83,hash_table)
hash_table = h.delete(302,hash_table)
hash_table = h.display(hash_table)