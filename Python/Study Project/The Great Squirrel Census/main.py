import pandas

data = pandas.read_csv("D:\\Python\Study Project\\The Great Squirrel Census\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color = {}
# colors = data["Primary Fur Color"]
# print(colors)
# tes = data.to_dict("Primary Fur Color")
# print(tes)
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
Black_squirrels = data[data["Primary Fur Color"] == "Black"]
# color = cinamon_squirrels["Primary Fur Color"].to_dict('r')

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(grey_squirrels), len(cinamon_squirrels), len(Black_squirrels)]
}
# print(grey_squirrels)
df = pandas.DataFrame(data_dict)
df.to_csv("D:\Python\Study Project\The Great Squirrel Census\Squirrel_Count.csv")
# print(Black_squirrels)
# print(len(grey_squirrels))
# print(len(cinamon_squirrels))
# print(len(Black_squirrels))

# pandas.DataFrame