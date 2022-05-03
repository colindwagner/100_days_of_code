from turtle import Turtle, Screen
import random

line_cursor = Turtle()
screen = Screen()
unit = 100
line_cursor.pensize(width=15)
line_cursor.speed(10)

def draw():
    angles = [0,90,180,270]
    length = random.randint(1,100)
    angle = random.choice(angles)

    line_cursor.pendown()
    change_color()
    line_cursor.forward(length)
    line_cursor.right(angle=angle)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    line_cursor.color(R, G, B)
    
for _ in range(300):
    draw()

screen.exitonclick()