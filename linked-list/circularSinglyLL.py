class Node:  
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

class CircularLinkedList:
    def __init__(self, head = None):
        self.head = head 

    def insertAtEnd(self, value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != self.head):
                t1 = t1.next
            t1.next = temp
            temp.next = self.head  
        else:
            self.head = temp
            temp.next = self.head 

    def insertAtBeg(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
            temp.next = self.head
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            temp.next = self.head
            self.head = temp
            last.next = self.head 

    def insertAtMid(self, value, x):
        temp = Node(value)
        t1 = self.head
        while True: 
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
                break
            t1 = t1.next
            if t1 == self.head:  
                break

    def deleteLL(self, value):
        if self.head is None:
            return
        
        t1 = self.head
        prev = None
        
        if(t1.data == value):
            if t1.next == self.head: 
                self.head = None
                return
            else:
                last = self.head
                while last.next != self.head:
                    last = last.next
                self.head = t1.next
                last.next = self.head
                return
        
        while True:
            prev = t1
            t1 = t1.next
            if t1.data == value:
                prev.next = t1.next
                break
            if t1 == self.head: 
                break

    def printLL(self):
        if self.head is None:
            print("Empty list")
            return
        
        t1 = self.head
        while True:
            print(t1.data, end=" -> ")
            t1 = t1.next
            if t1 == self.head:
                break
        print("(back to head)")

obj = CircularLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtMid(25, 20)
obj.deleteLL(30)
obj.printLL()  