from queue import Queue
def genereate(n) :
    arr = Queue()
    arr.put("1")
    while n :
        n -= 1
        s1 = arr.get()
        print(s1)
        s2 = s1
        arr.put(s1+"0")
        arr.put(s2+"1")

if __name__ == "__main__" :
    genereate(10)