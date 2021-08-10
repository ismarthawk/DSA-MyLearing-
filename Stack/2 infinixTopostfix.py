

def converter(infix : str) :

    s = []
    op = ""
    prior = {
        '+' : 1,
        '-' : 1,
        '*' : 2,
        '/' : 2,
        '^' : 3
    }

    def push(i) :
        s.append(i)
    def isEmpty() :
        return not len(s)
    def peek() :
        if not isEmpty() :
            return s[-1]
        return None
    def pop() :
        a = peek()
        if a :
            del s[-1]
            return a
        return None

    for i in infix :
        if i.isalpha() :
            op += i
            continue
        if i == "(" :
            push(i)
            continue
        if i == ")" :
            while peek() != "(" :
                op += pop()
            pop()
            continue
        curr = prior[i]
        while not isEmpty() :
            if peek() == "(" :
                break
            if prior[peek()] >= curr :
                op += pop()
            else : break
        push(i)
    op += "".join(s[::-1])
    print(op)
                





if __name__ == '__main__' :
    print('hello world')
    infix = input()
    converter(infix)