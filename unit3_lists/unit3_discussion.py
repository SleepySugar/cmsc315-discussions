"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Insert places the new value at the specified index and shifts
    # existing elements at that position and after it one position to the right.
    # Inserting near the beginning takes more work because more elements
    # may need to be shifted. Inserting at the end is generally more efficient.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validate the index before deleting so the program does not raise an IndexError when an invalid position is provided.
    if index < 0 or index >= len(lst):
        return None

    # Removing an item causes elements after it to shift one position
    # to the left to fill the empty space.
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # A Python list search is a linear search because it checks values
    # sequentially from the beginning until the value is found or the
    # end of the list is reached.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Returning -1 clearly indicates that the value was not found.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Create a list representing tasks in a to-do list.
    tasks = ["Study", "Exercise", "Laundry", "Homework"]
    print("Original task list:", tasks)

    # Insert at the beginning. Existing elements are shifted right.
    insert_at(tasks, 0, "Breakfast")
    print("After inserting at the beginning:", tasks)

    # Insert in the middle. Elements after the index are shifted right.
    insert_at(tasks, 3, "Grocery Shopping")
    print("After inserting in the middle:", tasks)

    # Insert at the end. No existing elements need to be shifted.
    insert_at(tasks, len(tasks), "Relax")
    print("After inserting at the end:", tasks)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Delete from the beginning. The remaining elements shift left.
    removed = delete_at(tasks, 0)
    print("Removed from the beginning:", removed)
    print("Updated task list:", tasks)

    # Delete from the middle. Elements after the deleted item shift left.
    middle_index = len(tasks) // 2
    removed = delete_at(tasks, middle_index)
    print("Removed from the middle:", removed)
    print("Updated task list:", tasks)

    # Delete from the end. No other elements need to be shifted.
    removed = delete_at(tasks, len(tasks) - 1)
    print("Removed from the end:", removed)
    print("Updated task list:", tasks)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a task that still exists in the list.
    search_result = search_value(tasks, "Homework")
    print("Searching for 'Homework': Index", search_result)

    # Search for a task that is not in the list.
    search_result = search_value(tasks, "Work")
    print("Searching for 'Work': Index", search_result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Try to delete using an index that does not exist.
    # The function returns None instead of causing an IndexError.
    invalid_delete = delete_at(tasks, 100)
    print("Attempting to delete index 100:", invalid_delete)

    # Edge case 2: Insert into an empty list.
    # The list should accept the new value at index 0.
    empty_list = []
    insert_at(empty_list, 0, "First Item")
    print("Inserting into an empty list:", empty_list)

    # Edge case 3: Search for a value that does not exist.
    # The function returns -1 when the value cannot be found.
    missing_search = search_value(empty_list, "Missing Item")
    print("Searching for a missing value:", missing_search)




if __name__ == "__main__":
    main()