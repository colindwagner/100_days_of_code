def filereader(file):

    with open(file, "r") as file:
        f_read = file.readlines()
        f = [int(i.replace("\n", "")) for i in f_read]
        return f

file1 = filereader("file1.txt")
file2 = filereader("file2.txt")

result = [num for num in file1 if num in file2]

# Write your code above 👆

print(result)
