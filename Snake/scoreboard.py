from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 12, "normal"
GAME_OVER = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGN, font=GAME_OVER)