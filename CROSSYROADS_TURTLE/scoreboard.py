from turtle import Turtle

FONT = ("Courier", 24, "normal")
#SCOREBOARD CLASS DEFINITION
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.Level=0
        self.hideturtle()
        self.penup()
        self.goto(-230,250)
        self.color("black")

    def next_level(self):   #LEVEL INCREMENT
        self.Level += 1