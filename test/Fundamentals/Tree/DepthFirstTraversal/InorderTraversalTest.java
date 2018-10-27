package Fundamentals.Tree.DepthFirstTraversal;

import Fundamentals.DataStructures.TreeNode;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class InorderTraversalTest {

    private InorderTraversal inOrderTraversal = new InorderTraversal();
    private TreeNode root = new TreeNode();

    @Test
    void testBalancedTree() {
        root = TreeNode.getBalancedTree();

        List<Integer> actual = inOrderTraversal.inOrderTraversalRecursive(root, new ArrayList<>());
        List<Integer> actual2 = inOrderTraversal.inOrderTraversalIterative(root, new ArrayList<>());

        List<Integer> expected = new ArrayList<>();
        expected.add(4);
        expected.add(2);
        expected.add(5);
        expected.add(1);
        expected.add(6);
        expected.add(3);
        expected.add(7);

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
    }

    @Test
    void testEmptyTree() {
        root = null;

        List<Integer> actual = inOrderTraversal.inOrderTraversalRecursive(root, new ArrayList<>());
        List<Integer> actual2 = inOrderTraversal.inOrderTraversalIterative(root, new ArrayList<>());
        List<Integer> expected = new ArrayList<>();

        assertEquals(expected, actual2);
    }

    @Test
    void testLinkedList() {
        root = TreeNode.getLinkedList();

        List<Integer> actual = inOrderTraversal.inOrderTraversalRecursive(root, new ArrayList<>());
        List<Integer> actual2 = inOrderTraversal.inOrderTraversalIterative(root, new ArrayList<>());

        List<Integer> expected = new ArrayList<>();
        expected.add(7);
        expected.add(6);
        expected.add(5);
        expected.add(4);
        expected.add(3);
        expected.add(2);
        expected.add(1);

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
    }
}