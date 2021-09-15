class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = self.next = None


def connect(root) :
    if root is None :
        return
    q = [root]

    while q :
        l = len(q)
        while l :
            l -= 1
            last = q[0]
            if last.left : q.append(last.left)
            if last.right : q.append(last.right)
            del q[0]
        for ind,n in enumerate(q) :
            if ind == len(q) - 1 :
                break
            n.next = q[ind+1]


if __name__ == "__main__" :
    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)

    root = a
    root.left = b
    root.right = d
    d.left = c

    connect(root)
    print(b.next.data)
