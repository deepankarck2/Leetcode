from tkinter.tix import Tree
from traceback import print_tb


def merge(nums1, nums2):
    len1 = len(nums1)
    len2 = len(nums2)
    i,j = 0,0
    answer = [] 
    while(i< len1 and j < len2):
        if(nums1[i] <= nums2[j]):
            answer.append(nums1[i])
            i+= 1
        else:
            answer.append(nums2[j])
            j+= 1
    
    while(i < len1):
        answer.append(nums1[i])
        i+= 1
    
    while(j < len2):
        answer.append(nums2[j])
        j+= 1
    
    return answer
def question1(): 
    nums1 = [1,4,6]
    nums2 = [2,4,3,5]
    print(merge(nums1,nums2))


class TreeNode:
    def __init__(self,x) -> None:
        self.val = x
        self.left = self.right = None

def sum_of_left_leaves(root):
    sum = 0

    if(root.left is not None):
        left = root.left
        if(left.left == None and left.right == None):
            sum += left.val 
    
        sum += sum_of_left_leaves(root.left)
        sum += sum_of_left_leaves(root.right)

    return sum
    

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(sum_of_left_leaves(root))