from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup (width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
time.sleep(1)
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

        
    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -295 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
