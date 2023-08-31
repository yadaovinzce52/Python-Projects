from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
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
food = Food()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    # Updating the screen so snake moves as one unit
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Snake eats food
    if snake.head.distance(food) < 15:
        food.random_location()
        scoreboard.update_score()
        snake.extend()

    # Collision with wall
    if (snake.head.xcor() > 280 or
            snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or
            snake.head.ycor() < -280):
            scoreboard.reset()
            snake.reset()

    # collision with self
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            game_on = not game_on
            scoreboard.game_over()

screen.exitonclick()
