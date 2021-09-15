class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None

def findAncestors(root,data) :
    if root  is None :
        return False
    if root.data == data :
        return True

    if (findAncestors(root.left,data) or findAncestors(root.right,data)) :
        print(root.data,end=" ")
        return True
    else :
        return False

if __name__ == "__main__" :

    a = Node(10)
    b = Node(20)
    c = Node(30)
    d = Node(40)

    root = a
    root.left = b
    root.right = d
    d.left = c

    findAncestors(root,30)
