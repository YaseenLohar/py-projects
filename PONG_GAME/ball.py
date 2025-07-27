from turtle import Turtle
#BALL CLASS DEFINITION
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(1)
        self.penup()
        self.speed('fastest')
        self.color("white")
        self.setheading(45)
        self.goto(0,0)

    def move(self): #MOVE THE BALL
        self.forward(0.17)

    def bounce_wall(self): #DETECT A COLLISION OF THE BALL WITH THE TOP OR BOTTOM HORIZONTAL WALL
        if self.ycor() > 290:
            newh = 90 - self.heading()
            self.setheading(360 - newh)

        elif self.ycor() < -290:
            newh = 90 - self.heading()
            self.setheading(360 - newh)

    def bounce_paddle(self,paddle1,paddle2):  #DETECT COLLISION WITH THE PADDLE
        if (350<self.xcor()<360) and (paddle1.ycor() -50< self.ycor()<paddle1.ycor()+50) :
            self.setheading(180 - self.heading())

        if (-370<self.xcor()<-360) and (paddle2.ycor()-50< self.ycor()<paddle2.ycor()+50) :
            self.setheading(180 - self.heading())






