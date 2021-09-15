class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None

def findDiameter(root) :
    if root is None :
        return 0
    return max(height(root.left)+height(root.right)+1,findDiameter(root.left),findDiameter(root.right))



def height(root) :
    if not root :
        return 0
    lt = height(root.left)
    rt = height(root.right)
    return 1 + max(lt,rt)

if __name__ == "__main__" :

    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)

    root = a
    root.left = b
    root.right = d
    d.left = c

    print(findDiameter(root))
