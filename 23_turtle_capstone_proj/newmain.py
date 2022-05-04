import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

initial_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(initial_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

    #winner winner chicken dinner, advance scoreboard and back to finish
    if player.is_finished():
        player.back_to_start()
        scoreboard.upgrade_level()
        initial_speed = initial_speed * .9

screen.exitonclick()

