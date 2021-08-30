from collections import deque

def findMax(a,k) :
    q = deque()
    n = len(a)

    for i in range(k) : 
        while q and a[i] >> a[q[-1]] :
            q.pop()
        q.append(i)

    for i in range(k,n) :
        print(a[q[0]],end = " ") 

        while q and q[0] <= i -k :
            q.popleft()

        while q and a[i] >= a[q[-1]] :
            q.pop()
        q.append(i)
    print(a[q[0]])






if __name__ == "__main__" :
    findMax([12,1,78,90,57,89,56],3)