class Node() :
    def __init__(self,val) -> None:
         self.data = val
         self.left = self.right = None


def inOrder(root : Node) :
    # L N R
    if root :
        return inOrder(root.left) + [root.data] + inOrder(root.right)
    return []

def preOrder(root : Node) :
    if root :
        return [root.data] + preOrder(root.left) + preOrder(root.right)
    return []

def postOrder(root: Node) :
    if root :
        return postOrder(root.left) + postOrder(root.right) + [root.data]
    return []

if __name__ == "__main__" :
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print(inOrder(root))
    print(preOrder(root))
    print(postOrder(root))