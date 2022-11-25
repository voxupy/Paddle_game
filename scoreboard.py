from turtle import Turtle
FONT = ("Arial", 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.penup()
        self.color("white")
        self.update_scoreboard_l()
        self.update_scoreboard_r()
        self.hideturtle()

    def update_scoreboard_r(self):
        self.goto(40, 250)
        self.write(f"{self.score_r}",align="center",font=FONT)

    def update_scoreboard_l(self):
        self.goto(-40, 250)
        self.write(f"{self.score_l}",align="center",font=FONT)

    def increase_score_l(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard_l()
        self.update_scoreboard_r()

    def increase_score_r(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard_r()
        self.update_scoreboard_l()

