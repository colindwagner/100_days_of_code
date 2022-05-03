#slicing

piano_keys = ["a","b","c","d","e","f","g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la","ti")

# d e
print(piano_keys[3:5])

#all the way to position 5
print(piano_keys[:5])

#slice in incerement too, every 2nd item
print(piano_keys[2:5:2])
print(piano_keys[::2])

#reverse the list
print(piano_keys[::-1])

#tuple
print(piano_tuple[2:5])
print(piano_tuple[::-1])