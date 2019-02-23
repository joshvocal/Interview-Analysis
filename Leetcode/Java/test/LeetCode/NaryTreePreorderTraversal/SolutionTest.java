package LeetCode.NaryTreePreorderTraversal;

import Fundamentals.DataStructures.Node;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;

class SolutionTest {

    private Solution solution = new Solution();
    private Node root = new Node();

    @Test
    void testBalancedTree() {
        root = Node.getBalanced3aryTree();

        List<Integer> actual = solution.preorder(root);
        List<Integer> actual2 = solution.preorder2(root);
        List<Integer> actual3 = solution.preorder3(root);
        List<Integer> expected = new ArrayList<>();
        expected.add(1);
        expected.add(2);
        expected.add(5);
        expected.add(6);
        expected.add(7);
        expected.add(3);
        expected.add(8);
        expected.add(9);
        expected.add(10);
        expected.add(4);
        expected.add(11);
        expected.add(12);
        expected.add(13);

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
        assertEquals(expected, actual3);
    }

    @Test
    void testEmptyTree() {
        root = Node.getEmptyNaryTree();

        List<Integer> actual = solution.preorder(root);
        List<Integer> actual2 = solution.preorder2(root);
        List<Integer> actual3 = solution.preorder3(root);
        List<Integer> expected = new ArrayList<>();

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
        assertEquals(expected, actual3);
    }

    @Test
    void testLinkedList() {
        root = Node.getLinkedList();

        List<Integer> actual = solution.preorder(root);
        List<Integer> actual2 = solution.preorder2(root);
        List<Integer> actual3 = solution.preorder3(root);
        List<Integer> expected = new ArrayList<>();
        expected.add(1);
        expected.add(2);
        expected.add(3);

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
        assertEquals(expected, actual3);
    }
}