# Average: time: O(long(n)) | Space: O(1) --> Since Iterative
# Wrost : time: O(N), a straight branch| space: O(1) --> since iterative


def inorder(tree, target, closest, min_val):
    
    if(tree == None):
        return closest; 

    inorder(tree.left, target, closest, min_val)
    if(abs(tree.value-target) < min_val):
            closest = tree.value
            min_val = abs(tree.value-target)
    inorder(tree.right, target, closest, min_val)
            

def findClosestValueInBst1(tree, target):
    closest = tree.value
    min_val = float('inf')
    inorder(tree, target, closest, min_val)


def findClosestValueInBst(tree, target):
    min_val = float('inf')  
    closest = tree.value
    
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
        print(findClosestValueInBst1(root,target))

if __name__ == '__main__':
    main()