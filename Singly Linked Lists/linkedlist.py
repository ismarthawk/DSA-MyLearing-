class Node() :
    def __init__(self,data) :
        self.data = data
        self.next = None
class Llist() :
    def __init__(self) -> None:
        self.head = None
    # some basic operations on the linked list is coded.
    # Traversing the linked list
    def traverseList(self) :
        s = self.head 
        while s :
            print(s.data,end=" ")
            s = s.next
        print("")
    
    # Insertion can be done in 3 ways
    # 1. at start 
    # 2. in middle
    # 3. at last

    # insert at start
    def insert_at_start(self,data) :
        n = Node(data)
        n.next = self.head
        self.head = n
    
    # insert at middle
    def insert_after(self,k,data) :
        iter = self.head
        while iter :
            if iter.data == k :
                n = Node(data)
                n.next = iter.next
                iter.next = n
                return

    # insert at end
    def append(self,data) :
        n = Node(data)
        if self.head is None :
            self.head = n
            return 
        iter = self.head
        while iter.next is not None :
            iter = iter.next
        iter.next = n
    
    #
    #Deletion of a node 
    #to delete the first occourance of the given key
    #
    def delete(self,key) :
        # The element could deleted 1.first node
        #                           2.middle node(end node)
        if self.head :
            pre = None
            iter = self.head 
            while iter :
                if iter.data == key :
                    # This is first case
                    if pre is None :
                        self.head = iter.next
                        del iter
                        return 
                    pre.next = iter.next
                    del iter 
                    return
                pre = iter
                iter = iter.next
                
        print(f"No such {key} found")

    # delete a key by positon
    def delete_by_pos(self,pos) :
        if pos < 0 :
            print("Inappropriater position")
            return 
        c = 0
        iter = self.head
        pre = None
        if iter :
            while iter :
                if pos == c :
                    if pre is None : self.head = iter.next
                    else : pre.next = iter.next
                    del iter
                    return
                pre = iter 
                iter = iter.next
                c += 1
        print("Inappropriater position")

    

    

if __name__ == '__main__' :
    head = Llist()
    head.append(1)
    head.append(7)
    head.append(4)
    head.append(8)
    head.append(5)
    head.append(3)
    head.traverseList()


    # head.delete(10)
    # head.delete(1)
    # head.traverseList()
    # head.delete(4)
    # head.traverseList()
    # head.delete(3)
    # head.traverseList()


    # head.delete_by_pos(-1)
    # head.delete_by_pos(0)
    # head.traverseList()
    # head.delete_by_pos(3)
    # head.traverseList()
    # head.delete_by_pos(3)
    # head.traverseList()

    # print(head.length_iter())
    # print(head.length_recur())

    # head.swap_nodes(7,8)
    # head.traverseList()