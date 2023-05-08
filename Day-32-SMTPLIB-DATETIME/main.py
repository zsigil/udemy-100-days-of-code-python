# import smtplib

# from secret import emailinfo

# # WILL NOT WORK BECAUSE OF EMAIL SECURITY

# # connection = smtplib.SMTP('smtp.freemail.hu')
# # # secure connection
# # connection.starttls()
# # connection.login(user=emailinfo.EMAIL1, password=emailinfo.PASSWORD)
# # connection.sendmail(from_addr=emailinfo.EMAIL1,
# #                     to_addrs=emailinfo.EMAIL2, msg='Hello')
# # connection.close()

import datetime as dt
import random

now = dt.datetime.now()
year = now.year
print(year)

date_of_birth = dt.datetime(year=1981, month=7, day=10)
print(date_of_birth)


# send a motivational quote on Monday

# read quotes into list, and pick one

with open('quotes.txt', 'r', encoding='utf-8') as f:
    quotes = f.readlines()

daily_quote = random.choice(quotes)

today = dt.datetime.now().strftime('%A')

if today == 'Monday':
    # eg. send email
    print(daily_quote)
