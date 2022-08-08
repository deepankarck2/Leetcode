class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
def inOrderTraverse(tree, array):
    if(tree == None):
        return array

    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)

def preOrderTraverse(tree, array):
    if(tree == None):
        return array

    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)

def postOrderTraverse(tree, array):
    if(tree == None):
        return array
    
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)


root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.right = BST(22)       

array = []
inOrderTraverse(root,array)
print(array)

array = []
preOrderTraverse(root,array)
print(array)

array = []
postOrderTraverse(root,array)
print(array)