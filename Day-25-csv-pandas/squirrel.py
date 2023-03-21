# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color_list = data["Primary Fur Color"].to_list()

gray = fur_color_list.count('Gray')
cinnamon = fur_color_list.count('Cinnamon')
black = fur_color_list.count('Black')

my_squirrel_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "count": [gray, cinnamon, black]
}

squirrels = pandas.DataFrame(my_squirrel_dict)
squirrels.to_csv('squirrel_count.csv')