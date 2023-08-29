from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def moveUp(self):
        self.forward(MOVE_DISTANCE)

    def nextLevel(self):
        self.goto(STARTING_POSITION)
