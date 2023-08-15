from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=800, height=480)
bet = screen.textinput(title='Make your bet', prompt="Who gonna win? ")
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_axis = [-150, -100, -50, 0, 50, 100, 150]
turtles = []

for i in range(len(y_axis)):
    t1 = Turtle("turtle")
    t1.color(colors[i])
    t1.penup()
    t1.goto(x=-380, y=y_axis[i])
    turtles.append(t1)

if bet:
    race_on = True

while race_on:
    for turtle in turtles:
        turtle.forward(randint(a=0, b=10))
        if turtle.xcor() > 380:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

screen.exitonclick()