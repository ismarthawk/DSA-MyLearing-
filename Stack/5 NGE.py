def FindNextGreaterElement(li : list) -> dict :
    s = []
    d = dict()

    def push(i):
        s.append(i)

    def isEmpty():
        return not len(s)

    def peek():
        if not isEmpty():
            return s[-1]
        return None

    def pop():
        a = peek()
        if a:
            del s[-1]
            return a
        return None
    next = 0
    while next < len(li) :
        if isEmpty() :
            push(li[next])
        elif peek() >= li[next] :
            push(li[next])
        else :
            while peek() and peek() < li[next] :
                d[pop()] = li[next]
            push(li[next])
        next += 1
    while not isEmpty() :
        d[pop()] = -1
    return d
        

                
if __name__ == '__main__' :
    # print('Hello there')
    print(FindNextGreaterElement([13,6,7,12]))
    print(FindNextGreaterElement([4,5,2,25]))
