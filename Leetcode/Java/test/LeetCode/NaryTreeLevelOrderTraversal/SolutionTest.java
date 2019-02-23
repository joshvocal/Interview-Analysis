package LeetCode.NaryTreeLevelOrderTraversal;

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

        List<List<Integer>> actual = solution.levelOrder(root);
        List<List<Integer>> expected = new ArrayList<>();

        List<Integer> levelZero = new ArrayList<>();
        levelZero.add(1);

        List<Integer> levelOne = new ArrayList<>();
        levelOne.add(2);
        levelOne.add(3);
        levelOne.add(4);

        List<Integer> levelTwo = new ArrayList<>();
        levelTwo.add(5);
        levelTwo.add(6);
        levelTwo.add(7);
        levelTwo.add(8);
        levelTwo.add(9);
        levelTwo.add(10);
        levelTwo.add(11);
        levelTwo.add(12);
        levelTwo.add(13);

        expected.add(levelZero);
        expected.add(levelOne);
        expected.add(levelTwo);

        assertEquals(expected, actual);
    }

    @Test
    void testEmptyTree() {
        root = Node.getEmptyNaryTree();

        List<List<Integer>> actual = solution.levelOrder(root);
        List<List<Integer>> expected = new ArrayList<>();

        assertEquals(expected, actual);
    }

    @Test
    void testLinkedList() {
        root = Node.getLinkedList();

        List<List<Integer>> actual = solution.levelOrder(root);
        List<List<Integer>> expected = new ArrayList<>();

        List<Integer> levelZero = new ArrayList<>();
        levelZero.add(1);

        List<Integer> levelOne = new ArrayList<>();
        levelOne.add(2);

        List<Integer> levelTwo = new ArrayList<>();
        levelTwo.add(3);

        expected.add(levelZero);
        expected.add(levelOne);
        expected.add(levelTwo);

        assertEquals(expected, actual);
    }
}