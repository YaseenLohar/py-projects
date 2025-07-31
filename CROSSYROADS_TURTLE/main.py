import random
import time
import turtle
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#CREATE THE SCREEN
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#CREATE THE PLAYER
tutu= Player()

#CREATE THE SCOREBOARD
scoreboard = Scoreboard()
scoreboard.write(arg = f"LEVEL:{scoreboard.Level}",align = "center", font = ("Courier", 24, "normal"))
scoreboard2=Scoreboard()

#EVENT LISTENERS FOR MOVEMENT
turtle.onkeypress(fun= tutu.move, key = "space")
screen.listen()

#LIST OF Y POSITIONS
pos=[]
for x in range(-240,280,20):
    pos.append(x)

cars=[]  # LIST FOR CAR OBJECTS

#MAIN GAME LOOP
game_is_on = True
while game_is_on:
    rand = random.randint(1, 6) # RANDOM INT FOR CHANCE
    time.sleep(0.1)
    screen.update()
    if rand == 1:                            #GENERATE CARS ONLY IF RAND ==1
        car= CarManager(random.choice(pos))
        cars.append(car)
    for x in cars:
        x.move()
        if tutu.distance(x.tut) < 20:            # GAME OVER TEXT
            scoreboard2.clear()
            scoreboard2.goto(0,0)
            scoreboard2.write(arg="GAME OVER", align="center", font=("Arial", 20, "bold"))
            game_is_on = False
    if tutu.ycor() > 290:        #NEXT LEVEL CHANGES
        scoreboard.clear()
        scoreboard.next_level()
        tutu.goto(0, -280)
        scoreboard.write(arg = f"LEVEL:{scoreboard.Level}",align = "center", font = ("Courier", 24, "normal"))
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT

screen.exitonclick()