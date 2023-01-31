rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random 

print('Welcome To The Game.')
move_player = input('What is your move? r/p/s ')

move_computer = random.choice(['r', 's', 'p'])

if(move_player == 'r'):
    print(rock)
elif(move_player == 'p'):
    print(paper)   
elif(move_player == 's'):
    print(scissors)

print('Computer played')

if(move_computer == 'r'):
    print(rock)
elif(move_computer == 'p'):
    print(paper)   
elif(move_computer == 's'):
    print(scissors)


if move_player == move_computer:
    print("It's a draw.")

elif move_player == 'r':
    if move_computer == 's':
        print('You win.')
    else:
        print('Computer wins')

elif move_player == 's':
    if move_computer == 'p':
        print('You win.')
    else:
        print('Computer wins')

elif move_player == 'p':
    if move_computer == 'r':
        print('You win.')
    else:
        print('Computer wins')