import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            self.cars.append(Turtle("square"))
            self.cars[-1].shapesize(stretch_wid=1, stretch_len=2)
            self.cars[-1].penup()
            self.cars[-1].color(random.choice(COLORS))
            self.cars[-1].goto(300, -300 + random.randint(2, 13) * 40)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.cars_speed)

    def check_touch_cars(self, player) -> bool:
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT
