from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#CARMANAGER CLASS DEFINITION
class CarManager:
    def __init__(self,y):
        super().__init__()
        self.tut = Turtle()
        self.tut.setheading(180)
        self.tut.shape("square")
        self.tut.penup()
        self.tut.color(random.choice(COLORS))
        self.tut.shapesize(stretch_len=2,stretch_wid=1)
        self.tut.goto(310,y)
        self.tut.xcor = self.tut.position()[0]

    def move(self):
        self.tut.forward(STARTING_MOVE_DISTANCE)   #MOVING THE CARS












