#functions with outputs

def format_name(f_name, l_name):
    #print(f_name.lower().capitalize() + " " + l_name.lower().capitalize())
    return (f_name + " " + l_name).title()

print(format_name("anGelA", "yu"))

#!leap year
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

#docstrings : first indentation after function def betwwen triple quotation marks
# 
def is_leap(year):
    """takes a year AD and returns True if it is a leap year otherwise False"""
    
    if year <0:
        return False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month-1]

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)