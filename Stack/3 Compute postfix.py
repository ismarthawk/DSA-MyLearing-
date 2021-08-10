def computerPostfix(post : str) :
    s = []

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

    for i in post :
        try :
            i = int(i)
            push(i)
        except :
            b = pop()
            a = pop()
            if a and b :
                if i == "+" : push(a+b)
                if i == "-" : push(a-b)
                if i == "*" : push(a*b)
                if i == "/" : push(a/b)
    print(s[-1])

if __name__ == '__main__' :
    computerPostfix("231*+9-")


# if the numbers of multiple digits 
# use the str.split() and take inputs like this
#"2 3 10 * + 90 -"
