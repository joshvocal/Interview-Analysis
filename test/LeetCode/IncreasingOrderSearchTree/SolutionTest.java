package LeetCode.IncreasingOrderSearchTree;

import Fundamentals.DataStructures.TreeNode;
import Fundamentals.Tree.DepthFirstTraversal.InorderTraversal;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class SolutionTest {

    private Solution solution = new Solution();
    private TreeNode root = new TreeNode();

    @Test
    void testBalancedTree() {
        root = TreeNode.getBalancedTree();

        TreeNode expected = solution.increasingBST(root);
        System.out.println(InorderTraversal.inOrderTraversalRecursive(expected, new ArrayList<>()));
        System.out.println(InorderTraversal.inOrderTraversalRecursive(root, new ArrayList<>()));
    }
}