
# how to listen to keystrokes on the keyboard
# event listeners
from re import T
from turtle import Turtle, Screen, width
import random

race_on = False
screen = Screen()
screen.setup(height=500, width=500)
user_bet = screen.textinput("BET", "Which tutle will win the race?: ")
colors = ["red", "green", "blue", "orange", "yellow"]
y_positions = [200, 100, 0, -100, -200]
all_turtles = []

for i in range(0,5):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-200, y=y_positions[i])
    turtle.speed(random.randint(0,10))
    all_turtles.append(turtle)
    

if user_bet:
    race_on = True

while race_on:
    for t in all_turtles:
        if t.xcor() > 200:
            winner = t.color()
            race_on = False
            if winner[0] == user_bet:
                print("You win!")
            else:
                print("You bet on the wrong turtle")
        random_distance = random.randint(0,10)
        t.forward(random_distance)


screen.exitonclick()





