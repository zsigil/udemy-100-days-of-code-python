programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

#retrieving data
print(programming_dictionary["Bug"])

#new entry  - just add with new key
programming_dictionary["Loop"] = "The action of doing something over and over again"

empty_dictionary = {}

#wiping an existing dictionary
#programming_dictionary = {}

#editing - use existing key
programming_dictionary["Loop"] = "new definition of loop"

for key in programming_dictionary:
    print(key) #key
    print(programming_dictionary[key]) #value


#student scores=> student grades
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for name in student_scores:
    grading = ""
    if student_scores[name] > 90:
        grading = "Outstanding"
    elif student_scores[name] > 80:
        grading = "Exceeds Expectations"
    elif student_scores[name] > 70:
        grading = "Acceptable"
    else:
        grading = "Fail"

    student_grades[name] = grading


print(student_grades)

#travel log
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_country)


#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

print(dict[1])