import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1=Player()
screen.listen()
screen.onkey(player1.up,"Up")
carsman=CarManager()
sb1=Scoreboard()
game_is_on = True
x=0.1
while game_is_on:
    time.sleep(x)
    screen.update()
    carsman.movecars()
    if player1.wincheck():
        sb1.level+=1
        sb1.updatelevel()
        player1.goto(0,-280)
        x/=1.5
    for i in carsman.cars:
        if i.position()[1]-player1.position()[1]<19 and i.distance(player1)<19:
            game_is_on=False
        elif -i.position()[0]+player1.position()[0]<19 and i.distance(player1)<19:
            game_is_on = False
screen.exitonclick()