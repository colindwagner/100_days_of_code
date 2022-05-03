from turtle import Turtle, position
import random

class Food:

    def __init__(self):
        self.create_food()

    def create_food(self):
        position = (random.randint(-300,300), random.randint(-300,300))
        food = Turtle("square")
        food.color("white")
        food.penup()
        food.goto(position)
