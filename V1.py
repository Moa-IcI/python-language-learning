import os
import random
import time
import json  # Add this to load JSON data

readfile = input("Load File to use: ")

# Open the file and load the dictionary as JSON
with open(readfile, "r") as f:
    word_pairs = json.load(f)  # Assuming the file is in JSON format

print(readfile + ' loaded successfully.')
time.sleep(1)

# Game loop
def play_game():
    print("Welcome to the French-German word guessing game!")
    print("Match the French word with its German translation.")
    print("The full French word will be displayed.")

    # Create a shuffled list of word pairs to avoid repetition
    word_list = list(word_pairs.items())
    random.shuffle(word_list)  # Shuffle the word pairs

    while True:
        # Loop through the shuffled word pairs
        for german_word, french_word in word_list:
            print(f"\nFrench word: {french_word}")
            guess = input("What is the German word? ").lower()

            if guess == german_word.lower():
                print("Correct!")
            else:
                print(f"Incorrect! The correct word is '{german_word}'.")

        # Once all word pairs are exhausted, shuffle them again for variety
        print("\nAll word pairs have been used. Shuffling and starting over!")
        random.shuffle(word_list)

# Run the game
play_game()
