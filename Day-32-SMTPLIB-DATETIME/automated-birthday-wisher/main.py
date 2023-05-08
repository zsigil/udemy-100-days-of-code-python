##################### Extra Hard Starting Project ######################

import random
import datetime as dt
import csv


def sendletter(letter, user):
    print('email:', user[1])
    print(letter)

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv


# read csv into file

birthdays = []

with open('birthdays.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)

    for row in reader:
        if not reader.line_num == 1:
            birthdays.append(row)

today_month = dt.datetime.now().month
today_day = dt.datetime.now().day

birthday_today = []

for bday in birthdays:
    if int(bday[3]) == today_month and int(bday[4]) == today_day:
        birthday_today.append(bday)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# if today's birthday list is not empty
if birthday_today:
    for bd in birthday_today:
        # pick random letter
        letter_num = random.randint(1, 3)

        with open(f"letter_templates/letter_{letter_num}.txt", 'r', encoding='utf-8') as f:
            contents = f.read()
            letter = contents.replace('[NAME]', bd[0])

        # 4. Send the letter generated in step 3 to that person's email address.
        sendletter(letter, bd)
