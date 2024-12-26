import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_alphabet)

word = input("Enter a word: ").upper()
nato_word = [nato_alphabet[letter] for letter in word]

print(nato_word)