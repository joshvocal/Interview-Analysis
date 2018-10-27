package Fundamentals.Tree.DepthFirstTraversal;

import Fundamentals.Tree.TreeNode;
import sun.reflect.generics.tree.Tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class PostOrderTraversal {


    /*
     * Time: O(n)
     *
     * Space: O(n)
     *
     * Resource:
     */

    public List<Integer> postOrderTraversalIterative(TreeNode root, List<Integer> list) {

        if (root == null) return list;

        Stack<TreeNode> s1 = new Stack<>();
        Stack<TreeNode> s2 = new Stack<>();
        s1.push(root);

        while (!s1.isEmpty()) {

            root = s1.pop();
            s2.push(root);

            if (root.left != null) {
                s1.push(root.left);
            }

            if (root.right != null) {
                s1.push(root.right);
            }
        }

        while (!s2.isEmpty()) {
            root = s2.pop();
            list.add(root.val);
        }

        return list;
    }

    public List<Integer> postOrderTraversalIterative2(TreeNode root, List<Integer> list) {
        return list;
    }

    /*
     * Time: O(n)
     * The algorithm runs in linear time because we need to visit every node in the tree
     *
     * Space:
     *
     * Average: O(log(n))
     * The space will be logarithmic because the stack space in the recursive calls will be the same as height
     * of a binary tree
     *
     * Worst: O(n)
     * The space will be linear because the stack space will be the entire tree if it is a a linked-list
     *
     * Resource:
     */

    public List<Integer> postOrderTraversalRecursive(TreeNode root, List<Integer> list) {
        if (root == null) return list;

        postOrderTraversalRecursive(root.left, list);
        postOrderTraversalRecursive(root.right, list);
        list.add(root.val);

        return list;
    }
}
