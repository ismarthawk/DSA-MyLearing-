class Node() :
    def __init__(self,value) :
        self.data = value
        self.left = self.right = None

#  print(type(Node(10)))

# Seach a node in BST

def search(root,data) :
    if root is None : return None
    if root.data == data :
        return root
    elif root.data < data :
        return search(root.right , data)
    return search(root.right,data)

# insertion in a BST

def insert(root,data) :
    if root is None :
        return Node(data)
    elif root.data == data :
        return root
    elif root.data > data :
        root.left = insert(root.left,data)
    else :
        root.right = insert(root.right,data)

    return root

# Find min element in the tree.

def findMin(root) :
    if not root : return root
    iter = root
    while iter.left : iter = iter.left
    return iter

# Find max element in the tree.

def findMax(root) :
    if root is None : return None
    if root.right is None : return root
    return findMax(root.right)




# delete some data in tree.

def delete(root,data) :
    if root is None :
        return None
    elif root.data > data :
        root.left = delete(root.left,data)
    elif root.data < data :
        root.right = delete(root.right,data)
    else :
        if root.left is None and root.right is None :
            del root
            return None
        elif root.right is None :
            left = root.left
            del root
            return left
        else :
            minNode = findMin(root.right)
            root.data = minNode.data
            root.right = delete(root.right,minNode.data)

    return root



# find the inorder predecessor and successor for a given element in BST


pre = succ = None

def findPreSucc(root,data) :
    if root is None : return
    if root.data == data :
        if root.left :
            pre = findMin(root.left)
        if root.right :
            suc = findMin(root.right)
        return
    if root.data > data :
        suc = root
        findPreSucc(root.left,data)
    else :
        pre = root
        findPreSucc(root.right,data)


# check a Binary tree is BST or not.

def isBST(root) :
    if root is None : return True
    if root.left :
        if root.left.data >= root.data : return False
    if root.right :
        if root.right.data <= root.data : return False
    return isBST(root.left) and isBST(root.right)

    ## This is failing some test cases as we are not maintaing the permissable values in a sub tree.
    ## So we keep track of the min and max of the tree.

# check a Binary  Tree is a BST or not - 2.

def isBST2(root) :
    min  = float('-inf')
    max = float('inf')

    def check(root,min,max) :
        if root is None : return True
        if root.data <= min or root.data >= max :
            return False
        if root.left :
            if root.data <= root.left.data : return False
        if root.right :
            if root.data >= roo.right.data : return False
        return check(root.left,min,root.data) and check(root.right,root.data,max)

    return check(root,min,max)

# Find the least Common Ancestor.

def findLCA(root,d1,d2) :
    if root is None :
        return None
    if root.data < d1 and root.data < d2 :
        return findLCA(root.right,d1,d2)

    if root.data > d1 and root.data > d2 :
        return findLCA(root.left,d1,d2)

    return root

# Find k the smallest element is the BST.

## 1 approach is to find the Inorder Traversal and find the kth element in the result

## 2nd approach is to use a stack, maintaing a count var and doing the inorder travsrsal
    # this takes O(n) - time and O(h) - space complexity

def findKthSmallest(root,k) :
    if root is None : return -1
    count = 0
    stack = []
    iter = root
    while True :
        if iter :
            stack.append(iter)
            iter = iter.left
        elif stack :
            node = stack.pop(-1)
            count += 1
            if count > k :
                return -1
            if count == k : return node.data
            iter = node.right
        else :
            break
    return -1
