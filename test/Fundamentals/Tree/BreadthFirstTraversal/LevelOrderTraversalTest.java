package Fundamentals.Tree.BreadthFirstTraversal;

import Fundamentals.DataStructures.TreeNode;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class LevelOrderTraversalTest {

    private LevelOrderTraversal levelOrderTraversal = new LevelOrderTraversal();
    private TreeNode root = new TreeNode();

    @Test
    public void testBalancedTree() {
        root = TreeNode.getBalancedTree();

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>());
        expected.get(0).add(1);
        expected.add(new ArrayList<>());
        expected.get(1).add(2);
        expected.get(1).add(3);
        expected.add(new ArrayList<>());
        expected.get(2).add(4);
        expected.get(2).add(5);
        expected.get(2).add(6);
        expected.get(2).add(7);

        List<List<Integer>> actual = levelOrderTraversal.levelOrderTraversal(root);

        assertEquals(expected, actual);
    }

    @Test
    public void testNullTree() {
        List<List<Integer>> expected = new ArrayList<>();
        List<List<Integer>> actual = levelOrderTraversal.levelOrderTraversal(null);

        assertEquals(expected, actual);
    }

    @Test
    public void testLinkedList() {
        root = TreeNode.getLinkedList();

        List<List<Integer>> expected = new ArrayList<>();
        expected.add(new ArrayList<>());
        expected.get(0).add(1);
        expected.add(new ArrayList<>());
        expected.get(1).add(2);
        expected.add(new ArrayList<>());
        expected.get(2).add(3);
        expected.add(new ArrayList<>());
        expected.get(3).add(4);
        expected.add(new ArrayList<>());
        expected.get(4).add(5);
        expected.add(new ArrayList<>());
        expected.get(5).add(6);
        expected.add(new ArrayList<>());
        expected.get(6).add(7);

        List<List<Integer>> actual = levelOrderTraversal.levelOrderTraversal(root);

        assertEquals(actual, expected);
    }

}