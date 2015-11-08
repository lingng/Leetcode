# https://leetcode.com/problems/count-complete-tree-nodes/

# Given a complete binary tree, count the number of nodes.

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.countLeft(root) + 1
        right = self.countRight(root) + 1
        if left == right:
            return (2<<(left-1)) - 1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
            
    def countLeft(self, root):
        if root is None:
            return 0
        count = 0
        while root.left:
            count = count + 1
            root = root.left
        return count
        
    def countRight(self, root):
        if root is None:
            return 0
        count = 0
        while root.right:
            count = count + 1
            root = root.right
        return count
        