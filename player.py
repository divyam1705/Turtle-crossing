STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.color("black")
        self.pu()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
    def up(self):
        self.forward(MOVE_DISTANCE)
    def wincheck(self):
        if self.position()[1]>FINISH_LINE_Y:
            return True
        else:
            return False


