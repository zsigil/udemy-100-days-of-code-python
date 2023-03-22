import random
import pandas

#! LIST COMPREHENSIONS
numbers = [1,2,3]

increased_numbers = [n+1 for n in numbers]

print(increased_numbers)

#works with other iterables : list, tuple, range, string
name = "Angela"
letters = [letter for letter in name]
print(letters)

doubled_numbers = [x*2 for x in range(1,10)]
print(doubled_numbers)

# conditional list comprehension
# eg only double even numbers 
doubled_even_numbers = [x*2 for x in range(1,10) if x%2==0]
print(doubled_even_numbers)


#! DICTIONARY COMPREHENSIONS
names = ["Alex", "John", "Eleanor", "Dave", "Susan", "Freddie"]

students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

students_passed = {student:score for student,score in students_scores.items() if score>60}
print(students_passed)


#! loop through pandas dataframe
student_dict = {
    "students":  ["Alex", "John", "Eleanor", "Dave", "Susan", "Freddie"],
    "scores": [34, 45, 21, 87, 66, 94]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for student, score in student_data_frame.items():
    print(student)


#! BUILT-IN PANDA : iterating through rows
for index,row in student_data_frame.iterrows():
    print(row.students)


