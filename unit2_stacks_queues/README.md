# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.


## Implementation

### Stack

I created a `Stack` class that used a Python list to store values. I implemented `push()`, `pop()`, `peek()`, and `is_empty()` methods.

The `push()` method added new values to the top of the stack, while `pop()` removed the most recently added value. This demonstrated LIFO (Last In, First Out) behavior.

I used browser history as a real-world example because the most recently visited page is the first page returned to when using the back button.

### Queue

I created a `Queue` class that used `collections.deque` to store values. I implemented `enqueue()`, `dequeue()`, `front()`, and `is_empty()` methods.

The `enqueue()` method added values to the back of the queue, while `dequeue()` removed the value from the front. This demonstrated FIFO (First In, First Out) behavior.

I used a coffee shop line as a real-world example because the first customer to arrive is normally the first customer to be served.

### Edge Cases

I tested empty stacks and queues by calling `pop()`, `peek()`, `dequeue()`, and `front()` when there were no values. These operations returned `None` instead of causing an error.

I also created stack and queue objects containing only one item. After removing the item, I verified that each structure was empty.

### Memory Usage

Both structures used more memory as more values were added. The stack and queue required O(n) space, where `n` represented the number of items stored in the structure.

The stack used a Python list, while the queue used `deque`, which was useful for efficiently adding and removing values from the queue.

## Student-Created Extension

I added browser history and coffee shop customer scenarios to demonstrate how stacks and queues could be used in practical applications. I also added additional edge-case tests beyond the basic demonstrations.