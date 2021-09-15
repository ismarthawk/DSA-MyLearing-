# How to construct the tree given the inorder and preorder traversals

def inorder(root) :
    if root :
        inorder(root.left)
        inorder(root.right)
        print(root.data,end= " ")
    

class Node() :
    def __init__(self,data) :
        self.data = data
        self.left = self.right = None





def buildTree(inorder : list , preorder : list) -> Node :
    if len(inorder) != len(preorder) :
        return "This can't be done"
    if len(inorder) == 0 :
        return None
    root = Node(preorder[0])
    left_inorder = inorder[:inorder.index(preorder[0])]
    right_inorder = inorder[inorder.index(preorder[0])+1:]
    root.left = buildTree(left_inorder,preorder[1:len(left_inorder)+1])
    root.right = buildTree(right_inorder,preorder[len(left_inorder)+1:])
    return root

if __name__ == "__main__" :
    tree = buildTree(list("DBEAFC"),list("ABDECF"))
    inorder(tree)
