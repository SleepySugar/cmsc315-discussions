# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Implementation

### Creating and Populating the Dictionary

I created an empty Python dictionary called game_library and added seven game IDs and their corresponding game titles. The game ID is used as the key and the game title is stored as the value. Python dictionaries use hash tables internally, which allows keys to be hashed so their associated values can be stored and retrieved efficiently.

The games used in the dictionary were Minecraft, League of Legends, Red Dead Redemption 2, Overwatch, Resident Evil Village, Animal Crossing: New Horizons, and Elden Ring.

### Lookup Operations

I used two existing game IDs to demonstrate successful lookups. Game ID 310 returned Red Dead Redemption 2, and game ID 520 returned Resident Evil Village. A dictionary can use the key to efficiently locate its associated value instead of searching through every entry.

### Update Operations

I updated the value associated with game ID 415 from Overwatch to Overwatch 2. Assigning a new value to an existing key replaces the previous value while keeping the same key.

### Delete Operations

I deleted game ID 625, which removed Animal Crossing: New Horizons from the dictionary. The program displayed the dictionary before and after the deletion to show that the key-value pair was removed.

### Edge Cases

I tested two edge cases involving missing game IDs. First, I used get() to look up game ID 999, which returned None because the key did not exist. Using get() allowed the program to handle the missing key without causing an error.

Second, I attempted to delete game ID 888. The program first checked whether the key existed before trying to delete it. Since the key was not found, the program displayed a message instead of causing an error.

### Real-World Scenario

The dictionary represents a video game library where each game has a unique ID. A game library could use this type of key-value structure to quickly find information about a game when a user provides its ID. This demonstrates how hash tables can be useful for applications that frequently store and retrieve information using unique keys.

### Hashing and Collisions

A hash table uses a hash function to determine where a key should be stored. A collision occurs when two different keys produce the same hash location. A collision resolution strategy allows the hash table to store both entries and continue retrieving them correctly. If collisions happen frequently, they can increase the amount of work required to find a value and reduce performance. Python handles these hash table operations internally when using dictionaries.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.