# with open('weather_data.csv') as fhand:
#     data = fhand.readlines()

import csv

temperatures = []

with open('weather_data.csv') as fhand:
    data = csv.reader(fhand)
    for row in data:
        # print(row)
        try:
            temperatures.append(int(row[1]))
        except:
            pass


# print(temperatures)

#!pandas installed in environment

import pandas

data_pandas = pandas.read_csv('weather_data.csv')
print(data_pandas["temp"])


