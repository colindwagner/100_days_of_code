# key value pairs, think a table, {Key: Value}

programming_dictionary = {
    "Bug": "An error in a program that keeps it from being run as expected",
    "Function": "A code block",
    "Loop": "Repeatable"
}

print(programming_dictionary["Function"])

#adding new items
programming_dictionary["Looping"] = "I am the looping walrus"

print(programming_dictionary)

#empty dictionary
empty_dictionary = {}

#wipe dict
#programming_dictionary = {}

#edit an item
programming_dictionary["Bug"] = "This is a changed bug"

print(programming_dictionary)


#looping

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict[1] = 4
print(dict)