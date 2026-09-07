"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The root is updated with the result of the recursive
        # method so the tree can create its first node or add
        # new values in the correct position.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # When an empty position is reached, create a new node there.
        if node is None:
            return Node(value)

        # Smaller values belong in the left subtree.
        # Larger values belong in the right subtree.
        # This ordering allows the BST to narrow the search area.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            # Duplicate values are ignored so each employee ID
            # appears only once in the tree.
            return node

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # BST search can skip an entire subtree after each comparison.
        # When the tree is reasonably balanced, this is often faster
        # than checking every value like a linear search.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # If there is no node left to search, the value was not found.
        if node is None:
            return False

        # If the current node contains the value, the search is complete.
        if value == node.value:
            return True

        # If the value is smaller, only search the left subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Otherwise, only search the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        # An empty subtree has nothing to visit.
        if node is None:
            return

        # In-order traversal visits left, current, then right.
        # Because a BST stores smaller values on the left and
        # larger values on the right, this produces sorted output.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Employee IDs are used as the real-world application.
    # The first ID becomes the root, and each additional ID
    # is placed to the left or right based on its value.
    employee_ids = [1050, 1025, 1075, 1010, 1035, 1060, 1100]

    employee_bst = BST()

    for employee_id in employee_ids:
        employee_bst.insert(employee_id)

    print("Employee IDs inserted:", employee_ids)

    # Each comparison tells the BST whether to continue searching
    # in the left or right subtree, reducing the number of values
    # that need to be considered at each step when the tree is balanced.


    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    traversal = employee_bst.inorder()
    print("In-order traversal:", traversal)

    # In-order traversal visits the left subtree, the current node,
    # and then the right subtree. Since smaller employee IDs are on
    # the left and larger IDs are on the right, the result is sorted.


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # These employee IDs exist in the tree, so the search should return True.
    existing_ids = [1050, 1060]

    for employee_id in existing_ids:
        print(f"Searching for employee ID {employee_id}: "
              f"{employee_bst.search(employee_id)}")

    # These employee IDs were not inserted, so the search should return False.
    missing_ids = [1000, 1080]

    for employee_id in missing_ids:
        print(f"Searching for employee ID {employee_id}: "
              f"{employee_bst.search(employee_id)}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # An empty tree should safely return an empty list when traversed
    # and False when searching because it contains no nodes.
    empty_bst = BST()

    print("In-order traversal of empty tree:", empty_bst.inorder())
    print("Searching empty tree for 1050:", empty_bst.search(1050))

    # A tree containing only one node is another boundary case.
    # The single value becomes the root with no children.
    single_node_bst = BST()
    single_node_bst.insert(1001)

    print("Single-node tree traversal:", single_node_bst.inorder())
    print("Searching single-node tree for 1001:",
          single_node_bst.search(1001))



if __name__ == "__main__":
    main()