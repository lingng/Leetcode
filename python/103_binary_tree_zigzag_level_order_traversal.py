# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def level(self, root, level, solution):
        if root:
            if len(solution) < level + 1:
                solution.append([])
            self.level(root.left, level + 1, solution)
            self.level(root.right, level + 1, solution)
            solution[level].append(root.val)
            
    def zigzagLevelOrder(self, root):
        res = []
        self.level(root, 0, res)
        level = len(res)
        # print level
        for i in range(0, level):
            if i % 2 == 0:
                continue
            else:
                res[i].reverse()
        return res