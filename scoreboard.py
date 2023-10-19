from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 250)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
    def increase_score(self):       
        self.score += 10
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)
