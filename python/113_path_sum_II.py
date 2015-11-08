# https://leetcode.com/problems/path-sum-ii/

# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        #     """
        #     :type root: TreeNode
        #     :type sum: int
        #     :rtype: List[List[int]]
        #     """
        solution = []
        self.helper(root, sum, 0, [], solution)
        return solution
    
    def helper(self, root, sum, tempSum, tempList, solution):
        if root == None:
            return
        tempList.append(root.val)
        tempSum += root.val
        if root.left == None and root.right == None:
            if tempSum == sum:
                solution.append(list(tempList))
        else:
            self.helper(root.left, sum, tempSum, tempList, solution)
            self.helper(root.right, sum, tempSum, tempList, solution)
        tempList.pop()
            
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
x = Solution()
print x.pathSum(root, 22)