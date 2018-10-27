package LeetCode.MaximumDepthOfNaryTree;

import Fundamentals.DataStructures.Node;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    private Solution solution = new Solution();
    private Node root = new Node();

    @Test
    void testBalancedTree() {
        root = Node.getBalanced3aryTree();

        int actual = solution.maxDepth(root);
        int actual2 = solution.maxDepth2(root);
        int expected = 3;

        assertEquals(actual, expected);
        assertEquals(actual2, expected);
    }

    @Test
    void testEmptyTree() {
        root = Node.getEmptyNaryTree();

        int actual = solution.maxDepth(root);
        int actual2 = solution.maxDepth2(root);
        int expected = 0;

        assertEquals(actual, expected);
        assertEquals(actual2, expected);
    }

    @Test
    void testLinkedList() {
        root = Node.getLinkedList();

        int actual = solution.maxDepth(root);
        int actual2 = solution.maxDepth2(root);
        int expected = 3;

        assertEquals(actual, expected);
        assertEquals(actual2, expected);
    }

}