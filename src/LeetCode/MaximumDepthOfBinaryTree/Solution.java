package LeetCode.MaximumDepthOfBinaryTree;

import Fundamentals.DataStructures.TreeNode;

import java.util.LinkedList;
import java.util.Queue;

public class Solution {

    /*
     * Time: O(n)
     *
     * The algorithm run-time is linear as we need to traverse through every single node in the tree to get the
     * amount of levels the tree contains
     *
     * Space: O(n)
     *
     * The algorithm contains linear space because we are using a queue to store each level of the binary tree.
     * The queue will contain the most nodes when it has all the leaves of the binary tree, the lowest point of the
     * tree (n / 2) + 1
     *
     * Idea:
     * We will use BFS to traverse through the entire tree. By using level-order traversal we can go through the
     * tree level-by-level and increment our counter each time we traverse to the next level of the tree.
     */

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        int depth = 0;

        while (!queue.isEmpty()) {

            int size = queue.size();

            for (int i = 0; i < size; i++) {

                TreeNode current = queue.poll();

                if (current.left != null) {
                    queue.add(current.left);
                }

                if (current.right != null) {
                    queue.add(current.right);
                }
            }

            depth++;
        }

        return depth;
    }

    /*
     * Time: O(n)
     * The run-time in linear because we need to visit each of the nodes in the binary tree
     *
     * Space: O(log(n))
     * The space is logarithmic because when we recurse down the tree, the number of stack calls we have is the same
     * as the height of a binary tree which is O(log(n))
     *
     * The worst case is when we have a tree that only contains left or right children. In that case the space would
     * be the same as the number of nodes in the binary tree which is O(n)
     *
     * We can use DFS to traverse the entire tree. Recursively go down the tree, when we hit the leaves of the tree
     * we can start counting up from the bottom til we reach back up to the top
     */

    public int maxDepth2(TreeNode root) {
        if (root == null) return 0;

        int left = maxDepth2(root.left);
        int right = maxDepth2(root.right);

        return Math.max(left, right) + 1;
    }
}
