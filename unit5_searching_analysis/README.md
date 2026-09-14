# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Implementation

### Linear Search

I implemented linear search by checking each value in the list from the beginning until the target was found. If the target was not present, the method returned -1. Linear search has a worst case time complexity of O(n) because it may need to examine every item in the list.

### Binary Search

I implemented binary search using the left, right, and middle positions of the list. The algorithm compared the target to the middle value and eliminated half of the remaining search space after each comparison. Binary search has a time complexity of O(log n), but it required the dataset to already be sorted.

### Small Dataset

I used a small sorted dataset of game IDs:

[101, 205, 310, 415, 520, 625, 730]

Both algorithms successfully found game ID 415 at index 3. I also searched for game ID 500, which was not present, and both algorithms correctly returned -1.

### Large Dataset

I created a sorted dataset containing 10,000 game IDs. I searched for game ID 9876, and both algorithms correctly found it at index 9875.

The large dataset demonstrated why binary search becomes more efficient as the amount of data increases. Linear search may need to check many values before finding a target near the end of a list. Binary search repeatedly divides the search space in half, so it can reach the target with significantly fewer comparisons.

### Edge Cases

I tested an empty list, a single element list, and boundary values.

For the empty list, both searches returned -1 because there was nothing to search. For the single element list [500], both searches correctly returned index 0. I also tested the first and last values of the small dataset. Both algorithms correctly found 101 at index 0 and 730 at index 6.

### Performance Analysis

Linear search was simpler because it did not require the data to be sorted. However, its O(n) time complexity means that the number of comparisons can increase significantly as the dataset grows.

Binary search was more efficient for the sorted datasets because its O(log n) time complexity allowed it to eliminate approximately half of the remaining search space after each comparison. The tradeoff was that the data needed to be sorted before binary search could be used.

### Real-World Search Scenario

I used game IDs as a real world search scenario. A game library could contain thousands of games, and searching through the IDs could become slower with a linear search. If the game IDs were maintained in sorted order, binary search would be a better choice for quickly finding a specific game.

However, linear search could still be more appropriate when the collection was small, unsorted, or only needed to be searched once. Sorting the data first would require additional time and processing, so binary search would not always be worth the preparation cost.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.