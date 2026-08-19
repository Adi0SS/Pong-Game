import turtle


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle(shape="circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.speed("slowest")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed:float = 0.07

    def move(self):
        new_x = self.ball.xcor()+self.x_move
        new_y = self.ball.ycor()+self.y_move
        self.ball.goto(new_x, new_y)
        print(f"x={self.ball.xcor()}, y={self.ball.ycor()}")

    def bounce(self):
        self.y_move *= -1
        print("wall hit")
        print(self.ball.ycor())

    def rebound(self):
        self.x_move *= -1
        print("paddle hit")
        print(self.ball.xcor())

    def reset_pos(self):
        self.ball.goto(0, 0)
        self.rebound()
