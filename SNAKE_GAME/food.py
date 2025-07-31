from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("Blue")
        self.shapesize(0.5,0.5)
        self.goto(random.randint(-320,320),random.randint(-320,320))

    def relocate(self,snakehead,scoreturtle):
        if self.distance(snakehead) < 15:
            self.goto(random.randint(-280,280),random.randint(-280,280))
            scoreturtle.Score += 1
            return True
        return False






