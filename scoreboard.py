FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(-280,260)
        self.level=0
        self.write(f"Level : {self.level}",font=FONT)
    def updatelevel(self):
        self.clear()
        self.write(f"Level : {self.level}", font=FONT)


