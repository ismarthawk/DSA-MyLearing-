def sort(li : list) :
    s = li

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

    def sortedInsert(i) :
        if isEmpty() or peek() <= i :
            push(i) 
        else :
            t = pop()
            sortedInsert(i)
            push(t)

    if not isEmpty() :
        t = pop()
        sort(s)
        sortedInsert(t)
    return s

print(sort([1,2,5,3,6]))