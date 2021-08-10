class Node() :
    def __init__(self,data) -> None:
        self.data = data
        self.next =  None

class Llist() :
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):
        n = Node(data)
        if self.head is None:
            self.head = n
            return
        iter = self.head
        while iter.next is not None:
            iter = iter.next
        iter.next = n
    
    def traverse(self) :
        if self.head :
            iter = self.head
            while iter :
                print(iter.data,end=" ")
                iter = iter.next
        print("")

    #1. Find length of the linked list
    # can be done both in i. iterative method ii.recursive method
    def length_iter(self) :
        # this is iterative method
        res = 0
        iter = self.head
        while iter :
            res += 1
            iter = iter.next
        return res
    
    def counter(self,node : Node) :
        if node :
            return 1 + self.counter(node.next)
        return 0
    def length_recur(self) :
        return self.counter(self.head)


    # 2. Swappping the nodes of the linked list without using the data swapp
    # in them.
    
    def swap_nodes(self,x, y) :
        if x ==  y : return 
        iterx = self.head
        itery = self.head
        prex = prey = None

        while iterx :
            if iterx.data == x :
                break
            prex = iterx
            iterx = iterx.next
        while itery :
            if itery.data == y :
                break
            prey = itery
            itery = itery.next
        
        if iterx is None or itery is None : 
            print('no two elements')
            return 

        if prex is None : self.head = itery
        else : prex.next = itery
        if prey is None : self.head = iterx
        else : prey.next = iterx

        t = iterx.next
        iterx.next = itery.next
        itery.next = t

    # 3. Reverse the linked list
    def reverse(self) :
        pre = None
        iter = self.head
        while iter :
            next = iter.next
            iter.next = pre
            pre = iter
            iter = next
        self.head = pre

    
       
            

#3 . Merging two sorted linked lists
def sorted_merge(l1 : Node,l2 : Node) :
    if l1 is None : return l2
    if l2 is None : return l1
    if l1.data <= l2.data : 
        res = l1
        l1 = l1.next
    else : 
        res = l2
        l2= l2.next
    res.next = None
    k = res
    while l1 and l2 :
        if l1.data <= l2.data :
            k.next = l1
            l1 = l1.next
        else :
            k.next = l2
            l2 = l2.next
        k= k.next
        k.next = None
    if l1 : k.next = l1
    else : k.next = l2
    return res



# 4. MergeSort for the linked lists

def mergeSort(head : Node ) : 
    if head is None or head.next is None :
        return head
    def getMiddle(head) :
        if head is None :
            return head
        slow = head 
        fast = head
        while fast.next and fast.next.next :
            slow = slow.next
            fast = fast.next.next
        return slow
    mid = getMiddle(head)
    midp1 = mid.next
    mid.next = None
    left = mergeSort(head)
    right = mergeSort(midp1)
    return sorted_merge(left,right)  

# 5.reverse the linked list in groups
def reverse_in_groups(head : Node , k )  -> Node :
    if head is None :
        return head
    pre = next = None
    iter = head
    c = 0
    while iter is not None and c < k :
        next = iter.next
        iter.next = pre
        pre = iter
        iter = next
        c += 1
    head.next = reverse_in_groups(next,k)
    return pre  

# 6.Floyd's Loop detection
def islooped(head : Node) -> bool :
    slow = fast = head
    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            return True
    return False


# 7. Remove loop
def remove_loop(head : Node,loop_node : Node) :
    iter = head
    while True :
        iter2 = loop_node
        while iter2.next != iter and iter2.next != loop_node :
            iter2 = iter2.next
            if iter2.next == iter :
                iter2.next = None
                return head
            iter = iter.next

# 8. Add two numbers represted by linked lists

def add_lists(l1 : Llist , l2 : Llist) -> Llist :
    res = Llist()
    if l1.head is None :
        res = l2.head
        return res
    if l2.head is None :
        res = l1.head
        return res    
    n1 = 0
    n2 = 0
    iter = l1.head
    while iter  :
        n1 = n1 * 10 + iter.data
        iter = iter.next
    iter = l2.head
    while iter :
        n2 = n2 * 10 + iter.data
        iter = iter.next
    
    adds = n1 + n2
    while adds > 0 :
        rem = adds % 10
        adds //= 10
        res.append(rem)
    return res.reverse()

        
def find_and_remove_loop(head : Node) :
    slow = fast = head
    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            return remove_loop(head,slow)
    return head
    
#9. Rotate the linked list clock wise
def rotate(head,k) :
    # The idea is to blend the linked list into a circular linked list
    #traverse by k nodes and removing the back link.
    if head is None :
        return head
    iter = head
    while iter.next :
        iter = iter.next
    iter.next = head
    pre = None
    for i in range(k) :
        pre = head
        head = head.next
    pre.next = None
    return head



if __name__ == '__main__' :
    l = Llist()
    l.append(3)
    l.append(2)
    l.append(5)
    l.append(4)
    l.append(1)
    l.append(8)
    l.append(9)

    l.traverse()
    # print(l.length_iter())
    # print(l.length_recur())

    # l.swap_nodes(3,5)
    # l.traverse()


    # l.reverse()
    # l.traverse()

    # l1 = Llist()
    # l1.append(3)
    # l1.append(5)
    # l1.append(6)
    # l1.append(7)
    # l1.append(9)

    # l2 = Llist()
    # l2.append(2)
    # l2.append(4)
    # l2.append(6)
    # l2.append(8)
    # l2.append(10)
    
    # l1.traverse()
    # l2.traverse()

    # res = Llist()
    # res.head = sorted_merge(l1.head,l2.head)
    # res.traverse()

    # res = Llist()
    # res.head = mergeSort(l.head)
    # res.traverse()

    res = Llist()
    res.head = reverse_in_groups(l.head,4)
    res.traverse()
    

    
    
    

