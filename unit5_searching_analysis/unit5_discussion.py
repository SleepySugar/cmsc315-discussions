"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Linear search checks each item from the beginning of the list
    # until the target is found or the list ends. In the worst case,
    # every item must be checked, giving it O(n) time complexity.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    # If the loop finishes, the target was not found.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Binary search requires the list to already be sorted.
    # The search starts with the entire list and checks the middle.
    # Each comparison eliminates approximately half of the remaining
    # search space, giving binary search O(log n) time complexity.
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        # If the target is larger, search the right half.
        if target > lst[middle]:
            left = middle + 1

        # If the target is smaller, search the left half.
        else:
            right = middle - 1

    # If the search space becomes empty, the target was not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # The game IDs are sorted so both search algorithms can be tested.
    small_dataset = [101, 205, 310, 415, 520, 625, 730]

    print("Small game ID dataset:", small_dataset)

    # Test a value that exists in the dataset.
    target = 415

    linear_result = linear_search(small_dataset, target)
    binary_result = binary_search(small_dataset, target)

    print(f"Searching for {target}:")
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Test a value that does not exist.
    missing_target = 500

    linear_result = linear_search(small_dataset, missing_target)
    binary_result = binary_search(small_dataset, missing_target)

    print(f"Searching for missing ID {missing_target}:")
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Both algorithms return -1 when the target is not found.
    # Binary search can reach this result using fewer comparisons
    # because it repeatedly eliminates half of the search space.


    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # This creates a sorted dataset containing 10,000 game IDs.
    large_dataset = list(range(1, 10001))

    large_target = 9876

    linear_result = linear_search(large_dataset, large_target)
    binary_result = binary_search(large_dataset, large_target)

    print("Large dataset size:", len(large_dataset))
    print(f"Searching for game ID {large_target}:")
    print("Linear search index:", linear_result)
    print("Binary search index:", binary_result)

    # Linear search may need to check many values before reaching
    # a target near the end of a large dataset. Binary search keeps
    # dividing the search space in half, making it much more efficient
    # as the dataset becomes larger.


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Searching an empty list.
    # Neither algorithm has a value to check, so both return -1.
    empty_list = []

    print("Empty list:")
    print("Linear search:", linear_search(empty_list, 100))
    print("Binary search:", binary_search(empty_list, 100))

    # Edge case 2: Searching a single-element list.
    # Both algorithms should successfully find the only value.
    single_item = [500]

    print("\nSingle-element list:")
    print("Linear search for 500:", linear_search(single_item, 500))
    print("Binary search for 500:", binary_search(single_item, 500))

    # Edge case 3: Searching for the first and last values.
    # These boundary cases confirm that both algorithms correctly
    # handle the beginning and end of the dataset.
    print("\nBoundary values in small dataset:")
    print("First value (101), linear search:",
          linear_search(small_dataset, 101))
    print("First value (101), binary search:",
          binary_search(small_dataset, 101))
    print("Last value (730), linear search:",
          linear_search(small_dataset, 730))
    print("Last value (730), binary search:",
          binary_search(small_dataset, 730))


if __name__ == "__main__":
    main()