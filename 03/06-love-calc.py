# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.upper()
name2 = name2.upper()
combined_names = name1 + name2
print(combined_names)

t = combined_names.count('T')
r = combined_names.count('R')
u = combined_names.count('U')
e = combined_names.count('E')
count_true = t + r + u + e

l = combined_names.count('L')
o = combined_names.count('O')
v = combined_names.count('V')
e = combined_names.count('E')
count_love = l + o + v + e

score = int(str(count_true) + str(count_love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")