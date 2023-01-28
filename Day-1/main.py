print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

print("-"*20+'*'+"-"*20)

print("Hello World\n"*3)

print("-"*20+'*'+"-"*20)

#comment
print("Hello " + input("What is your name? "))

print("-"*20+'*'+"-"*20)

print(len(input("What is your name? ")))

print("-"*20+'*'+"-"*20)

name = input("What is your name? ")
length = len(name)
print(length)

print("-"*20+'*'+"-"*20)

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
a,b = b,a



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

print("-"*20+'*'+"-"*20)

#! DAY 1 PROJECT
#! BAND NAME GENERATOR
print("Welcome to the Band Name Generator")
city = input('What\'s the name of the city you grew up in?\n')
pet = input('What\'s the name of your pet?\n')
print("Your band name could be " + city + " " + pet)