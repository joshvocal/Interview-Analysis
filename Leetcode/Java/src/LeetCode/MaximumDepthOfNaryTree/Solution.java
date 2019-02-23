package LeetCode.MaximumDepthOfNaryTree;

import Fundamentals.DataStructures.Node;

import java.util.LinkedList;
import java.util.Queue;

public class Solution {

    /*
     * Time: O(n)
     * We iterate through all the nodes in the tree using BFS.
     *
     * Space: O(n)
     * We are using a queue as the data structure to store the levels of the k-ary tree.
     * The maximum nodes that the queue will hold is at the bottom are the leaves of the k-ary tree
     * which is (n / k) + 1
     */

    public int maxDepth(Node root) {
        if (root == null) return 0;

        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        int depth = 0;

        while (!queue.isEmpty()) {

            int nodesInLevel = queue.size();

            for (int i = 0; i < nodesInLevel; i++) {

                Node curr = queue.poll();

                for (Node child : curr.children) {
                    queue.add(child);
                }
            }

            depth++;
        }

        return depth;
    }

    /*
     * Time: O(n)
     * We must iterate through the entire k-ary tree to find the maximum depth of the tree
     *
     * Space: O(log(n))
     * Since we are recursively going down into the tree, the stack space for our recursion will
     * be the same as the height of our tree.
     */

    public int maxDepth2(Node root) {
        if (root == null) return 0;

        int maxDepth = 0;

        for (Node child : root.children) {
            maxDepth = Math.max(maxDepth, maxDepth2(child));
        }

        return maxDepth + 1;
    }
}
