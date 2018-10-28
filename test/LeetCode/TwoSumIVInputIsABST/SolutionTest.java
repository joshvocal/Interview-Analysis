package LeetCode.TwoSumIVInputIsABST;

import Fundamentals.DataStructures.TreeNode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    private Solution solution = new Solution();
    private TreeNode root = new TreeNode();

    @Test
    void testBalancedTree() {
        root = TreeNode.getBalancedTree();
        int target = 5;

        boolean actual = solution.findTarget(root, target);
        boolean actual2 = solution.findTarget2(root, target);
        boolean actual3 = solution.findTarget3(root, target);
        boolean expected = true;

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
        assertEquals(expected, actual3);
    }
}