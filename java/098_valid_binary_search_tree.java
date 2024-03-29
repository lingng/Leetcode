https://leetcode.com/problems/validate-binary-search-tree/

// Given a binary tree, determine if it is a valid binary search tree (BST).
// Assume a BST is defined as follows:
// The left subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.


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
    public boolean isValidBST(TreeNode root) {
        // Cannnot use Integer.MAX_VALUE or Integer.MIN_VALUE, since these values are set to be the test cases,
        // and does not meat the min, max conditino in the validBST function.
        return validBST(root, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
    }
    
    private boolean validBST(TreeNode root, double min, double max){
        if (root == null){
            return true;
        }
        if (root.val >= max || root.val <= min){
            return false;
        }
        return validBST(root.left, min, root.val) && validBST(root.right, root.val, max);
    }
}