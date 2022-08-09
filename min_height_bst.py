def minHeightBst(array):
    root = None
    return consMinHeight2(array, 0, len(array)-1)

# Comlexity: Time: O(N * Log(N)) --> Number of nodes in the array that was added * log(n) time of the addition
# Space :          O(N) --> number of nodes that were added 
#      
def consMinHeight(array, root, start, end):
    if(start > end):
        return root

    mid_index = (start+end)//2 

    if(root == None):
        root = BST(array[mid_index])
    else:
        root.insert(array[mid_index])

    consMinHeight(array, root, start, mid_index-1)
    consMinHeight(array, root, mid_index+1, end)

    return root


def consMinHeight2(array, start, end):
    # So, since we are aready going down left and right, it makes sense not to reference 
    # root node every time we insert something. Instead, we can keep track of the right and left hand of
    # of the root at each passing.

    # -- Runs in O(N) time, Space is still O(N)
    
    if(start > end):
        return None

    mid_index = (start+end)//2

    root = BST(array[mid_index])

    root.left = consMinHeight2(array, start, mid_index-1) #Smart Idea. 
    root.right = consMinHeight2(array, mid_index+1, end)

    return root

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def inOrderTraverse(tree):
    if(tree == None): #//Maybe not a good idea, since we are not going to be returning anything. See preOrder for a better
        return

    inOrderTraverse(tree.left) 
    print(tree.value, end=" ")
    inOrderTraverse(tree.right)
     

array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
tree = minHeightBst(array)
print(tree)
inOrderTraverse(tree)