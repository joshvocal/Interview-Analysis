package LeetCode.NaryTreeLevelOrderTraversal;

import Fundamentals.DataStructures.Node;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class Solution {

    /*
     * Time: O(n)
     * The algorithm run-time is linear as it visits every node in the n-ary tree.
     * If the amount of nodes in the tree doubles, so does the time.
     *
     * Space: O(log(n))
     * The space is logarithmic for the average case because of the data structure we
     * are using, a queue, will at most hold the lowest level of the tree.
     *
     * Idea:
     * Use the classic level-order algorithm to traverse this k-ary tree.
     * A typical example using level-order traversal often uses a binary tree. Sine
     * we are traversing a k-ary tree we don't need to check if the tree has a left or right
     * child before adding it to the queue. we just need to iterate through all of the node's
     * children and add them to the queue to get the next level.
     */

    public List<List<Integer>> levelOrder(Node root) {
        List<List<Integer>> res = new ArrayList<>();

        if (root == null) return res;

        Queue<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {

            int nodesInLevel = q.size();
            List<Integer> level = new ArrayList<>();

            for (int i = 0; i < nodesInLevel; i++) {

                Node curr = q.poll();
                level.add(curr.val);

                for (Node child : curr.children) {
                    q.add(child);
                }
            }

            res.add(level);
        }

        return res;
    }
}
