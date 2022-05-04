

with open("myfile.txt") as file:
    contents = file.read()
    print(contents)

with open("myfile.txt", mode="a") as file:
    file.write("TEXT")

with open("myfile1.txt", mode="w") as file:
    file.write("bleh")
