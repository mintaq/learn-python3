# with open('./weather_data.csv', 'r') as data_file:
#     weather_data = data_file.readlines()
#     print(weather_data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data['temp'].to_list()
# max_temp = data['temp'].max()
# day_has_max_temp = data[data['temp'] == data['temp'].max()]
# print(day_has_max_temp)

# Create a dataframe from scatch
# data_dict = {
#     "students": ['Minh', 'Thu', 'Khiet Anh'],
#     "scores": [77, 88, 99]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("students.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
data_frame = pandas.DataFrame(data_dict).to_csv("squirrel_count.csv")
