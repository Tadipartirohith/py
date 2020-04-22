class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class SLL:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head =newNode

    def delete(self,data):
        delnode = Node(data)
        print (delnode.data)                #value we want to delete
        if (self.head):
            current = self.head
            while (current.data):
                 if current.data == delnode.data:
                     print (current.data)
                     break
                 prev = current             # we created a new object prev so that we could manipulate the 
                 print (current.data)
                 current = current.next
        else:
            return (0)
        print (prev.next.data)
        prev.next = current.next
        current = None

    def printSLL(self):
        current = self.head
        while (current):
            print (" %d" %(current.data))
            current = current.next

obj = SLL()
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.delete(3)
obj.printSLL()
