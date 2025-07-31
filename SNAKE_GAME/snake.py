from turtle import Turtle
import time
class Snake:
    def __init__(self):
        self.turtles = []
        xco = 0
        for x in range(0, 3):
            tutu = Turtle()
            tutu.speed("fast")
            tutu.shape("square")
            tutu.color("white")
            self.turtles.append(tutu)
            tutu.up()
            tutu.setx(xco)
            xco -= 20
        self.head=self.turtles[0]

    def extend(self):
        posx= self.turtles[-1].xcor()
        posy = self.turtles[-1].ycor()
        new= Turtle()
        new.penup()
        new.speed("fast")
        new.shape("square")
        new.color("white")
        self.turtles.append(new)
        new.goto(posx, posy)

    def self_collision(self):
        for x in self.turtles[1::]:
            if x.distance(self.head) < 10:
                turt= Turtle()
                turt.hideturtle()
                turt.up()
                turt.goto(0,0)
                turt.color("white")
                turt.write(arg='GAME OVER', align='center', font=('Courier', 15, 'normal'))
                return False
        return True


    def move(self):
        for x in range((len(self.turtles) - 1), 0, -1):
            tut = self.turtles[x - 1]
            self.turtles[x].goto(tut.xcor(), tut.ycor())
        self.head.forward(20)
        time.sleep(0.1)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
        else:
            pass

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
        else:
            pass

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
        else:
            pass

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        else:
            pass