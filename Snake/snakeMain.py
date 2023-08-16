from snake import Snake
from turtle import Screen
import time

# Setup window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

# Create Snake object
snake = Snake()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    # Updating the screen so snake moves as one unit
    screen.update()
    time.sleep(0.1)

    # Use Snake Class move method to move snake forward
    snake.move()

screen.exitonclick()
