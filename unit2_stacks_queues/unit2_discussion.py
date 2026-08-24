"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # New items are added to the top, so the most recently added item will be the first one removed.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Returning None prevents an error when pop() is called on an empty stack.
        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek lets us view the most recently added value without removing it.
        if self.is_empty():
            return None

        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New items are added to the back, so the first item added will be the first one removed.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Returning None prevents an error when dequeue() is called on an empty queue.
        if self.is_empty():
            return None

        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front lets us view the first waiting value without removing it.
        if self.is_empty():
            return None

        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO: Browser History ===")

    browser_history = Stack()
    browser_history.push("Google")
    browser_history.push("YouTube")
    browser_history.push("GitHub")
    browser_history.push("Canvas")

    print("Added 4 pages to the browser history.")
    print("Top page:", browser_history.peek())

    print("\nLIFO behavior:")
    print("Back button returned to:", browser_history.pop())
    print("Back button returned to:", browser_history.pop())
    print("Back button returned to:", browser_history.pop())
    print("Back button returned to:", browser_history.pop())

    print("\nEmpty stack tests:")
    print("Is the stack empty?", browser_history.is_empty())
    print("Attempting to pop from an empty stack:", browser_history.pop())
    print("Attempting to peek at an empty stack:", browser_history.peek())

    # Test a stack containing only one item.
    single_stack = Stack()
    single_stack.push("Home Page")

    print("\nSingle-item stack test:")
    print("Before removal, is the stack empty?", single_stack.is_empty())
    print("Removed:", single_stack.pop())
    print("After removal, is the stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: Coffee Shop Customers ===")

    coffee_queue = Queue()

    coffee_queue.enqueue("Max")
    coffee_queue.enqueue("Geri")
    coffee_queue.enqueue("Payne")
    coffee_queue.enqueue("Morgan")

    print("Added 4 customers to the coffee shop queue.")
    print("Customer at the front:", coffee_queue.front())

    print("\nFIFO behavior:")
    print("Served customer:", coffee_queue.dequeue())
    print("Served customer:", coffee_queue.dequeue())
    print("Served customer:", coffee_queue.dequeue())
    print("Served customer:", coffee_queue.dequeue())

    print("\nEmpty queue tests:")
    print("Is the queue empty?", coffee_queue.is_empty())
    print("Attempting to dequeue from an empty queue:", coffee_queue.dequeue())
    print("Attempting to view the front of an empty queue:", coffee_queue.front())

    # Test a queue containing only one item.
    single_queue = Queue()
    single_queue.enqueue("Jaime")

    print("\nSingle-item queue test:")
    print("Before removal, is the queue empty?", single_queue.is_empty())
    print("Served:", single_queue.dequeue())
    print("After removal, is the queue empty?", single_queue.is_empty())


if __name__ == "__main__":
    main()