from turtle import Turtle, Screen

cursor = Turtle()
tom = Turtle()


screen = Screen()
cursor.shape("turtle")
cursor.color("red")


for _ in range(4):
    cursor.forward(100)
    cursor.right(90)

for _ in range(4):
    tom.circle(100,100)

screen.exitonclick()

#can also import modules as
#import turtle as t
#installing modules like pip install heros