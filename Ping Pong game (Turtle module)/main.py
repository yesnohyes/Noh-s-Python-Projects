from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# TODO: create screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if right paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_score()

    # if left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_score()
