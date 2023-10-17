import turtle
import Paddle
import Ball
import time
import Scoreboard

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle.Paddle((350, 0))
l_paddle = Paddle.Paddle((-350 , 0))
ball = Ball.Ball()
r_score = Scoreboard.Scoreboard((100, 250))
l_score = Scoreboard.Scoreboard((-100, 250))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    elif ball.distance(r_paddle) < 30 and ball.xcor() > 320 or ball.distance(l_paddle) < 30 and ball.xcor() < -320:
        ball.x_bounce()
    elif ball.xcor() > 380:
        l_score.increase_score()
        ball.reset_position()
        ball.x_bounce()
    elif ball.xcor() < -380:
        r_score.increase_score()
        ball.reset_position()
        ball.x_bounce()
    elif r_score.score == 10:
        r_score.r_game_over()
        game_on = False
    elif l_score.score == 10:
        l_score.l_game_over()
        game_on = False
        
        

screen.exitonclick()