from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_cars(self):
        random_choice = randint(1, 6)
        if random_choice == 1:
            car = Turtle("square")
            car.color(choice(COLORS))
            car.shapesize(stretch_len=2)
            car.penup()
            car.setheading(180)
            car.goto(x=320, y=randint(-250, 250))
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_speed)

    def speedUp(self):
        self.move_speed += MOVE_INCREMENT
