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
        delnode = Node(data)                #value we want to delete
        current = self.head
        if (delnode.data == self.head.data):
            self.head = current.next
            delnode = None
            return
        if (delnode.data):
            while (current.data):
                 if current.data == delnode.data:
                     break
                 prev = current             # we created a new object prev so that we could manipulate the
                 current = current.next
        else:
            return (0)
        prev.next = current.next
        current = None



    def search(self,data):
        reqnode = Node(data)
        if (self.head):
            current = self.head
            count =0
            while (current.data):
                count=count+1
                if current.data == reqnode.data:
                    break
                print ("The node %d is at position %d of the list" %(reqnode.data, count))
                break
        else:
            print ("%d is not in this node" %(reqnode))

    def size(self):
        pass

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
obj.delete(5)
obj.search(2)
obj.printSLL()
