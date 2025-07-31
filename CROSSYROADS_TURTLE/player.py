from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#PLAYER CLASS DEFINITION
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.color("black")

    def move(self):
        self.forward(MOVE_DISTANCE)  #PLAYER MOVEMENT