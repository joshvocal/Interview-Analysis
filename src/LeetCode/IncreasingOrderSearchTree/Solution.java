package LeetCode.IncreasingOrderSearchTree;

import Fundamentals.DataStructures.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class Solution {

    public TreeNode increasingBST(TreeNode root) {
        List<TreeNode> inorderList = inorder(root, new ArrayList<>());
        TreeNode curr = root;

        for (TreeNode node : inorderList) {
            node.left = null;
            curr.right = node;
            curr = curr.right;
        }

        return root;
    }

    private List<TreeNode> inorder(TreeNode root, List<TreeNode> list) {
        if (root == null) return list;

        inorder(root.left, list);
        list.add(root);
        inorder(root.right, list);

        return list;
    }
}
