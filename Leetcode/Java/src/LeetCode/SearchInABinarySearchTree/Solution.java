package LeetCode.SearchInABinarySearchTree;

import Fundamentals.DataStructures.TreeNode;

public class Solution {

    /*
     * Time: O(log(n))
     * We only need to traverse the height of the BST which is log(n)
     *
     * Space: O(log(n))
     * The number of recursive calls is the same as the height of a tree
     */

    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null) return null;

        if (val == root.val) {
            return root;
        } else if (val < root.val) {
            return searchBST(root.left, val);
        } else if (val > root.val) {
            return searchBST(root.right, val);
        }
        
        return null;
    }
}
