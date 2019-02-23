package LeetCode.MaximumDepthOfNaryTree;

import Fundamentals.DataStructures.Node;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;

class SolutionTest {

    private Solution solution = new Solution();
    private Node root = new Node();

    @Test
    void testBalancedTree() {
        root = Node.getBalanced3aryTree();

        int actual = solution.maxDepth(root);
        int actual2 = solution.maxDepth2(root);
        int expected = 3;

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
    }

    @Test
    void testEmptyTree() {
        root = Node.getEmptyNaryTree();

        int actual = solution.maxDepth(root);
        int actual2 = solution.maxDepth2(root);
        int expected = 0;

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
    }

    @Test
    void testLinkedList() {
        root = Node.getLinkedList();

        int actual = solution.maxDepth(root);
        int actual2 = solution.maxDepth2(root);
        int expected = 3;

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
    }
}