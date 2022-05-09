import pandas as pd

data = pd.read_csv("weather_data.csv")
temp = data["temp"]

data_dict = data.to_dict()
print(data_dict)


print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
print(data.condition)

#get data in row
print(data[data["day"] == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)


#get mondays temp and convert to F
monday = data[data.day == "Monday"]

monday_f = (monday.temp * 9/5) +32
print(monday_f)

#create df from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("newdata.csv")
