package Fundamentals.Tree.DepthFirstTraversal;

import Fundamentals.DataStructures.TreeNode;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class PostOrderTraversalTest {

    private PostOrderTraversal postOrderTraversal = new PostOrderTraversal();
    private TreeNode root = new TreeNode();

    @Test
    void testBalancedTree() {
        root = TreeNode.getBalancedTree();

        List<Integer> actual = postOrderTraversal.postOrderTraversalRecursive(root, new ArrayList<>());
        List<Integer> actual2 = postOrderTraversal.postOrderTraversalIterative(root, new ArrayList<>());

        List<Integer> expected = new ArrayList<>();
        expected.add(4);
        expected.add(5);
        expected.add(2);
        expected.add(6);
        expected.add(7);
        expected.add(3);
        expected.add(1);

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
    }

    @Test
    public void testEmptyTree() {
        root = TreeNode.getEmptyTree();

        List<Integer> actual = postOrderTraversal.postOrderTraversalRecursive(root, new ArrayList<>());
        List<Integer> actual2 = postOrderTraversal.postOrderTraversalIterative(root, new ArrayList<>());

        List<Integer> expected = new ArrayList<>();

        assertEquals(expected, actual);
        assertEquals(expected, actual2);
    }

    @Test
    public void testLinkedList() {
        root = TreeNode.getLinkedList();

        List<Integer> actual = postOrderTraversal.postOrderTraversalRecursive(root, new ArrayList<>());
        List<Integer> actual2 = postOrderTraversal.postOrderTraversalIterative(root, new ArrayList<>());

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