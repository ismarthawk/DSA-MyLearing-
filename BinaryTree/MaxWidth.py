class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None

def height(root) :
    if root is None : return 0
    lh = height(root.left)
    rh = height(root.right)

    return 1 + max(lh,rh)

def getWidth(root,level) :
    if root is None : return 0
    if level ==1 : return 1
    return getWidth(root.left,level-1) + getWidth(root.right,level-1)

def getMaxWidth(root) :
    res =  0
    if not root :
        return res
    for level in range(1,height(root)+1) :
        res = max(res,getWidth(root,level))
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
