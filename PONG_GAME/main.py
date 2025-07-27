#IMPORTS
import turtle
from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#INITIALISE SCREEN
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

#SEPERATION LINE ON SCREEN
tutu= Turtle()
tutu.color('white')
tutu.speed("fastest")
tutu.pencolor('white')
tutu.hideturtle()
tutu.penup()
tutu.width(5)
tutu.goto(0,-280)
tutu.setheading(90)

for x in range(0,10):
    tutu.pendown()
    tutu.forward(30)
    tutu.penup()
    tutu.forward(30)

#CREATE THE PONG PADDLES
paddle1=Paddle(370,0)
paddle2=Paddle(-380,0)
ball = Ball()

#CREATE THE SCOREBOARDS
scoreboard1=Scoreboard(40,250)
scoreboard2=Scoreboard(-40,250)

#ENDGAME TURTLE *ANNOUNCES THE WINNER
tut=Turtle()
tut.hideturtle()
tut.color('white')
tut.penup()

#EVENT LISTENERS FOR KEYPRESSES
turtle.onkeypress(fun = paddle1.up,key = "Up")
turtle.onkeypress(fun = paddle1.down,key = "Down")
turtle.onkeypress(fun = paddle2.up,key = "w")
turtle.onkeypress(fun = paddle2.down,key = "s")
screen.listen()

#MAIN GAME LOOP
is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    ball.bounce_paddle(paddle1,paddle2)
    ball.bounce_wall()
    scoreboard1.score1(ball)
    scoreboard2.score2(ball)
    if scoreboard1.Score==10:
        tut.goto(150,0)
        tut.write(arg = "RIGHT WINS", align = "center", font = ("Arial", 30,"normal"))
        is_game_on = False
    if scoreboard2.Score==10:
        tut.goto(-150,0)
        tut.write(arg = "LEFT WINS", align = "center", font = ("Arial", 30,"normal"))
        is_game_on = False

screen.exitonclick()