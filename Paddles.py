import turtle
from turtle import Turtle


class Paddle1:
    def __init__(self):
        self.tim = Turtle()
        self.tim.shape("square")
        self.tim.penup()
        self.tim.color("white")
        self.tim.goto(-370, 0)
        self.tim.shapesize(stretch_len=1, stretch_wid=5)
        self.tim.color("red")

    def move_up(self):
        self.tim.goto(self.tim.xcor(), self.tim.ycor()+20)
        turtle.Screen().update()

    def move_down(self):
        self.tim.goto(self.tim.xcor(), self.tim.ycor()-20)
        turtle.Screen().update()


class Paddle2(Paddle1):
    def __init__(self):
        super().__init__()
        self.tim.color("blue")
        self.tim.goto(375, 0)
