import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Object Creations
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

# Screen listen for key presses
screen.listen()
screen.onkey(fun=player.moveUp, key="Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create cars and make them move
    cars.create_cars()
    cars.move()

    # if player touches any of the cars, end game
    for car in cars.cars:
        if car.distance(player) <= 20:
            scoreboard.gameOver()
            game_is_on = False

    # If player reaches top, reset position and increase speed
    if player.ycor() >= 280:
        player.nextLevel()
        cars.speedUp()
        scoreboard.nextLevel()

screen.exitonclick()
