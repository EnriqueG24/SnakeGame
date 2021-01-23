from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", False, font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="Center", font=("Arial", 16, "normal"))
