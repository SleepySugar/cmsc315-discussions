# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Implementation

### BST Construction

I created a Binary Search Tree using employee ID numbers as a real-world example. The employee IDs used were 1050, 1025, 1075, 1010, 1035, 1060, and 1100. The first value becomes the root of the tree, and each additional value is compared with the current node. Smaller values are placed in the left subtree, while larger values are placed in the right subtree.

The BST structure allows the search area to become smaller after each comparison. When the tree is reasonably balanced, this can make searching more efficient than checking every value in a list.

### Recursive Insertion

The insert() method uses a recursive helper method called _insert_recursive(). When an empty position is found, a new Node is created. The method continues recursively through the left or right subtree until the correct position is found.

I also added handling for duplicate values so that the same employee ID is not inserted into the tree more than once.

### In-Order Traversal

The inorder() method uses _inorder_recursive() to visit the left subtree, the current node, and then the right subtree. In a BST, this produces the values in sorted order.

For my employee ID example, the in-order traversal produced:

[1010, 1025, 1035, 1050, 1060, 1075, 1100]

This demonstrates how the organization of a BST can be used to maintain ordered data.

### Searching

The search() method uses recursion to look for an employee ID. If the value matches the current node, the method returns True. If the value is smaller, it searches the left subtree. If the value is larger, it searches the right subtree.

This can be more efficient than a linear search when the BST is balanced because the search does not need to examine every value. A balanced BST can have an average search time of O(log n), while a linear search takes O(n) in the worst case.

### Edge Cases

I tested an empty BST and a BST containing only one node.

An empty tree returns [] when traversed.
Searching an empty tree returns False.
A single-node tree successfully stores and searches for its only value.

These tests help make sure the program behaves correctly when there are very few or no nodes.

### BST Performance

BST performance depends heavily on the shape of the tree. When values are distributed in a reasonably balanced way, searching and inserting can be approximately O(log n). However, if values are inserted in an order that creates a very unbalanced tree, the BST can become similar to a linked list. In that situation, searching and insertion can become O(n).

Compared with a Python list, a BST can be useful when data needs to remain ordered while values are frequently searched or inserted. A Python list provides fast access by index, but searching for an arbitrary value requires checking elements sequentially. A BST uses its ordering to eliminate parts of the tree from consideration during a search.
## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.