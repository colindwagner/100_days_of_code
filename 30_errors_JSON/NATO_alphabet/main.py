import pandas as pd

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(data)
nato_dict = {row.letter:row.code for index,row in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def NATO():
    word = input("Input a word to get phonetic pronounciation: ").upper()

    try:
        word_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters are allowed.")
        NATO()
    else:
        print(word_list)
NATO()