class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None

def height(root) :
    if not root :
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh,rh)


def printaLevel(root,level) :
    if root is None :
        return
    if level == 1 :
        print(root.data,end = " ")
        return
    elif level > 1 :
        printaLevel(root.left,level-1)
        printaLevel(root.right,level-1)

def levelOrderTraversal(root) :
    h = height(root)
    for i in range(1,h+1) :
        printaLevel(root,i)
        print("")

if __name__ == "__main__" :
    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)

    root = a
    root.left = b
    root.right = d
    d.left = c

    print("Height is : ",height(root))
    for i in range(1,height(root)+1) :
        printaLevel(root,i)
        print("")

    levelOrderTraversal(root)
