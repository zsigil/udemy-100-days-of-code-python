import pandas

data = pandas.read_csv('weather_data.csv')
print(type(data))  #DataFrame ~ eg a full excel sheet
print(type(data["temp"])) #Series ~ list / column

data_dict = data.to_dict()
print(data_dict)

#! GET COLUMNS

data_temp_list = data["temp"].to_list()
print(data_temp_list)

# average_temp = sum(data_temp_list)/len(data_temp_list)
average_temp = data["temp"].mean()
print(average_temp)

# max_temp = data["temp"].max()
max_temp = data.temp.max()
print(max_temp)


#! GET ROWS
print(data[data.day == "Monday"])

#day with highest temp
print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
print(monday.condition)
monday_fahrenheit = int(monday.temp) * 9/5+32
print(monday_fahrenheit) 


#! create a dataframe from scratch

my_data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores":[56, 42, 78]
}

new_data = pandas.DataFrame(my_data_dict)
new_data.to_csv('new_data.csv')
print(new_data)
