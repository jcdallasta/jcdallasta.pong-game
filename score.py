from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def left_wins(self):
        self.clear()
        self.goto(0, 0)
        self.write(f" LEFT PLAYER WINS! \n FINAL SCORE: {self.l_score}-{self.r_score}",
                   align="center", font=("Courier", 25, "normal"))

    def right_wins(self):
        self.clear()
        self.goto(0, 0)
        self.write(f" RIGHT PLAYER WINS! \n FINAL SCORE: {self.l_score}-{self.r_score}",
                   align="center", font=("Courier", 25, "normal"))
