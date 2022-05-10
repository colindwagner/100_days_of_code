#functions with arguments that have defaults values

#b and c have defaults values, a is required
from ast import arg
from webbrowser import get


def my_function(a, b=4, c=6):
    pass

#unlimited positional arguments
#*args is arguments unlimited arguments, the * means any number, it returns a tuple of values
def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(4,5,6,7,8,9,10,500))


#unlimited keyword arguments
#kwars is basically a dict of values passed to it
def calculate(n, **kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=2, multiply=5)


# we can create our own kwargs class
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

        #if the make is not specificed, this get will not error out the program.
        #self.make = kwargs.get["make"]

my_car = Car(make="Ford", model="Pinto")
print(my_car.model)