import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    car_manager.create_car()
    car_manager.move_cars()

    if car_manager.check_touch_cars(player):
        scoreboard.game_over()
        break

    if player.is_at_finish():
        car_manager.level_up()
        scoreboard.add_level()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
