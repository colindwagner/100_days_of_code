from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball_speed = 0.1

scoreboard = Scoreboard()

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()

screen.listen()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -360:
        ball.bounce_x()
        ball_speed = ball_speed * .9

    #detect if passle misses
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()
        ball_speed = .1
    if ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.r_point()
        ball_speed = .1

screen.exitonclick()
