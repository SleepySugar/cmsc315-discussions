# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Implementation

### Bubble Sort

I implemented Bubble Sort by creating a copy of the original list and comparing adjacent values. Values were swapped when they were out of order, and I used a swapped variable so the algorithm could stop early if the list was already sorted.

### Merge Sort

I implemented Merge Sort using recursion and the divide-and-conquer approach. The list was divided into smaller halves where each half was sorted recursively, and then the sorted halves were combined using the merge() function.

The merge() function compared values from each half and built a new sorted list. I used <= when comparing values, so duplicate values could maintain their relative order.

### Datasets

For Dataset #1, I used:

[85, 62, 91, 74, 68, 95, 80, 74]

Both Bubble Sort and Merge Sort produced:

[62, 68, 74, 74, 80, 85, 91, 95]

For Dataset #2, I used:

[100, 45, 72, 88, 45, 63, 30, 99]

Both algorithms produced:

[30, 45, 45, 63, 72, 88, 99, 100]

The program also confirmed that both results matched.

### Edge Cases

I tested an empty list, an already sorted list, and a single-element list. Both algorithms handled these cases correctly. I also included duplicate values in the datasets to make sure repeated values were sorted correctly.

### Performance Analysis

Bubble Sort has a general time complexity of O(n²), while Merge Sort has a time complexity of O(n log n). This means Merge Sort is generally better for larger datasets. Bubble Sort is simpler and can work well for small or nearly sorted lists, especially with the early stopping condition used in my implementation.

Merge Sort uses additional memory while dividing and merging the lists, but its better time complexity makes it more practical for larger amounts of data.

### Real-World Sorting Example

A streaming platform could use sorting to organize movies and shows based on their ratings. The numerical values in my datasets can represent content ratings, with higher numbers representing higher-rated content.

For a large list of movies or shows, Merge Sort could be used to organize the content efficiently from highest rated to lowest rated. A stable sorting process can also help preserve the original order of content that has the same rating. For a small playlist or nearly sorted list, Bubble Sort would also be practical because of its simplicity.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.