from turtle import Turtle
#DEFINE THE SCOREBOARD CLASS
class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.goto(x,y)
        self.hideturtle()
        self.color('white')
        self.Score=0
        self.write(arg=self.Score, align='center', font=('Ariel', 30, 'normal'))

    def score2(self,ball): #SCORE COUNT FOR WHEN THE RIGHT PADDLE MISSES
        if ball.xcor()> 390:
            self.clear()
            self.Score += 1
            self.write(arg= self.Score , align = 'center', font = ('Ariel', 30, 'normal'))
            ball.goto(0,0)
            ball.setheading(180-ball.heading())

    def score1(self,ball): #SCORE PADDLE FOR WHEN THE LEFT PADDLE MISSES
        if ball.xcor()< -390:
            self.clear()
            self.Score += 1
            self.write(arg= self.Score , align = 'center', font = ('Ariel', 30, 'normal'))
            ball.goto(0, 0)
            ball.setheading(180 - ball.heading())
