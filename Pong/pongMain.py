from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle()

screen.listen()
screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(key="Down", fun=right_paddle.down)

screen.exitonclick()
