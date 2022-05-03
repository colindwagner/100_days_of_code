
# how to listen to keystrokes on the keyboard
# event listeners
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_right():
    tim.right(10)

def move_forward():
    tim.forward(10)

def move_left():
    tim.left(10)

def move_backward():
    tim.backward(10)

def clear():
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=clear)






screen.exitonclick()