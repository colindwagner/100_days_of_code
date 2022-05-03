total_bill = input("Welcome to the tip calculator.\nWhat was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

percentage = int(percentage) / 100
total_bill = float(total_bill) + (float(total_bill) * percentage)
share = round(total_bill / int(split), 2)

print(f"Each person should pay: ${share}")
