from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f" Score: {self.score} High score:{self.high_score}", align="center", font=('Arial', 20, 'normal'))

    def add_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", False, align="center", font=('Arial', 20, 'normal'))