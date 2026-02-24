class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None 

    def insertAtEnd(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
            
        t = self.head
        while t.next != None:
            t = t.next
        t.next = temp
        temp.prev = t

    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp 

    def insertAtMid(self, value, x):
        temp = Node(value)
        t = self.head
        while t != None and t.data != x:
            t = t.next
        
        if t == None:
            print(f"Value {x} not found")
            return
            
        temp.next = t.next
        temp.prev = t
        if t.next != None:
            t.next.prev = temp
        t.next = temp

    def deleteDLL(self, value):
        if self.head == None:
            print("Linked list is empty")
            return
            
        t = self.head
        
        if t.data == value:
            self.head = t.next
            if self.head != None:
                self.head.prev = None
            return
            
        while t != None:
            if t.data == value:
                if t.prev != None:
                    t.prev.next = t.next
                if t.next != None:
                    t.next.prev = t.prev
                return
            t = t.next
            
        print(f"Value {value} not found")

    def printDLL(self):
        if self.head == None:
            print("Empty list")
            return
            
        t1 = self.head
        while t1.next != None:
            print(t1.data, end=" <---> ")
            t1 = t1.next
        print(t1.data)

obj = DoublyLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtBeg(5)
obj.insertAtMid(25, 20)
obj.deleteDLL(40)
obj.printDLL()