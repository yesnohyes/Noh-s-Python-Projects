from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self, level):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(level-1))

    # def level_up(self, level):
    #     for car in self.all_cars:
    #         car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(level-1))

