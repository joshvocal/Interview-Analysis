package LeetCode.NaryTreePostorderTraversal;

import Fundamentals.DataStructures.Node;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {

    /*
     * Time: O(n)
     * Space: O(n)
     */

    public List<Integer> postorder(Node root) {
        List<Integer> res = new ArrayList<>();
        postorder(root, res);
        return res;
    }

    private void postorder(Node root, List<Integer> list) {
        if (root != null) {
            for (int i = 0; i < root.children.size(); i++) {
                postorder(root.children.get(i), list);
            }
            list.add(root.val);
        }
    }

    /*
     * Time: O(n)
     * Space: O(n)
     */

    private List<Integer> res = new ArrayList<>();

    public List<Integer> postorder2(Node root) {
        if (root == null) return res;

        for (Node child : root.children) {
            postorder2(child);
        }
        res.add(root.val);

        return res;
    }

    /*
     * Time: O(n)
     * Space: O(n)
     */

    public List<Integer> postorder3(Node root) {

        List<Integer> res = new ArrayList<>();

        if (root == null) return res;

        Stack<Node> s1 = new Stack<>();
        Stack<Node> s2 = new Stack<>();
        s1.push(root);

        while (!s1.isEmpty()) {

            root = s1.pop();
            s2.push(root);

            for (Node child : root.children) {
                s1.push(child);
            }

        }

        while (!s2.isEmpty()) {
            res.add(s2.pop().val);
        }

        return res;
    }

    /*
     * Time: O(n)
     * Space: O(n)
     */

    public List<Integer> postorder4(Node root) {

        List<Integer> res = new ArrayList<>();

        if (root == null) return res;

        Stack<Node> s1 = new Stack<>();
        s1.push(root);

        while (!s1.isEmpty()) {

            root = s1.pop();
            res.add(0, root.val);

            for (Node child : root.children) {
                s1.push(child);
            }
        }

        return res;
    }
}
