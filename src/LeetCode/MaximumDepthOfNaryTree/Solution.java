package LeetCode.MaximumDepthOfNaryTree;

import Fundamentals.DataStructures.Node;

import java.util.LinkedList;
import java.util.Queue;

public class Solution {

    /*
     * Time:
     * Space:
     * Idea:
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
     * Time:
     * Space:
     * Idea:
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
