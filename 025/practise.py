import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(len(data[data["Primary Fur Color"] == "Gray"]))
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
#print(len(data[data["Primary Fur Color"] == "Cinnamon"]))
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
#print(len(data[data["Primary Fur Color"] == "Black"]))
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#print(gray_squirrels_count, red_squirrels_count, black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")