package LeetCode.NaryTreePreorderTraversal;

import Fundamentals.DataStructures.Node;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {

    /*
     * Time: O(n)
     * Space: O(n)
     *
     * Using a global variable list to store the values
     */

    public List<Integer> res = new ArrayList<>();

    public List<Integer> preorder(Node root) {
        if (root == null) return res;

        res.add(root.val);
        for (Node child : root.children) {
            preorder(child);
        }

        return res;
    }

    /*
     * Time: O(n)
     * Space: O(n)
     *
     * Maintaining the values in the tree in a local variable
     */

    public List<Integer> preorder2(Node root) {
        List<Integer> res = new ArrayList<>();
        preorder2(root, res);
        return res;
    }

    private void preorder2(Node root, List<Integer> list) {
        if (root != null) {
            list.add(root.val);
            for (int i = 0; i < root.children.size(); i++) {
                preorder2(root.children.get(i), list);
            }
        }
    }

    /*
     * Time: O(n)
     * Space: O(n)
     *
     * Iterative approach
     */

    public List<Integer> preorder3(Node root) {
        List<Integer> res = new ArrayList<>();

        if (root == null) return res;

        Stack<Node> s = new Stack<>();
        s.add(root);

        while (!s.isEmpty()) {

            root = s.pop();
            res.add(root.val);

            // Add from right to left in the stack because a stack is FILO
            // In preOrder, we want to visit left to right
            for (int i = root.children.size() - 1; i >= 0; i--) {
                s.add(root.children.get(i));
            }
        }

        return res;
    }
}
