
# Create a function called greet()
# write 3 print statements inside the function
# call the creet finction and run your code

# def greet():
#     print("Hello")
#     print("My name is Colin")
#     print("How are you??")
# greet()


# def greet_me(name):
#     print("Hello")
#     print(f"My name is {name}")
#     print("How are you??")
#greet_me("Colin")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"Your location is {location}")

greet_with("Colin", "Houston")


#keyword arguments
def my_function(c=3,a=1,b=2):
    print(f"{a},{b},{c}")

my_function()

greet_with(name="Angela",location="london")