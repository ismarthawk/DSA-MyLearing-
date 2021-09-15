class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None

def inorder(root) :
    s = []
    # stack
    iter = root
    while True :
        if iter :
            s.append(iter)
            iter = iter.left
        elif s :
            last = s[-1]
            print(s[-1].data , end = " ")
            if last.right : iter = last.right
            del s[-1]
        else :
            break


if __name__ == "__main__" :

    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)

    root = a
    root.left = b
    root.right = d
    d.left = c

    inorder(root)
