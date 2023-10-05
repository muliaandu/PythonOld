from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

import turtle
import time

screen = turtle.Screen()
screen.setup(width = 1100, height = 1100)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    if snake.head.xcor() > 520 or snake.head.xcor() < -520 or snake.head.ycor() > 520 or snake.head.ycor() < -520:
        game_on = False
        scoreboard.game_over()

    for body in snake.snake[1:]:
        if snake.head.distance(body) < 15:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()