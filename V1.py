import os
import random
import time
import json

readfile = input("Load File to use: ")


with open(readfile, "r") as f:
    word_pairs = json.load(f)

print(readfile + ' loaded successfully.')
time.sleep(1)

# Game loop
def play_game():
    print("Welcome to the French-German word guessing game!")
    print("Match the French word with its German translation.")
    print("The full French word will be displayed.")

    word_list = list(word_pairs.items())
    random.shuffle(word_list)  
    while True:
        for german_word, french_word in word_list:
            print(f"\nFrench word: {french_word}")
            guess = input("What is the German word? ").lower()

            if guess == german_word.lower():
                print("Correct!")
            else:
                print(f"Incorrect! The correct word is '{german_word}'.")
        
        print("\nAll word pairs have been used. Shuffling and starting over!")
        random.shuffle(word_list)

play_game()
