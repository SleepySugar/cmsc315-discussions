# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.

## Implementation

### Graph Creation

I created a graph using an adjacency list where each node represents a video game and the connections represent games with similar genres or player interests. The graph initially contained eight games with multiple connections between them.

### BFS Traversal

I implemented BFS using a deque as a queue and a set to keep track of visited nodes. The starting node was added to the queue first, and each node's unvisited neighbors were added as the traversal continued. This allowed the graph to be visited level by level instead of following one path as far as possible.

Starting from Minecraft, the BFS traversal was:

['Minecraft', 'Terraria', 'Stardew Valley', 'Elden Ring',
'Animal Crossing', 'Dark Souls', 'Skyrim', 'The Sims']

I then added Hades as a new node connected to Elden Ring and Dark Souls. The updated traversal included the new node and demonstrated how adding a connection can change the traversal.

### Edge Cases

I tested starting from a different node, using a missing starting node, and using an empty graph. Starting from Animal Crossing produced a different traversal order because BFS began from a different location in the graph.

When the starting node did not exist, the function returned an empty list instead of causing an error. An empty graph also returned an empty list because there were no nodes to visit.

### BFS and DFS

BFS uses a queue to visit nearby nodes before moving farther through the graph. DFS uses a stack or recursion and explores one path as deeply as possible before going back to another branch.

BFS can be useful when finding the shortest path in an unweighted graph or when looking for connections close to a starting point. DFS can be more useful when the goal is to explore deeper paths, such as navigating through a directory structure or finding connected paths in a graph. The better choice depends on what the program needs to find and how the graph is organized.

### Real-World Graph Example

A video game recommendation system can represent games as nodes and connect games that have similar genres, ratings, or player interests. BFS could start with a game a user already enjoys and find other games through nearby connections. This could help a recommendation system find content that is closely related to the user's interests before exploring connections that are farther away.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

