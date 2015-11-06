# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeHelper(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def buildTreeHelper(self,preorder, a, b, inorder, c, d):
        if a>=b or c>=d:
            return None
        currentNode = TreeNode(preorder[a])
        i = inorder.index(preorder[a])
        currentNode.left = self.buildTreeHelper(preorder,a+1,a+i-c+1,inorder,c,i)
        currentNode.right = self.buildTreeHelper(preorder,a+i-c+1,b, inorder,i+1,d)
        return currentNode