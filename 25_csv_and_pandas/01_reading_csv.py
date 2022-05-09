
# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()

import csv
import pandas as pd

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures)

data = pd.read_csv("weather_data.csv")

temp = data["temp"]
print(data)
print(temp)