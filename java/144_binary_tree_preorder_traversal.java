// https://leetcode.com/problems/binary-tree-preorder-traversal/

// Given a binary tree, return the preorder traversal of its nodes' values.
// For example:
// Given binary tree {1,#,2,3},
//    1
//     \
//      2
//     /
//    3
// return [1,2,3].

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> rst = new ArrayList<Integer>();
        preorder(root,rst);
        return rst;
    }
    public void preorder(TreeNode root, List<Integer> rst){
        if (root == null){
            return;
        }
        rst.add(root.val);
        preorder(root.left, rst);
        preorder(root.right, rst);
    }
}