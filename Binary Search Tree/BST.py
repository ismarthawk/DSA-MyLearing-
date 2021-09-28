class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None

def search(root,data) :
    if root :
        if root.data == data :
            return True
        elif root.data > data :
            return search(root.left,data)
        return search(root.right,data)
    return False

def insert(root,data) :
    if root is None :
        root = Node(data)
        return root
    if data == root.data :
        print("Duplicate Found : ",data)
        return root
    elif data < root.data :
        root.left = insert(root.left,data)
    else :
        root.right = insert(root.right,data)
    return root

def inorder(root) :
    if root :
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
    return

def getMin(root) :
    if root is None :
        return None
    if root.left is None :
        return root
    return getMin(root.left)

def getMax(root) :
    if root is None :
        return None
    if root.right :
        return getMax(root.right)
    return root

def getMin2(root) :
    if root is None :
        return None
    pt = root
    while pt.left :
        pt = pt.left
    return pt

def delete(root,data) :
    if root is None :
        print("No such Element")
        return root
    elif root.data > data :
        root.left = delete(root.left,data)
    elif root.data < data :
        root.right = delete(root.right,data)
    else :
        if root.left is None and root.right is None :
            del root
            return None
        elif root.left is not None and root.right is None :
            t = root.left
            del root
            return t
        else :
            k = getMin(root.right)
            root.data = k.data
            root.right = delete(root.right,root.data)

    return root

pre = suc = None

def findInorderSuccessorNPredesessor(root,data) :
    global pre,suc
    if root is None :
        return None
    elif root.data == data :
        if root.left is not None :
            pre = getMax(root.left)
        if root.right is not None :
            suc = getMin(root.right)

    elif root.data > data :
        suc = root
        findInorderSuccessorNPredesessor(root.left,data)
    else :
        pre = root
        findInorderSuccessorNPredesessor(root.right,data)

def checkIsBst(root) :
    if root is None :
        return True
    left = True
    right = True
    if root.left :
        if root.left.data > root.data :
            left = False
    if root.right :
        if root.right.data < root.data :
            right = False

    if not left or not right :
        return False
    return checkIsBst(root.left) and checkIsBst(root.right)


def findCommonAncestor(root,n1,n2) :
    if n1 > n2 :
        n1,n2 = n2,n1
    if root is None :
        return
    if root.data == n1 :
        if search(root.right,n2) :
            return root
        return None
    if root.data == n2  :
        if search(root.left,n1) :
            return root
        return None
    if root.data > n1 and root.data < n2 :
        if search(root.left,n1) and search(root.right,n2) :
            return root
        return None
    if root.data > n2 :
        return findCommonAncestor(root.left,n1,n2)
    return findCommonAncestor(root.right,n1,n2)








if __name__ == "__main__" :
    root = None
    root = insert(root,10)
    root = insert(root,20)
    root = insert(root,5)
    root = insert(root,10)
    root = insert(root,30)

    inorder(root)
    print("")

    # findInorderSuccessorNPredesessor(root,30)
    # if suc and pre :
    #     print("Successor : ",suc.data, "Predessor : ",pre.data)
    # elif suc :
    #     if not pre :
    #         print("Successor : ", suc.data,"Predessor :" ,pre)
    # elif pre :
    #     if not suc :
    #         print("Successor : ", suc,"Predessor :" ,pre.data)
    # else :
    #     print(suc,pre)

    printNodeValue(kthSmallestInorder(root,1))
