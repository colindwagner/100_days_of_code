
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 0 gives you a leap year
div4 = year % 4

# 0 doesn't give you a leap year
div100 = year % 100

# 0 gives you a leap year
div400 = year % 400

if div4 == 0:
    if div100 == 0:
        if div400 == 0:
            print("Leap Year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
