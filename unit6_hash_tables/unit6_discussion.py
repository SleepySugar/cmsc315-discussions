"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    # A Python dictionary uses a hash table internally to store
    # key-value pairs. The key is hashed so Python can efficiently
    # find the location associated with its value.
    game_library = {}

    game_library[101] = "Minecraft"
    game_library[205] = "League of Legends"
    game_library[310] = "Red Dead Redemption 2"
    game_library[415] = "Overwatch"
    game_library[520] = "Resident Evil Village"
    game_library[625] = "Animal Crossing: New Horizons"
    game_library[730] = "Elden Ring"

    print("\n=== INSERT OPERATIONS ===")
    print("Game library after inserting key-value pairs:")
    print(game_library)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")

    # Looking up a value by its key allows the dictionary to use
    # the key's hash to find the associated value efficiently.
    print("Game ID 310:", game_library[310])
    print("Game ID 520:", game_library[520])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("Before update:", game_library)

    # Assigning a new value to an existing key replaces the old
    # value instead of creating a duplicate key.
    game_library[415] = "Overwatch 2"

    print("After updating game ID 415:", game_library)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("Before deletion:", game_library)

    # Deleting a key removes both the key and its associated value
    # from the dictionary.
    del game_library[625]

    print("After deleting game ID 625:", game_library)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    # Using get() allows the program to safely look up a key that
    # does not exist without causing a KeyError.
    missing_game = game_library.get(999)
    print("Lookup for missing game ID 999:", missing_game)

    # Checking whether a key exists before deleting it prevents
    # the program from raising an error when the key is missing.
    missing_id = 888
    if missing_id in game_library:
        del game_library[missing_id]
        print("Game ID 888 was deleted.")
    else:
        print("Game ID 888 was not found, so nothing was deleted.")

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO ===")
    print("A game library can use game IDs as keys and game titles as values.")
    print("This allows a user to quickly find a game by its unique ID.")
    print("For example, game ID 205 is:", game_library[205])



if __name__ == "__main__":
    main()