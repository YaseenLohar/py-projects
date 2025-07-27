from turtle import Turtle
#PADDLE CLASS DEFINITION
class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.goto(x,y)
        self.setheading(90)
        self.tilt(90)
        self.color('white')
        self.speed('fast')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape('square')
        self.penup()

    def up(self):
        self.forward(20)    #MOVE UPWARDS METHOD

    def down(self):
        self.backward(20)   #MOVE DOWNWARDS METHOD



