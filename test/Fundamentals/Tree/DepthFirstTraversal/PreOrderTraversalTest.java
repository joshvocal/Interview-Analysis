package Fundamentals.Tree.DepthFirstTraversal;

import Fundamentals.DataStructures.TreeNode;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class PreOrderTraversalTest {

    private PreOrderTraversal preOrderTraversal = new PreOrderTraversal();
    private TreeNode root = new TreeNode();

    @Test
    public void testBalancedTreeRecursive() {
        root = TreeNode.getBalancedTree();

        List<Integer> actual = preOrderTraversal.preOrderTraversalRecursive(root, new ArrayList<>());

        List<Integer> expected = new ArrayList<>();
        expected.add(1);
        expected.add(2);
        expected.add(4);
        expected.add(5);
        expected.add(3);
        expected.add(6);
        expected.add(7);

        assertEquals(actual, expected);
    }

    @Test
    public void testBalancedTreeIterative() {
        root = TreeNode.getBalancedTree();

        List<Integer> actual = preOrderTraversal.preOrderTraversalIterative(root, new ArrayList<>());

        List<Integer> expected = new ArrayList<>();
        expected.add(1);
        expected.add(2);
        expected.add(4);
        expected.add(5);
        expected.add(3);
        expected.add(6);
        expected.add(7);

        assertEquals(actual, expected);
    }

    @Test
    public void testEmptyTreeRecursive() {
        root = TreeNode.getEmptyTree();

        List<Integer> actual = preOrderTraversal.preOrderTraversalRecursive(root, new ArrayList<>());

        List<Integer> expected = new ArrayList<>();

        assertEquals(actual, expected);
    }

    @Test
    public void testEmptyTreeIterative() {
        root = TreeNode.getEmptyTree();

        List<Integer> actual = preOrderTraversal.preOrderTraversalRecursive(root, new ArrayList<>());

        List<Integer> expected = new ArrayList<>();

        assertEquals(actual, expected);
    }

    @Test
    public void testLinkedListRecursive() {
        root = TreeNode.getLinkedList();

        List<Integer> actual = preOrderTraversal.preOrderTraversalRecursive(root, new ArrayList<>());
        List<Integer> expected = new ArrayList<>();
        expected.add(1);
        expected.add(2);
        expected.add(3);
        expected.add(4);
        expected.add(5);
        expected.add(6);
        expected.add(7);

        assertEquals(actual, expected);
    }

    @Test
    public void testLinkedListIterative() {
        root = TreeNode.getLinkedList();

        List<Integer> actual = preOrderTraversal.preOrderTraversalRecursive(root, new ArrayList<>());
        List<Integer> expected = new ArrayList<>();
        expected.add(1);
        expected.add(2);
        expected.add(3);
        expected.add(4);
        expected.add(5);
        expected.add(6);
        expected.add(7);

        assertEquals(actual, expected);
    }
}