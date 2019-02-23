package Fundamentals.Tree.DepthFirstTraversal;

import Fundamentals.DataStructures.TreeNode;

import java.util.List;
import java.util.Stack;

public class PreOrderTraversal {


    /*
     * Time: O(n)
     * The algorithm runs in linear time because we must visit every node within the tree
     *
     * Space:
     *
     * Average: O(log(n))
     * The space is logarithmic because if we have a balanced binary tree, the number of nodes in
     * our stack will be the same as the height of the binary tree, log(n).
     *
     * Worst: O(log(n))
     * The space is linear because is we have a tree which is a linked-list, the number
     * will be the height of the entire linked-list which contains n nodes in our stack.
     *
     * Resource:
     */

    public static List<Integer> preOrderTraversalIterative(TreeNode root, List<Integer> list) {

        if (root == null) return list;

        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()) {

            root = stack.pop();

            list.add(root.val);
            if (root.right != null) stack.push(root.right);
            if (root.left != null) stack.push(root.left);
        }

        return list;
    }

    /*
     * Time: O(n)
     * The algorithm runs in linear time because we must visit every node within the tree
     *
     * Space:
     *
     * Average: O(log(n))
     * The space is logarithmic because if we have a balanced binary tree, the number of stack calls
     * will be the height of the binary tree which is log(n).
     *
     * Worst: O(n)
     * The space is linear because is we have a tree which is a linked-list, the number of stack calls
     * will be the height of the entire linked-list which contains n nodes.
     *
     *
     * Resource:
     */

    public static List<Integer> preOrderTraversalRecursive(TreeNode root, List<Integer> list) {
        if (root == null) return list;

        list.add(root.val);
        preOrderTraversalRecursive(root.left, list);
        preOrderTraversalRecursive(root.right, list);

        return list;
    }
}
