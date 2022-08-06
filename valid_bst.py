# This is an input class. Do not edit.
from tkinter.tix import Tree
from pyparsing import None_debug_action


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(root, min_val, max_val):
    if(root == None):
        return True 
    
    if(root.value < min_val or root.value >= max_val):
        return False

    leftValid = validateBstHelper(root.left, min_val, root.value)
    rightValid = validateBstHelper(root.right, root.value, max_val)

    return leftValid and rightValid
