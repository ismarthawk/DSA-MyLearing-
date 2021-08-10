# Stacks can be implemented in two ways i. using arrays and ii. using linked lists
# But in python the arrays are typically lists
def createStack() :
    stack = []
    return stack

#  There are only three operations on a stack i. push ii. pop iii.peek

def isEmpty(stack) :
    return not (len(stack))
# 1. push
def push(stack,item) :
    stack.append(item)
    return
# 2. peek
def peek(stack) :
    if not isEmpty(stack) :
        return stack[-1]
    return "Stack is Empty"
# 3. pop

def pop(stack) :
    if not isEmpty(stack) :
        del stack[-1]
        return
    print('The stack is empty') 


if __name__ == "__main__" :
    #print('hello world')
    s = createStack()
    push(s,10)
    print(s)
    push(s,20)
    print(s)
    print(peek(s))
    pop(s)
    print(s)
    print(isEmpty(s))
    pop(s)
    print(isEmpty(s))
    