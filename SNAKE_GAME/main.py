from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import *

screen = Screen()
screen.setup(width=660, height=660)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)

snake= Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    game_is_on = scoreboard.game_over_wall(snake.head)  # Wall collision check BEFORE moving
    if not game_is_on:
        break

    game_is_on = snake.self_collision()
    if not game_is_on:
        break

    snake.move()
    scoreboard.score()

    if food.relocate(snake.head, scoreboard):
        snake.extend()

screen.exitonclick()