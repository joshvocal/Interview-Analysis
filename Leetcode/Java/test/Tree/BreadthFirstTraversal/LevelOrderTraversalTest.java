package Tree.BreadthFirstTraversal;

import Fundamentals.DataStructures.TreeNode;
import Fundamentals.Tree.BreadthFirstTraversal.LevelOrderTraversal;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertEquals;

class LevelOrderTraversalTest {

    private LevelOrderTraversal levelOrderTraversal = new LevelOrderTraversal();
    private TreeNode root = new TreeNode();

    @Test
    public void testBalancedTree() {
        root = TreeNode.getBalancedTree();

        List<List<Integer>> actual = levelOrderTraversal.levelOrderTraversal(root);
        List<List<Integer>> expected = new ArrayList<>();

        // Level 0
        expected.add(new ArrayList<>());
        expected.get(0).add(1);

        // Level 1
        expected.add(new ArrayList<>());
        expected.get(1).add(2);
        expected.get(1).add(3);

        // Level 2
        expected.add(new ArrayList<>());
        expected.get(2).add(4);
        expected.get(2).add(5);
        expected.get(2).add(6);
        expected.get(2).add(7);


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

        List<List<Integer>> actual = levelOrderTraversal.levelOrderTraversal(root);
        List<List<Integer>> expected = new ArrayList<>();

        // Level 0
        expected.add(new ArrayList<>());
        expected.get(0).add(1);

        // Level 1
        expected.add(new ArrayList<>());
        expected.get(1).add(2);

        // Level 2
        expected.add(new ArrayList<>());
        expected.get(2).add(3);

        // Level 3
        expected.add(new ArrayList<>());
        expected.get(3).add(4);

        // Level 4
        expected.add(new ArrayList<>());
        expected.get(4).add(5);

        // Level 5
        expected.add(new ArrayList<>());
        expected.get(5).add(6);

        // Level 6
        expected.add(new ArrayList<>());
        expected.get(6).add(7);

        assertEquals(expected, actual);
    }
}