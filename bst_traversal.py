class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
def inOrderTraverse(tree, array):
    if(tree == None): #//Maybe not a good idea, since we are not going to be returning anything. See preOrder for a better
        return array

    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)

    return array

def preOrderTraverse(tree, array):

    if tree is not None: #do this as long as we are not in a leaf node
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)

    return array #return the array if we are in a leaf node

def postOrderTraverse(tree, array):
    if(tree == None):
        return array
    
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)

    return array

root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.right = BST(22)       

array = []
inOrderTraverse(root,array)
print("Inorder Travelsal     :   " , array)

array = []
preOrderTraverse(root,array)
print("Pre-order Traversal   :   ", array)

array = []
postOrderTraverse(root,array)
print("Post-order Traversal  :   ", array)