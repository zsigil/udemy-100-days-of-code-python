import random

def guessing_game():
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100, 1 and 100 included.")

    difficulty = input("Choose difficulty: Type 'hard' for hard, 'easy' for easy, any other key to quit.: ")
    guesses = 10

    #hard - 5 guesses
    #easy - 10 guesses
    if difficulty == 'hard':
        guesses = 5
    elif difficulty == 'easy':
        guesses = 10
    else:
        return
    
    secret_number = random.randint(1,100)
    guess = 0

    def game_over():
        if guesses == 0 or guess==secret_number:
            return True
        else:
            return False
    
    def check_number():
        if guess == secret_number:
            return f"You got it, the answer was {secret_number}\n\n"
        elif guesses == 0:
            return f"Sorry, you lost. The number was {secret_number}\n\n"
        elif guess > secret_number:
            return "Too high, guess lower."
        elif guess < secret_number:
            return "Too low, guess higher."

    while not game_over():
        guess = int(input(f"Make a guess ({guesses} guesses left): "))
        guesses -= 1
        print(check_number())
    
    guessing_game()


guessing_game()
