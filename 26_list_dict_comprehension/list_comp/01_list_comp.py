# new lists from previous lists

#oldway
numbers = [1,2,3]
new_list = []
for number in numbers:
    new_list.append(number + 1)


#new way
#new_list = [new_item for item in list]
numbers = [1,2,3]
new_list = [item+1 for item in numbers]
print(new_list)

name = "Colin"
list = [n for n in name]
print(list)

doubled = [n*2 for n in range(1,5)]
print(doubled)

#conditional list comp
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred"]
names2 = [name for name in names if len(name) < 5 ]
print(names2)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Fred"]
names2 = [name.upper() for name in names if len(name) > 5 ]
print(names2)