# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        self.maxSum = -10**10
        self.dfs(root)
        return self.maxSum

    def dfs(self, root):
        if not root: return 0
        vLeft = self.dfs(root.left)
        vRight = self.dfs(root.right)
        self.maxSum = max(self.maxSum, vLeft+vRight+root.val)
        # print self.maxSum
        # print max(root.val+vLeft, root.val+vRight, 0)
        return max(root.val+vLeft, root.val+vRight, 0)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(10)
root.left.right = TreeNode(20)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
x = Solution()
x.maxPathSum(root)