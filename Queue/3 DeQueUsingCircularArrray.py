class CircularDeQue :
    def __init__(self,n) -> None:
        self.n = n
        self.arr = [0] * n
        self.front = self.rare = -1

    def isEmpty(self) :
        return self.front == -1

    def isFull(self) :
        return (self.front+1) % self.n == self.rare

    def insertFront(self,i) :
        if self.isEmpty() :
            self.front = self.rare = 0
            self.arr[0] = i
            return 

        if self.isFull() :
            print('Overflow')
            return
        
        self.front += 1
        self.front = self.front % self.n
        self.arr[self.front] =i
    
    def insertRare(self,i) :
        if self.isEmpty() :
            self.front = self.rare = 0
            self.arr[0] = i
            return
        if self.isFull() :
            print('Overflow')
            return 
        
        self.rare -= 1
        if self.rare == -1 :
            self.rare = self.n - 1
        self.arr[self.rare] = i

    def print(self) :
        if self.isEmpty() :
            print('None')
            return
        end = self.rare
        start = self.front
        while True :
            print(self.arr[end],end=" ")
            if end == start : 
                print('')
                return
            end = (end+1) % self.n

    def deleteFront(self) :
        if self.isEmpty() :
            print('underFlow')
            return
        if self.front == self.rare :
            self.front = self.rare = -1
            return
        self.front -= 1
        if self.front == - 1 :
            self.front = self.n - 1
    
    def deleteRare(self) :
        if self.isEmpty() :
            print('underFlow')
            return
        if self.front == self.rare:
            self.front = self.rare = -1
            return
        self.rare  = (self.rare + 1) % self.n

    def getFront(self) :
        if self.isEmpty() :
            return None
        return self.arr[self.front]
    
    def getRare(self) :
        if self.isEmpty() :
            return None
        return self.arr[self.rare]




if __name__ == '__main__' :
    que = CircularDeQue(5)
    # print(que.isFull())
    # print(que.isEmpty())
    print(que.insertFront(10))
    print(que.insertRare(20))
    que.print()
    que.insertFront(30)
    que.print()
    que.insertRare(40)
    que.print()
    que.insertFront(50)
    que.print()
    print(que.isFull())
    que.insertFront(30)
    que.deleteFront()
    que.print()
    que.deleteRare()
    que.print()
    print(que.getFront())
    

    

    



    
    
