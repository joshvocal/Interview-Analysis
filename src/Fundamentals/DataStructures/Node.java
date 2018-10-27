package Fundamentals.DataStructures;

import java.util.ArrayList;
import java.util.List;

public class Node {

    public int val;
    public List<Node> children;

    public Node() {
    }

    public Node(int val, List<Node> children) {
        this.val = val;
        this.children = children;
    }

    public static Node getBalanced3aryTree() {
        // Level 0
        Node root = new Node(1, new ArrayList<>());

        // Level 1
        root.children.add(new Node(2, new ArrayList<>()));
        root.children.add(new Node(3, new ArrayList<>()));
        root.children.add(new Node(4, new ArrayList<>()));

        // Level 2
        root.children.get(0)
                .children.add(new Node(5, new ArrayList<>()));
        root.children.get(0)
                .children.add(new Node(6, new ArrayList<>()));

        root.children.get(1)
                .children.add(new Node(7, new ArrayList<>()));
        root.children.get(1)
                .children.add(new Node(8, new ArrayList<>()));
        root.children.get(1)
                .children.add(new Node(9, new ArrayList<>()));

        root.children.get(2)
                .children.add(new Node(10, new ArrayList<>()));
        root.children.get(2)
                .children.add(new Node(11, new ArrayList<>()));
        root.children.get(2)
                .children.add(new Node(12, new ArrayList<>()));

        return root;
    }

    public static Node getEmptyNaryTree() {
        Node root = null;

        return root;
    }

    public static Node getLinkedList() {
        // Level 0
        Node root = new Node(1, new ArrayList<>());

        // Level 1
        root.children.add(new Node(2, new ArrayList<>()));

        // Level 2
        root.children.get(0).children.add(new Node(3, new ArrayList<>()));

        return root;
    }
}
