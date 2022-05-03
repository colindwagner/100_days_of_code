from turtle import Turtle, Screen
import random

line_cursor = Turtle()
screen = Screen()
unit = 100
line_cursor.speed(10)

def draw_circle():
    change_color()
    line_cursor.circle(100)
    chead = line_cursor.heading()
    line_cursor.setheading(chead + 5)
    


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    line_cursor.color(R, G, B)
    
for _ in range(1,361):
    draw_circle()

screen.exitonclick()