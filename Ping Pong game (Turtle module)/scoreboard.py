from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.left_score}", True, align="center", font=('Courier', 60, 'normal'))
        self.goto(100, 200)
        self.write(f"{self.right_score}", True, align="center", font=('Courier', 60, 'normal'))

    def l_score(self):
        self.left_score += 1
        self.update_scoreboard()

    def r_score(self):
        self.right_score += 1
        self.update_scoreboard()
