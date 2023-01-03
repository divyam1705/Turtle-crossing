COLORS = ["red", "orange", "yellow", "green", "blue", "purple","cyan","violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
from random import randint
class CarManager:
    def __init__(self):
        self.cars=[]
        for i in range (0,200):
            newcar=Turtle()
            newcar.color(COLORS[randint(0,5)])
            newcar.pu()
            newcar.goto(280+randint(0,10000),randint(-260,280))
            newcar.setheading(180)
            newcar.shape("square")
            newcar.shapesize(1,2)
            self.cars.append(newcar)
    def movecars(self):
        for i in self.cars:
            i.fd(10)




