# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathP = self.findPath(root, p)
        pathQ = self.findPath(root, q)
        lenP = len(pathP)
        lenQ = len(pathQ)
        ans = None
        x = 0
        while x < min(lenP, lenQ) and pathP[x] == pathQ[x]:
            ans = pathP[x]
            x = x + 1
        return ans
        
    def findPath(self, root, target):
        stack = []
        lastVisit = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and lastVisit != peek.right:
                    root = peek.right
                else:
                    if peek == target:
                        return stack
                    lastVisit = stack.pop()
                    root = None
        return stack


x = Solution()
root = TreeNode(1)
right = TreeNode(2)
root.right = right
print x.lowestCommonAncestor(root, root, right)