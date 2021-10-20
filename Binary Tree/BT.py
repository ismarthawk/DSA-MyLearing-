class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None


# Traversal Techniques
## inorder Traversal

def inorder(root) :
    res = []
    if root is None :
        return res
    res = inorder(root.left) + [root.data] + inorder(root.right)

## preorder

def preorder(root) :
    if root is None : return []
    return [root.data]+ preorder(root.left) +  preorder(root.right)

## postorder

def postorder(root) :
    if root is None : return []
    return postorder(root.left) + postorder(root.right) + [root.data]

## level order Traversal (or) Breadth First Search.

def levelOrderTraversal(root) :
    if root is None : return []
    res = []
    q = [root]
    while q :
        node = q.pop(0)
        res.append(q.data)
        if node.left : q.append(node.left)
        if node.right : q.append(node.right)
    return res

# Diamerter of A tree

def diameter(root) :
    def height(root) :
        if root is None : return 0
        return 1 + max(height(root.left),height(root.right))

    if root is None : return 0
    return max(
        1+height(root.left) + height(root.right),
        diameter(root.left),
        diameter(root.right)
    )

# Inorder Traversal Without recursion.

def inorderWithoutRecursion(root) :

    """
        The algo is to maintain a stack.
        push the left side nodes till end.
        if no left nodes remain, pop out of the stack and append to result
        then push all left nodes of the right subtree of pop out node.
    """
    if root is None : return []
    res = []
    s = list()
    iter = root
    while True :
        if iter is not None :
            s.append(root.left)
            iter = iter.left
        elif stack :
            iter = s.pop(-1)
            res.append(iter.data)
            iter = iter.right
        else :
            break
    return res

# Height/ Depth of a tree

def height(root) :
    if root is None : return 0
    return 1 + max(height(root.left),height(root.right))

# Construct Tree Using inorder and postorder traversals


def buildTree(inorder,postorder) :
    if len(inorder) ==0 :
        return None
    res = Node(preorder[0])
    if len(inorder) == 1 : return res
    i = inorder.index(preorder[0])
    res.left = buildTree(inorder[:i],preorder[1:i+1])
    res.right = buildTree(inorder[i+1:],preorder[i+1:])

# Finding max Width .

def maxWidth(root) :
    if root is None : return 0
    d = dict()
    root.depth = 0
    q = [root]
    while q :
        node = q.pop(0)
        if node.depth in d :
            d[node.depth] += 1
        else :
            d[node.depth] = 1
        if node.left :
            node.left.depth = node.depth + 1
            q.append(node.left)
        if node.right :
            node.right.depth = node.depth + 1
            q.append(node.right)

    max = 0
    for value in d.values() :
        if max < value : max = value
    return max

# Print nodes at a distance 'd'

def printKDistanceNodes(root,k) :
    res = []
    def driver(root,k) :
        if root is None : return
        if k == 0 :
            res.append(root.data)
            return
        driver(root.left,k-1)
        driver(root.right,k-1)
    driver(root,k)
    return res


# finding ancestors

def findAncestors(root,target) :
    res = []
    def driver(root,target) :
        if root is None : return False
        if root.data == target : return True
        if driver(root.left,target) or driver(root.right,target) :
            res.append(root.data)
            return True
        return False
    driver(root,target)
    return res

# finding two trees are identical

def isIdentical(root1,root2) :
    if root1 is None and root2 is None : return True
    if(root1 is None and root2 is Not None) or (root1 and root2 is None) :
        return False
    if root1.data == root2.data :
        return isIdentical(root1.left,root2.left) and isIdentical(root1.righth,root2.right)
    return False

# finding whether a tree is subtree of other
## we check whether root2 is a sub of root1
def isSubtree(root1,root2) :
    if root2 is None : return True
    if root1 is None : return False
    if isIdentical(root1,root2) : return True
    return isSubtree(root1.left,root2) or isSubtree(root1.right,root2)


# connect the adjacent nodes of a binary tree

def connect(root) :
    if root is None : return
    q =  [root]
    while q :
        pre = None
        for i in range(len(q)) :
            node = q.pop(0)
            if node.left : q.appned(node.left)
            if node.right : q.append(node.right)
            pre.next = node
        
