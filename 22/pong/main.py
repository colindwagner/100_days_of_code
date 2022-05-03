from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

#left_paddle = Paddle()
#right_paddle = Paddle()
#scoreboard = Scoreboard()

right_paddle = Turtle("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

left_paddle = Turtle("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

screen.listen()

screen.onkey("w")
screen.onkey("s")

screen.onkey("up")
screen.onkey("down")




screen.exitonclick()
