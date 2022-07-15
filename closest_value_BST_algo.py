
from traceback import print_tb


def findClosestValueInBst(tree, target):
    min_val = tree.value
    closest = None 
    while(tree != None):
        if(target <= tree.value):
            if(abs(target-tree.value) < min_val):
                min_val = abs(tree.value-target)
                closest = tree.value
            tree = tree.left

        elif(target > tree.value):
            if(abs(target-tree.value) < min_val):
                min_val = abs(tree.value-target)
                closest = tree.value
            tree = tree.right
    return closest

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def main():
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        target = 12
        print(findClosestValueInBst(root,target))

if __name__ == '__main__':
    main()