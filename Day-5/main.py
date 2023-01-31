fruits = ["apple", "orange", "banana", "pear"]

for fruit in fruits:
    print(fruit)



#! average height
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

count = 0
sum = 0

for height in student_heights:
   count += 1
   sum += height

average = sum/count

print(round(average))

#! highest score
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score = student_scores[0]

for score in student_scores:
   if score>max_score:
      max_score = score

print(f"The highest score in the class is: {max_score}")

for n in range(1,11,3):
   print(n)

#! adding even numbers from 1-100
total = 0

for n in range(1,101):
   if n%2==0:
      total += n

print(total)

#! FizzBuzz
for n in range(1,101):
    if n%3==0 and n%5==0:
      print('FizzBuzz')
    elif n%3==0:
       print('Fizz')
    elif n%5==0:
       print('Buzz')
    else:
       print(n)


