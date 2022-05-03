#Write your code below this row 👇

total = 0
for x in range(1,101):
    if (x % 2) == 0:
        total += x
print(total)

for x in range(2,101,2):
    if (x % 2) == 0:
        total += x
print(total)