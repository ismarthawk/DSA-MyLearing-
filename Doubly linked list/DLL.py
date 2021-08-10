# Doubly linked list node declaration



class Node :
    def __init__(self,data) -> None:
        self.data = data
        self.pre = self.next = None
    
class DLL :
    def __init__(self) -> None:
        self.head = None

    # 1. Insertion 
    # insertion can be done in 4 ways 
    # i.at beginning 
    # ii.at end
    # iii.after a given node
    # iv. before a given node

    def insertBegin(self,data) :
        if self.head is None :
            self.head = Node(data)
            return 
        n = Node(data)
        n.next = self.head
        self.head.pre =n
        self.head = n
    
    def insertEnd(self,data) :
        if self.head is None :
            self.head = Node(data)
            return 
        iter = self.head
        while iter.next is not None :
            iter = iter.next
        n = Node(data)
        iter.next = n
        n.pre = iter
    
    def insertAfter(self,k,data) :
        if self.head :
            iter = self.head 
            while iter is not None :
                if iter.data == k :
                    n = Node(data)
                    n.next = iter.next
                    n.pre = iter
                    if iter.next :
                        iter.next.pre = n
                    iter.next = n
                    return 
                iter = iter.next
    
    def insertBefore(self,k,data) :
        if self.head :
            iter = self.head
            while iter is not None :
                if iter.data == k :
                    n = Node(data)
                    n.next = iter
                    n.pre = iter.pre
                    if n.pre :
                        n.pre.next = n
                    else :
                        self.head = n
                    return
                iter = iter.next
    
    # 2. Traverse

    def traverse(self) :
        if self.head :
            iter= self.head
            while iter is not None :
                print(iter.data,end = " ")
                iter = iter.next
        print("")

    # 3. Delete a given node 
    def delete(self,data) :
        if self.head :
            iter = self.head
            while iter :
                if iter.data == data :
                    p = iter.pre
                    n = iter.next
                    #1.middle element
                    if p and n :
                        p.next = n
                        n.pre = p
                        del iter
                    #2. first element
                    elif not p and n :
                        n.pre = None
                        self.head = n
                        del iter
                    elif p and not n :
                        p.next = None
                        del iter
                    else :
                        self.head = None
                        del iter
                    return 
                    
                iter = iter.next
        print('No such element found')

    # 4. Reverse the linked list.
    def reverse(self) :
        if self.head is None :
            return
        while self.head.next :
            self.head.pre , self.head.next = self.head.next,self.head.pre
            self.head = self.head.pre
        self.head.pre, self.head.next = self.head.next, self.head.pre
        
    # 5. Quick sort for doubly linked list
    def QuickSort(self) :
        def lastNode() :
            if self.head is None:
                return None
            iter = self.head
            while iter.next :
                iter = iter.next
            return iter
        
        def partition(l : Node ,h : Node) -> Node :
            x = h.data
            i = l.pre
            j = l
            while j != h :
                if j.data <= x :
                    if i == None :
                        i = l
                    else :
                        i = i.next
                    i.data,j.data = j.data,i.data
                j = j.next
            if i is None :
                i = l
            else :
                i = i.next
            i.data,h.data = h.data,i.data
            return i

        def quickSort(l : Node ,h : Node) -> None :
            if l is not None and h is not None and l != h and l != h.next:
                t = partition(l,h)
                quickSort(l,t.pre)
                quickSort(t.next,h)

        h = lastNode()
        return quickSort(self.head,h)


            
        



if __name__ == '__main__' :
    print('Hello')

    li = DLL()
    li.insertBegin(10)
    #li.traverse()
    li.insertEnd(20)
    #li.traverse()
    li.insertBefore(10,30)
    #li.traverse()
    li.insertAfter(30,40)
    li.traverse()

    # li.delete(30)
    # li.traverse()

    li.reverse()
    li.traverse()

    li.QuickSort()
    li.traverse()

