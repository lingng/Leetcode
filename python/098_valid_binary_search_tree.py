# https://leetcode.com/problems/validate-binary-search-tree/

# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # max int and min int are set to be test cases. 
        return self.validBST(root, -2147483649, 2147483648)
        
    def validBST(self, root, min, max):
        if root is None:
            return True
        if root.val >= max or root.val <= min:
            return False
        return self.validBST(root.left, min, root.val) and self.validBST(root.right, root.val, max)
        