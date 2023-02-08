def greet():
    print("Hello darling!")
    print("we have a beautiful day today.")
    print("See you later.")

greet()

#parameter: name of the data that is passed in (in the function def)
#argument:actual value (when calling the function)

#function that allows for input 
def greet_with_name(name): 
    print(f"Hello, {name}")

greet_with_name("Angela") 


#Functions with more than one input
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"What is it like in {location}?")

greet_with("Ben", "London") #positional arguments
greet_with(location="Budapest", name="Zsóka") #keyword arguments

#paint area calculator
#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    result = math.ceil(height*width/cover)
    print(f"You'll need {result} cans of paint.")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#! PRIME CHECKER
def prime_checker(number):
    prime = True

    for num in range(2, math.ceil(math.sqrt(number))):
        if number == 2:
            break
        if number % num == 0:
            prime = False
            break
        
    print(f"It's a prime number.") if prime else print(f"It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)