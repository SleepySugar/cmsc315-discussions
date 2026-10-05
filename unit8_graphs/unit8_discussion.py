"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # A queue is used so nodes are visited in the order they
    # were discovered, allowing BFS to move level by level.
    if start not in graph:
        return []

    queue = deque([start])
    visited = {start}
    traversal_order = []

    while queue:
        current = queue.popleft()
        traversal_order.append(current)

        # Neighbors are added to the queue so they can be visited
        # after the other nodes at the current level.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Unlike depth-first traversal, BFS finishes the closest
    # neighbors before moving to nodes farther away.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")

    # Each game is a node, and an edge connects games
    # with similar genres or player interests.
    game_graph = {
        "Minecraft": ["Terraria", "Stardew Valley"],
        "Terraria": ["Minecraft", "Stardew Valley", "Elden Ring"],
        "Stardew Valley": ["Minecraft", "Terraria", "Animal Crossing"],
        "Elden Ring": ["Terraria", "Dark Souls", "Skyrim"],
        "Animal Crossing": ["Stardew Valley", "The Sims"],
        "Dark Souls": ["Elden Ring", "Skyrim"],
        "Skyrim": ["Elden Ring", "Dark Souls", "The Sims"],
        "The Sims": ["Animal Crossing", "Skyrim"]
    }

    print("Video game recommendation graph:")
    for game, connections in game_graph.items():
        print(f"{game}: {connections}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    start_game = "Minecraft"
    traversal = bfs(game_graph, start_game)

    print(f"Starting game: {start_game}")
    print(f"BFS traversal: {traversal}")

    # Add a new game connection to demonstrate how the graph
    # and traversal can change when another node is added.
    game_graph["Hades"] = ["Elden Ring", "Dark Souls"]
    game_graph["Elden Ring"].append("Hades")

    print("\nAfter adding Hades:")
    print(f"Elden Ring connections: {game_graph['Elden Ring']}")

    updated_traversal = bfs(game_graph, start_game)
    print(f"Updated BFS traversal: {updated_traversal}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Starting from a different node.
    different_start = "Animal Crossing"
    different_traversal = bfs(game_graph, different_start)

    print(f"Starting from {different_start}:")
    print(different_traversal)
    print("The traversal order changes because BFS begins from a different node.")

    # Edge Case 2: Starting with a node that does not exist.
    missing_start = "Pokemon"
    missing_traversal = bfs(game_graph, missing_start)

    print(f"\nStarting from missing game {missing_start}:")
    print(missing_traversal)
    print("The function returns an empty list instead of causing an error.")

    # Edge Case 3: An empty graph.
    empty_graph = {}
    empty_traversal = bfs(empty_graph, "Minecraft")

    print("\nBFS on an empty graph:")
    print(empty_traversal)
    print("The function returns an empty list because there are no nodes to visit.")



if __name__ == "__main__":
    main()