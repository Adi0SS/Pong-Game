from turtle import Turtle
tup = ("Elephanta", 60, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.create_net()
        self.tim = Turtle()
        self.tum = Turtle()

    def move_up(self):
        self.forward(25)

    def create_net(self):
        self.hideturtle()
        self.pencolor("white")
        self.width(3)
        self.penup()
        self.goto(0, 350)
        self.right(90)
        self.pendown()
        for i in range(40):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

    def left_board(self):
        self.tim.pencolor("white")
        self.tim.hideturtle()
        self.tim.penup()
        self.tim.setposition(-90, 250)
        self.tim.pendown()
        self.tim.write(arg=f"{self.score_p1}", font=tup)
        self.penup()
        self.goto(0, 0)

    def right_board(self):
        self.tum.pencolor("white")
        self.tum.hideturtle()
        self.tum.penup()
        self.tum.setposition(30, 250)
        self.tum.pendown()
        self.tum.write(arg=f"{self.score_p2}", font=tup)
        self.penup()
        self.goto(0, 0)

    def update_score1(self):
        self.tim.clear()
        self.score_p1 += 1
        self.left_board()

    def update_score2(self):
        self.tum.clear()
        self.score_p2 += 1
        self.right_board()
