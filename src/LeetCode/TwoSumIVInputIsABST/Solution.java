package LeetCode.TwoSumIVInputIsABST;

import Fundamentals.DataStructures.TreeNode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {

    /*
     * Time: O(n)
     * Space: O(n)
     */

    public boolean findTarget(TreeNode root, int k) {
        List<Integer> inorder = inorder(root, new ArrayList<>());

        Set<Integer> set = new HashSet<>();

        for (Integer num : inorder) {
            int comp = k - num;

            if (set.contains(comp)) {
                return true;
            }

            set.add(num);
        }

        return false;
    }

    private List<Integer> inorder(TreeNode root, List<Integer> list) {
        if (root == null) return list;

        inorder(root.left, list);
        list.add(root.val);
        inorder(root.right, list);

        return list;
    }

    /*
     * Time: O(n + log(n))
     * Space: O(n)
     */

    public boolean findTarget2(TreeNode root, int k) {
        List<Integer> inorder = inorder(root, new ArrayList<>());

        int lo = 0;
        int hi = inorder.size() - 1;

        while (lo < hi) {

            int sum = inorder.get(lo) + inorder.get(hi);

            if (sum == k) {
                return true;
            } else if (sum < k) {
                lo++;
            } else if (sum > k) {
                hi--;
            }
        }

        return false;
    }

    /*
     * Time: O(n)
     * Space: O(n)
     */

    public boolean findTarget3(TreeNode root, int k) {
        return inorder(root, k, new HashSet<>());
    }

    private boolean inorder(TreeNode root, int k, HashSet<Integer> set) {
        if (root == null) return false;
        if (set.contains(k - root.val)) return true;

        set.add(root.val);
        boolean left = inorder(root.left, k, set);
        boolean right = inorder(root.right, k, set);

        return left || right;
    }
}
