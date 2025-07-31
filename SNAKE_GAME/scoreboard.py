from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.Score=0
        self.highscore=0
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.goto(0, 290)

    def score(self):
        self.clear()
        self.write(arg = f"SCORE : {self.Score} ",move =False, align = "center", font = ("Courier", 15,'normal'))

    def reset(self):
        if self.Score>self.highscore:
            self.highscore = self.Score
            self.score()

    def game_over_wall(self,snake):
        if snake.xcor() > 330 or snake.xcor() < -330 or snake.ycor() > 330 or snake.ycor() < -330:
            self.goto(0,0)
            self.write(arg="GAME OVER",align="center",font=("Courier", 15,'normal'))
            return False
        else:
            return True


