class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None

def levelOrderTraversal(root : Node) :
    q = []
    if root is None :
        return
    q.append(root)
    while q :
        if q[0].left :
            q.append(q[0].left)
        if q[0].right :
            q.append(q[0].right)

        print(q[0].data,end= " ")
        del q[0]
    return

if __name__ == "__main__" :
    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)

    root = a
    root.left = b
    root.right = d
    d.left = c

    # expected order 10 20 40 30

    levelOrderTraversal(root)
