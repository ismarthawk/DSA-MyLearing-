def reverse(li : list) :
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

    def insertAtBottom(i) :
        if isEmpty() :
            push(i)
            return
        t = pop()
        insertAtBottom(i)
        push(t)

    if not isEmpty() :
        t = pop()
        reverse(s)
        insertAtBottom(t)
    return s

if __name__ == '__main__' :
    # print('Hello ther')
    print(reverse(li=[1,2,3,4,5]))
    