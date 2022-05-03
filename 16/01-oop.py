#object oriented programming

# think of each compenent of the program as what it has and then what it does

#things the object has are variables
is_holding_plate = True
money = 40


#things that it does in functions
def take_payment(amount):
    print("Thankyou")


#we can use classes to make and group objects.

#creating a class and objects
#create car obj from the CarBlueprint Class
#car = CarBlueprint()
# call attributes by car.speed

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("coral")

my_screen = Screen()
print(my_screen.canvheight)

tim.forward(25)
tim.forward(25)
tim.forward(25)
tim.forward(25)

my_screen.exitonclick()

