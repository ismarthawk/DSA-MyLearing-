class Queue : 
    def __init__(self) -> None:
        self.que = list()

    # The ADT operations on a que are 
    # i.enqueue ii.dequeue iii.front iv.rear v.isempty

    def enque(self,i) :
        self.que.append(i)
    
    def isEmpty(self) :
        return not len(self.que)

    def front(self) :
        if not self.isEmpty() :
            return self.que[-1]
        return None

    def rare(self) :
        if not self.isEmpty() :
            return self.que[0]
        return None

    def deque(self) :
        try : 
            k = self.fron()
            del self.que[-1]
            return k
        except : 
            return None
    
    def traverse(self) :
        print(self.que)




    
    
