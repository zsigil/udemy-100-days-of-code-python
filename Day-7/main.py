#Hangman

import random
import os

import hangman_words


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

stages.reverse() # we need them backwards

chosen_word = random.choice(hangman_words.word_list)
bad_guesses = 0
used_letters = []

display = []
for _ in chosen_word:
    display += "_"


while '_' in display and bad_guesses<6:
    os.system('CLS')
    print(logo)
    print(stages[bad_guesses])
    print()
    print(" ".join(display), '\n')
    print(used_letters, '\n')

    guess = input("Guess a letter: ").lower()
    if guess in used_letters:
        print(f"You already guessed {guess}.")
        input("press enter to continue")
        continue
    
    used_letters += guess
    if guess not in chosen_word:
        bad_guesses +=1
        print(stages[bad_guesses])
    else:
        for (i, letter) in enumerate(chosen_word):
            if letter == guess:
                display[i] = letter

print(" ".join(display))

if bad_guesses == 6:
    print('You lose')
    print(chosen_word)
else: 
    print("Congrats, you win")