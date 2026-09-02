# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Implementation

### Insertion

I used Python's insert() method to add values to a task list. I tested inserting items at the beginning, middle, and end of the list. When an item is inserted near the beginning or middle, the existing elements after that position have to shift to the right. This can make insertion slower as the list gets larger. Inserting at the end requires less shifting.

The real-world scenario I used for the list was a to-do list, with tasks such as studying, exercising, doing laundry, grocery shopping, and homework.

### Deletion

I created a delete_at() function that removes and returns a value at a specific index. Before deleting, the function checks whether the index is valid. If the index does not exist, the function returns None instead of causing an IndexError.

When an item is removed from the beginning or middle of a Python list, the elements after it shift one position to the left. Removing the last item does not require the other elements to shift.

### Searching

I created a search_value() function that searches through the list one value at a time. This is a linear search because the function checks the elements sequentially until it finds the requested value or reaches the end of the list.

If the value is found, the function returns its index. If it is not found, the function returns -1.

### Edge Cases

I tested several edge cases to make sure the functions handled unexpected situations safely.

- Attempting to delete an invalid index returned None.
- Inserting a value into an empty list successfully added the value at index 0.
- Searching for a value that did not exist returned -1.

These tests helped verify that the program could handle situations where the list was empty or the requested value or index was not available.

### List Performance

Python lists are array-based structures that provide fast access to elements by index. However, inserting or deleting values near the beginning or middle can require other elements to be shifted, resulting in O(n) time in those cases. Searching for a value is also O(n) because the list may need to be scanned from beginning to end.

A linked list can be more efficient for frequent insertions or deletions when the location of the node is already known because the surrounding nodes can be updated without shifting other elements. However, linked lists are slower for direct access by index because the nodes must be followed sequentially.

For my to-do list example, a Python list works well because I may want quick access to tasks by index and the list is not expected to require constant insertions or deletions in the middle.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?
