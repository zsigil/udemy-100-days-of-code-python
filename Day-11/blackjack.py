import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []

def user_draws():
    new_card = random.choice(cards)
    if new_card == 11 and sum(user_cards)>10:
        new_card = 1
    user_cards.append(new_card)

def computer_draws():
    new_card = random.choice(cards)
    if new_card == 11 and sum(computer_cards)>10:
        new_card = 1
    computer_cards.append(new_card)

def first_draw():
    user_draws()
    user_draws()
    computer_draws()
    print_user()
    print_computer()


def print_user():
    print(f"Your cards: {user_cards}, current score {sum(user_cards)}")


def print_computer():
    if len(computer_cards) == 1:
        print(f"Computer's first card: {computer_cards[0]}")
    else:
        print(f"Computer's cards: {computer_cards}, current computer score {sum(computer_cards)}")


def user_wins():
    if sum(user_cards)<=21 and sum(user_cards)>sum(computer_cards):
        return True
    elif sum(computer_cards)>21 and sum(user_cards)<=21:
        return True
    else:
        return False


def blackjack():
    os.system('cls')
    print(logo)
    user_cards.clear()
    computer_cards.clear()
    
    will_play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    if will_play != 'y':
        print("Goodbye!")
        return

    first_draw()

    while sum(user_cards)<21:
        another_card_question = input("Type 'y' to get another card, 'n' to pass: ")
        if another_card_question == 'y':
             user_draws()
             print_user()
        else:
            while sum(computer_cards)<17:
                computer_draws()
                print_computer()
            break

    if(user_wins()):
        if sum(user_cards)==21 and len(user_cards)==2:
            print("BLACKJACK!")
        else:
            print("You won!")
    else:
        print("you lost :(")

    input()
    
    blackjack()

blackjack()