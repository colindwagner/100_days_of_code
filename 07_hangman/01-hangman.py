
import random

#Step 1 
word_list = ["aardvark", "baboon", "camel"]

#1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#chosen_word = word_list[random.randint(0,len(word_list) -1)]
chosen_word = random.choice(word_list)

#-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Please guess a letter: ").lower()

#-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if guess in chosen_word:
    print("Guess is in chosen word\n")
else:
    print("Guess is NOT chosen word\n")

