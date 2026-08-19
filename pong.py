import time
import turtle
from Paddles import Paddle1, Paddle2
from scoreboard import Scoreboard
from ball import Ball
from tkinter import messagebox

Ball = Ball()

turtle.tracer(0)
screen = turtle.Screen()
screen.bgcolor("grey")
screen.setup(width=800, height=700)
screen.title("⚾🥎PONG🥎⚾ : THE ARCADE GAME")

scoreboard = Scoreboard()
scoreboard.left_board()
scoreboard.right_board()
game_on = True


screen.listen()
paddle1 = Paddle1()
turtle.onkeypress(paddle1.move_up, "w")
turtle.onkeypress(paddle1.move_down, "s")
paddle2 = Paddle2()
turtle.onkeypress(paddle2.move_up, "Up")
turtle.onkeypress(paddle2.move_down, "Down")



def reset(): 
    Ball.ball_speed = 0.07 # type: ignore
    Ball.reset_pos() # type: ignore

def quit_game():
    answer = messagebox.askyesno("Quit Game", "Are you sure you want to quit?")
    if answer:
        global game_on
        game_on = False 
        screen.bye()

screen.onkeypress(quit_game, "h")

while game_on:
    time.sleep(Ball.ball_speed)
    Ball.move()
    if Ball.ball.ycor() > 330 or Ball.ball.ycor() < -330:
        Ball.bounce()
    if Ball.ball.xcor() == 360 and Ball.ball.distance(paddle2.tim) <= 50 or Ball.ball.xcor() == -360 and \
            Ball.ball.distance(paddle1.tim) <= 50:
        if Ball.ball_speed > 0.005:
            Ball.ball_speed -= 0.005
        print(Ball.ball_speed)
        Ball.rebound()

        # Keeping Score
        if Ball.ball.xcor() < 0:
            scoreboard.update_score1()
        elif Ball.ball.xcor() > 0:
            scoreboard.update_score2()

    #  Detect if the paddle has missed
    if Ball.ball.xcor() >= 370:
        reset()
        scoreboard.update_score1()
    elif Ball.ball.xcor() <= -370:
        reset()
        scoreboard.update_score2()
    screen.update()

