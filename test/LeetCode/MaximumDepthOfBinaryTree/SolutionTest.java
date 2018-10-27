package LeetCode.MaximumDepthOfBinaryTree;

import Fundamentals.DataStructures.TreeNode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    private Solution solution = new Solution();
    private TreeNode root = new TreeNode();

    @Test
    void testBalancedBinaryTree() {
        root = TreeNode.getBalancedTree();

        int actual = solution.maxDepth(root);
        int actual2 = solution.maxDepth2(root);
        int expected = 3;

        assertEquals(actual, expected);
        assertEquals(actual2, expected);
    }

    @Test
    void testLinkedList() {
        root = TreeNode.getLinkedList();

        int actual = solution.maxDepth(root);
        int actual2 = solution.maxDepth2(root);
        int expected = 7;

        assertEquals(actual, expected);
        assertEquals(actual2, expected);
    }

    @Test
    void testEmptyTree() {
        root = TreeNode.getEmptyTree();

        int actual = solution.maxDepth(root);
        int actual2 = solution.maxDepth(root);
        int expected = 0;

        assertEquals(actual, expected);
        assertEquals(actual2, expected);
    }
}