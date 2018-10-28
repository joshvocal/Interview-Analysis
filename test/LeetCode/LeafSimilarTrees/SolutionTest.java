package LeetCode.LeafSimilarTrees;

import Fundamentals.DataStructures.TreeNode;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    private Solution solution = new Solution();
    private TreeNode root1 = new TreeNode();
    private TreeNode root2 = new TreeNode();

    @Test
    void testEqualTrees() {
        root1 = TreeNode.getBalancedTree();
        root2 = TreeNode.getBalancedTree();

        boolean expected = true;
        boolean actual = solution.leafSimilar(root1, root2);

        assertEquals(expected, actual);
    }

    @Test
    void testEmptyTrees() {
        root1 = TreeNode.getEmptyTree();
        root2 = TreeNode.getEmptyTree();

        boolean expected = true;
        boolean actual = solution.leafSimilar(root1, root2);

        assertEquals(expected, actual);
    }
}