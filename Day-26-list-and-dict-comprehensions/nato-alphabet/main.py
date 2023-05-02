import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_alphabet = {row.letter: row.code for index, row in df.iterrows()}

print(nato_alphabet)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    user_input = input("What would you like to translate?: ").upper()

    try:
        phonetic_word = [nato_alphabet[letter] for letter in user_input]
        print(phonetic_word)
        break
    except KeyError:
        print('Sorry, only letters of alphabet.')
