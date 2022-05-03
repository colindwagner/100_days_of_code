from turtle import Turtle, Screen

line_cursor = Turtle()
screen = Screen()
unit = 100


def draw_shape(num_sides):
    sides = num_sides
    angle = 360/sides
    for _ in range(sides):
        line_cursor.pendown()
        line_cursor.forward(unit)
        line_cursor.right(angle=angle)
    
for i in range(3,12):
    draw_shape(i)

screen.exitonclick()