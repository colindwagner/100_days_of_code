import pandas as pd

#Fur Color count

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#squirrel_count = pandas.DataFrame(data)

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon","Black"],
    "Count": [gray, cinnamon, black]

}

new_data = pd.DataFrame(data_dict)
print(new_data)