#insert_before, insert_after, insert_last, insert_beg

class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=None
        self.next=None

class Dll:
    def __init__(self):
        self.first=None
        self.last = None
    def insert_before(self,ref_node, data):
        newnode = Node(data)
        ref_node = Node(ref_node)
        if ref_node.prev is None:
            self.first = newnode
        else:
            newnode.prev = ref_node.prev
            print (ref_node.prev.next)
            ref_node.prev.next = newnode
        ref_node.prev = newnode

    def insert_after(self,ref_node, data):
        newnode = Node(data)
        ref_node = Node(ref_node)
        if ref_node.next is None:
            self.last = newnode
        else:
            newnode.next = ref_node.next
            newnode.next.prev=newnode
        ref_node.next = newnode

    def insert_beg(self, data):
        newnode = Node(data)
        if self.first is None:
            self.first = newnode.data
            self.last = newnode.data
        else:
            self.insert_before(self.first, newnode.data)


    def printdll(self):
        current = self.first
        while current:
            print (current.data)
            current = current.next

a = Dll()
a.insert_beg(1)
a.insert_before(1,2)
a.insert_after(2,3)
a.printdll()
