from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.writeScore()

    def writeScore(self):
        self.clear()
        self.goto(x=-200, y=250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def nextLevel(self):
        self.level += 1
        self.writeScore()

    def gameOver(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)
