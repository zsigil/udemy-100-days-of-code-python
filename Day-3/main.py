print("Welcome to the rollercoaster!")
height = int(input("Your height in cm? "))

if height>=120:
    print('You can ride')
    bill = 5;
    age = int(input("How old are you? "))
    if age<12:
        print("child ticket is $5.")
    elif age <= 18:
        print("Youth ticket is $8.")
        bill = 8
    elif 45<=age<=55:
        print("Midlife crisis")
        bill = 0
    else:
        print("Adult ticket is $12.")
        bill=12
    
    wants_photo = input("Do you want a photo taken? y/n ")
    if wants_photo == 'y':
        bill += 3

    print(f"You will pay ${bill}")

else:
    print('Sorry, you cannot ride')


#! odd or even?
number = int(input("Which number do you want to check? "))

if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")


#! BMI CALCULATOR 2.0
# bmi = kg/(m^2)
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight/height**2)
bold = '\033[1m'

if bmi<18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5<=bmi<25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25<=bmi<30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30<=bmi<35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")


#!leap year
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


#! PIZZA ORDER
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

#size
if size == 'S':
    bill += 15

elif size == 'M':
    bill += 20

elif size == 'L':
    bill += 25

#pepperoni +2 for small, +3 for m/l
if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

#extra cheese +1 for all sizes
if extra_cheese == 'Y':
    bill += 1


print(f"Your final bill is: ${bill}.")


#! LOVE CALCULATOR

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names =(name1+name2).lower()
true_part = combined_names.count('t') +  combined_names.count('r') +  combined_names.count('u') +  combined_names.count('e') 
love_part = combined_names.count('l') +  combined_names.count('o') +  combined_names.count('v') +  combined_names.count('e') 

percent = int(str(true_part)+str(love_part))

if percent<10 or percent>90:
    print(f"Your score is {percent}, you go together like coke and mentos.")

elif 40<percent<50:
    print(f"Your score is {percent}, you are alright together.")

else:
    print(f"Your score is {percent}.")
