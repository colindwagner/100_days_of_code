from turtle import Turtle, Screen

line_cursor = Turtle()


screen = Screen()

for _ in range(100):
    line_cursor.pendown()
    line_cursor.forward(10)
    line_cursor.penup()
    line_cursor.forward(10)

screen.exitonclick()