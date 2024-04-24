# import csv

# with open("D:\Python\Study Project\Reading CSV\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("D:\Python\Study Project\Reading CSV\weather_data.csv")
monday = data[data.day == "Monday"]
celcius = monday.temp
print(celcius * 1.8 + 32)