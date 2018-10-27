package Fundamentals.Tree.DepthFirstTraversal;

import Fundamentals.Tree.TreeNode;

import java.util.List;
import java.util.Stack;

public class InorderTraversal {

    /*
     * Time: O(n)
     * The algorithm runs in linear time because we have to visit every node within the tree
     *
     * Space:
     *
     * Average: O(log(n))
     * The space is logarithmic because of the stack will contain at most the height of the tree.
     *
     * Worst: O(n)
     * The space is linear in the worst case if we have a tree which is a linked list. The stack will contain all
     * the elements in the tree.
     *
     * Resource:
     */

    public List<Integer> inOrderTraversalIterative(TreeNode root, List<Integer> res) {

        if (root == null) return res;

        Stack<TreeNode> stack = new Stack<>();

        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }

            root = stack.pop();
            res.add(root.val);
            root = root.right;

        }

        return res;
    }

    /*
     * Time: O(n)
     * The algorithm runs in linear time because we have to visit every node within the tree once.
     *
     * Space:
     *
     * Average: O(log(n))
     * The space is logarithmic because of the stack calls when traversing the tree. If the tree is balanced, the
     * number of stack calls will be the same as the height of the tree, which is logarithmic.
     *
     * Worst: O(n)
     * The space is linear in the worst case if we have a tree which is a linked list. The number of stacks calls
     * will contain all the nodes in the tree.
     */

    public List<Integer> inOrderTraversalRecursive(TreeNode root, List<Integer> res) {
        if (root == null) return res;

        inOrderTraversalRecursive(root.left, res);
        res.add(root.val);
        inOrderTraversalRecursive(root.right, res);

        return res;
    }
}
