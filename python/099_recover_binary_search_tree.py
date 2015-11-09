# https://leetcode.com/problems/recover-binary-search-tree/

# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        list = []
        listnode = []
        self.inorder(root, list, listnode)
        list.sort()
        for i in range(len(list)):
            listnode[i].val = list[i]
            
        
    def inorder(self, root, list, listnode):
        if root:
            self.inorder(root.left, list, listnode)
            list.append(root.val)
            listnode.append(root)
            self.inorder(root.right, list, listnode)
            
    def recoverTree1(self, root):
        self.n1 = self.n2 = None
        self.prev = None
        self.FindTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val

    def FindTwoNodes(self, root):
        if root:
            self.FindTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                self.n2 = root
                if self.n1 == None:
                    self.n1 = self.prev
            self.prev = root
            self.FindTwoNodes(root.right)