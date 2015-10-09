# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        tmpStr = ""
        self.getPath(result, tmpStr, root)
        return result

    def getPath(self, result, tmpStr, root):
        if tmpStr == "" and root.val is not None:
            tmpStr = tmpStr + str(root.val)
        elif tmpStr != "" and root.val is not None:
            tmpStr = tmpStr + "->" + str(root.val)

        if root is not None and root.left is None and root.right is None:
            result.append(tmpStr)
            return
        else:
            if root.left is not None and root.right is None:
                self.getPath(result, tmpStr, root.left)
            elif root.right is not None and root.left is None:
                self.getPath(result, tmpStr, root.right)
            else:
                self.getPath(result, tmpStr, root.left)
                self.getPath(result, tmpStr, root.right)

x = Solution()
root = TreeNode(1)
left1 = TreeNode(2)
right1 = TreeNode(3)
left2 = TreeNode(5)
root.left = left1
root.right = right1
left1.right = left2
print x.binaryTreePaths(root)