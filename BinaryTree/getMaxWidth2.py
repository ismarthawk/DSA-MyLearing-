class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None

def getMaxWidth(root) :
    if not root :
        return 0
    res = 0
    q = []
    q.append(root)

    while q :
        l = len(q)
        res = max(res,l)
        while l != 0 :
            l -= 1
            curr = q[0]
            if curr.left : q.append(curr.left)
            if curr.right : q.append(curr.right)
            del q[0]
    return res


if __name__ == "__main__" :

    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)

    root = a
    root.left = b
    root.right = d
    d.left = c

    print(getMaxWidth(root))
