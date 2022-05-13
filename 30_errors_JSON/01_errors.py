# #filenotfound
#     with open("afile.txt") as file:
#         file.read()

# #key error
# a_dict = {"key": "value"}
# value = a_dict["none"]

# #index error
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit_list[3]

# type error
# tet = "abc"
# print(tet + 3)


#we can catch exeptions for programs can't fail

# try:
#     #something that may cause an exeption
# except:
#     #do this is there was an exception
# else:
#     #do this is there were no exeptions
# finally:
    #finally, do this no matter what happens


try:
    file = open("afile.txt")
    adict = {"key": "value"}
    print(adict["asdasd"])
except FileNotFoundError:
    file = open("afile.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(error_message)
else:
    content = file.read()
    print(content)
finally:
    print("i like turtles")
    file.close()
    #can raise my own errors
    #raise KeyError
    raise TypeError("i madethis up")
