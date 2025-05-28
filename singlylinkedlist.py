"""from symtable import Class

class SinglyLinkedList:
    def __init__ (self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode

snode1=SinglyLinkedList("1")
snode2=SinglyLinkedList("2")
snode3=SinglyLinkedList("3")
snode4=SinglyLinkedList("4")

snode1.nextNode=snode2
snode2.nextNode=snode3
snode3.nextNode=snode4

currentNode=snode1
while True:
    print(currentNode.value, ">>>", end=' ')

    if currentNode.nextNode==None:
        print("None")
        break
    currentNode = currentNode.nextNode
  
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtBeginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtEnd(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node
    
    def deleteFromBeginning(self):
        if self.head is None:
            return "The Linked List Is Empty"
        self.head = self.head.next
    
    def deleteFromEnd(self):
        if self.head is None:
            return "List Is Empty"
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None



    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = ' ')
            temp = temp.next
            
        
        print()
        
if __name__ == '__main__':
   llist=LinkedList()
   llist.insertAtBeginning("fox")
   llist.insertAtBeginning("Brown")
   llist.insertAtBeginning("Quick")
   llist.insertAtBeginning("The")
   llist.printList()
   
   llist.insertAtEnd("jumps")
   llist.printList()

   llist.deleteFromBeginning()
   llist.printList()

   llist.deleteFromEnd()
   llist.printList()

   llist.insertAtBeginning("A")
   llist.printList()