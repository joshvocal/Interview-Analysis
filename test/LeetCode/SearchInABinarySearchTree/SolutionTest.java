package LeetCode.SearchInABinarySearchTree;

import Fundamentals.DataStructures.TreeNode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    private Solution solution = new Solution();
    private TreeNode root = new TreeNode();

    @Test
    void testBalancedTree() {
        root = TreeNode.getBalancedTree();
        int val = 7;

        TreeNode actual = solution.searchBST(root, val);
        TreeNode expected = new TreeNode(7);

        assertEquals(actual.val, expected.val);
    }
}