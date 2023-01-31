#RANDOMIZATION AND LISTS

import random
import my_module

random_integer = random.randint(0,10)
print(random_integer)
print(my_module.pi)

#0.000000000000-0.9999999999999999999
random_float = random.random() # 0.0<=x<1


#! COIN TOSS

coin = random.randint(0,1)

if coin==0:
    print("Tails")
else:
    print('Heads')


#! LISTS

fruits = ["apple", "pear", "orange"]
first_fruit = fruits[0]

fruits[1] = "banana"
fruits.append("coconut")


#! bankers' roulette
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# print(names)

random_index = random.randint(0, len(names)-1) #randint includes both
unlucky_guy = names[random_index] # random.choice(names)

print(f"{unlucky_guy} is going to buy the meal today!")

#! nested lists

vegetables = ["potato", "spinach"]
dirty_dozen = [fruits, vegetables]
all_stuff_in_one = [*fruits, *vegetables]

print(dirty_dozen)
print(all_stuff_in_one)


# treasure map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

col = int(position[0])-1
row = int(position[1])-1
map[row][col] = 'X'

# print(f"{row1}\n{row2}\n{row3}")