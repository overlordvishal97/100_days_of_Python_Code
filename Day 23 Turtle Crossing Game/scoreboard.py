FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_score = 1
        self.penup()
        self.goto(-270, 260)
        self.write(f"Level: {self.level_score}", align="left", font= FONT)
        self.hideturtle()


    def level_up(self):
        self.clear()
        self.level_score += 1
        self.write(f"Level: {self.level_score}", align="left", font= FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align='center',font= FONT )