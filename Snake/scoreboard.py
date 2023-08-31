from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 12, "normal")
GAME_OVER = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        self.high_score = max(self.high_score, self.score)
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align=ALIGN, font=GAME_OVER)
