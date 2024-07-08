from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
UP = 280
DOWN = -280

screen = Screen()
score = Scoreboard()
#screen size
screen.screensize(canvwidth=800,canvheight=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350,0),"square")
r_paddle = Paddle((350,0),"square")
ball = Ball()

#controls to control the paddle
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

#creating paddles for pong game

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #detect collison with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when paddles miss the ball
    if ball.distance(r_paddle) > 50 and ball.xcor() > 340:
        ball.reset()
        score.l_point()

    if ball.distance(l_paddle) > 50 and ball.xcor() < -340:
        ball.reset()
        score.r_point()
