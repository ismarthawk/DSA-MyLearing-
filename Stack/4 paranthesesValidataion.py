def isValid(exp: str) -> bool :
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

    for i in exp :
        if i in '([{' :
            push(i)
            continue
        if i == '}' :
            if pop() != '{' :
                return False
        if i == ']' :
            if pop() != '[' :
                return False
        if i == ')':
            if pop() != '(':
                return False
    return isEmpty()

if __name__ == '__main__' :
    print(isValid("{()}[][)"))
