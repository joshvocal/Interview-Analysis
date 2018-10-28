package LeetCode.LeafSimilarTrees;

import Fundamentals.DataStructures.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class Solution {

    /*
     * Time: O(n + m)
     * We need to traverse the all the nodes within the two trees, n and m
     *
     * Space: O(n + m)
     * We are storing all the elements from both trees into lists so we can compare them.
     *
     * Basically a modification of pre-order traversal. We just need to change the condition
     * of when we add elements to the list. If the current node is a leaf, add it to the list.
     * Once we do that for both trees, we can just compare if both lists are equal!
     */

    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaves1 = preorder(root1, new ArrayList<>());
        List<Integer> leaves2 = preorder(root2, new ArrayList<>());

        return leaves1.equals(leaves2);
    }

    private List<Integer> preorder(TreeNode root, List<Integer> list) {
        if (root == null) return list;

        if (root.left == null && root.right == null)
            list.add(root.val);
        preorder(root.left, list);
        preorder(root.left, list);

        return list;
    }
}
