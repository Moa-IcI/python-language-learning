import os
import random
import time
import json

readfile = input("Load JSON File to use: ")


with open(readfile, "r") as f:
    word_pairs = json.load(f)

print(readfile + ' loaded successfully.')
time.sleep(1)

# Game loop
def play_game():
    print("Welcome to the Language-to-Language word guessing game!")
    print("Match your languages' word with its translation.")

    word_list = list(word_pairs.items())
    random.shuffle(word_list)  
    while True:
        for language2_word, language1_word in word_list:
            print(f"\nYour word: {language1_word}")
            guess = input("What is the word? ").lower()

            if guess == language2_word.lower():
                print("Correct!")
            else:
                print(f"Incorrect! The correct word is '{language2_word}'.")
        
        print("\nAll word pairs have been used. Shuffling and starting over!")
        random.shuffle(word_list)

play_game()
