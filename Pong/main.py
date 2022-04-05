from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Welcome to the Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_scoreboard = Scoreboard((-100, 200))
r_scoreboard = Scoreboard((100, 200))

screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")




game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #detect collision with right paddle or left paddle
    if ball.xcor() > 320 and ball.xcor() < 340 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.xcor() > -340 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    
    #detect when paddles misses
    if ball.xcor() > 380:
        ball.refresh()
        l_scoreboard.add_score()
    
    if ball.xcor() < -380:
        ball.refresh()
        r_scoreboard.add_score()
