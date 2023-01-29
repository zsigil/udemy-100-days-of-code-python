#Data Types

#String
print("Hello"[0]) #H
print("Hello"[-1]) #o
print("123"+"345") # "123345"

#Integer
print(123+345) #468
print(123_456_789) #123456789

#Float
print(3.456)

#Boolean
print(False)
print(True)

print("*"*40)

num_char = len(input('What is your name? ')) #integer
# print("Your name has " + num_char + "characters") #TypeError

#TYPE CHECKING
print(type(num_char)) #int

#TYPE CONVERSION
print("Your name has " + str(num_char) + " characters")
print("*"*40)

#!CODE CHALLENGE
#!26->2+6->8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(type(two_digit_number)) #str
print(int(two_digit_number[0])+int(two_digit_number[1]))

print("*"*40)

print(-2**2) #-4

#!CODE CHALLENGE
#!BMI calculator

height = float(input("enter your height:"))
weight = float(input("enter your weight:"))
print(int(weight/(height*height)))

print("*"*40)

print(round(8/3,3)) #2.667
print(round(2.51)) #3
print(8//3) #2  floor division

#! F string
score = 17
print(f"your score is {score}")

print("*"*40)

age = int(input("What is your current age? "))

years = 90-age
months = years * 12
weeks = years *52
days = years * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

print("*"*40)

#! DAY 2 project
#! TIP CALCULATOR
print('Welcome to the tip calculator')

total = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10,12, or 15? '))
num_people = int(input('How many people to split the bill? '))

pay_per_person = round((total*(1+tip_percentage/100))/num_people, 2)
pay_per_person_formatted = "{:.2f}".format(pay_per_person)
message = f"Each person should pay: ${pay_per_person_formatted}."
print(message)