
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
#int
print(day_of_week)

if year == 2022:
    print("woop")


date_of_birth = dt.datetime(year=1990, month=8, day=10, hour=8, minute=10)
print(date_of_birth)