from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle():
    def __init__(self):
        self.create_paddle()
        
    def create_paddle(self):
        paddle = Turtle("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(paddle.xcor, paddle.ycor)
