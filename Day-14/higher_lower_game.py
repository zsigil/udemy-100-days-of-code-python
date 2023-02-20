import random
import os

from art import logo, vs
from game_data import data

def print_formatted_stuff(stuff, position):
    text = "Compare A: " if position == "A" else "Against B: "
    print(f'{text}{stuff["name"]}, a(n) {stuff["description"]}, from {stuff["country"]}')


def game():
    score = 0
    lives = 1

    #later on ,the second one will be the first one, will not be random
    compare1 = random.randint(0,len(data)-1)
    
    while lives>0:

        #get random index for comparing data first
        compare2 = random.randint(0,len(data)-1)
        #if they are equal, keep getting another one, till ok
        while compare1==compare2:
            compare2 = random.randint(0,len(data)-1)

        stuff_A = data[compare1]
        stuff_B = data[compare2]

        #print stuff
        print(logo)
        print('\n')
        print_formatted_stuff(stuff_A, "A")
        print(vs)
        print_formatted_stuff(stuff_B, "B")
        guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()


        if guess == 'a' and stuff_A["follower_count"]>=stuff_B["follower_count"]:
            score +=1
            print(f"You are right!. Current score: {score}")
            #save second as first
            compare1 = compare2
        elif guess == 'b' and stuff_A["follower_count"]<=stuff_B["follower_count"]:
            score +=1
            print(f"You are right!. Current score: {score}")
            #save second as first
            compare1 = compare2
        else:
            lives -= 1
            os.system('cls')
            print (logo)
            print(f"Sorry, you are wrong. Final score: {score}")
            should_continue = input("Type 'y' for another game, any other to quit: ")
            if should_continue == 'y':
                os.system('cls')
                game()
        

game()
