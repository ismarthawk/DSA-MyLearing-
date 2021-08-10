
# Declaring the structure of node.
class Node() :
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
# Declaring the structure of the Circular linked list

class CircularLinkedList() :
    def __init__(self) -> None:
        self.tail = None
    
    #Insertions can be done in 4 ways
    #1. At end
    #2. At last
    #3. to empty list
    #4. after an element k.


    # insertion to empty list
    def addToEmpty(self,data) :
        if self.tail :
            return 
        self.tail = Node(data)
        self.tail.next = self.tail
    
    # insertion at beginning
    def insertBegin(self,data) :
        if self.tail is None :
            return self.addToEmpty(data)
        n = Node(data)
        n.next = self.tail.next
        self.tail.next = n

    # insertion at end

    def insertEnd(self,data) :
        self.insertBegin(data)
        self.tail = self.tail.next

    # insertion after an element

    def insertAfter(self,data,k) :
        if self.tail is None :
            print('Empty list')
            return 
        if self.tail.data == k :
            return self.insertBegin(data)
        iter = self.tail.next
        while iter != self.tail :
            if iter.data == k :
                n = Node(data)
                n.next = iter.next
                iter.next = n
                return 
            iter = iter.next
        if iter == self.tail :
            print(f'No such {k} exists')
    
    # 2. Traversal
    
    def traverse(self) :
        if self.tail is None :
            print("")
            return 
        head = self.tail.next
        while head != self.tail :
            print(head.data,end = " ")
            head = head.next
        print(self.tail.data)


    # 3. Make the circular linked lists to two halves
    def makeintoTwo(self) :
        res1 = CircularLinkedList()  
        res2 = CircularLinkedList()
        fast  = slow = self.tail.next
        if self.tail is None :
            return (res1,res2)
        fast = slow = self.tail.next
        while fast.next != self.tail.next and fast.next.next != self.tail.next :
            fast = fast.next.next
            slow = slow.next

        slow = slow.next
        while fast.next != slow :
            fast = fast.next
        fast.next = self.tail.next
        self.tail.next = slow
        res1.tail = fast
        res2.tail = self.tail
        return (res1,res2)

    # 3. Sorted insertion
    def sortedInsert(self,data) :
        if self.tail is None :
            return self.addToEmpty(data)
        if self.tail.data <= data :
            return self.insertEnd(data)
        pre = self.tail
        iter = self.tail.next
        while iter.data < data :
            pre = iter
            iter = iter.next
        n = Node(data)
        pre.next = n
        n.next = iter
        

        






if __name__ == '__main__' :
    # print("Hello there")
    # cslist = CircularLinkedList()
    # cslist.traverse()
    # cslist.addToEmpty(10)
    # cslist.traverse()
    # cslist.insertBegin(20)
    # cslist.traverse()
    # cslist.insertBegin(100)
    # cslist.traverse()
    # cslist.insertAfter(100,2)
    # cslist.insertAfter(2,100)
    # cslist.traverse()
    
    
    # cs1, cs2 = cslist.makeintoTwo()
    # cs1.traverse()
    # cs2.traverse()
    
    cllist = CircularLinkedList()
    cllist.sortedInsert(1)
    cllist.insertEnd(10)
    cllist.insertEnd(20)
    cllist.insertEnd(30)
    cllist.insertEnd(40)
    cllist.insertEnd(50)
    cllist.insertEnd(60)
    cllist.traverse()

    cllist.sortedInsert(10)
    cllist.sortedInsert(70)
    cllist.traverse()