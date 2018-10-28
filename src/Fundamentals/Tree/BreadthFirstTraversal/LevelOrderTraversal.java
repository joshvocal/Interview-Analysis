package Fundamentals.Tree.BreadthFirstTraversal;

import Fundamentals.DataStructures.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class LevelOrderTraversal {

    /*
     * Time: O(n)
     * The algorithm is linear run-time as it visits every node in the tree.
     * If the amount of nodes in the tree doubles, so does the time.
     *
     * Space:
     *
     * Average: O(n)
     * The space is linear for the average case because of the data structure we
     * are using, a queue, will at most hold the lowest level of the tree.
     *
     * Best: O(1)
     * The space is constant when a tree is a linked-list. We will hold at most one node in each level
     *
     * Resource: https://eugene-eeo.github.io/blog/tree-traversal-storage.html
     */

    public static List<List<Integer>> levelOrderTraversal(TreeNode root) {

        List<List<Integer>> res = new ArrayList<>();

        if (root == null) return res;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {

            int size = queue.size();
            List<Integer> level = new ArrayList<>();

            for (int i = 0; i < size; i++) {

                TreeNode currentNode = queue.poll();
                level.add(currentNode.val);

                if (currentNode.left != null) {
                    queue.add(currentNode.left);
                }

                if (currentNode.right != null) {
                    queue.add(currentNode.right);
                }
            }

            res.add(level);
        }

        return res;
    }
}
