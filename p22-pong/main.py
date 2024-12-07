from turtle import Screen
from paddles import Paddle
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-300, 0))
right_paddle = Paddle((300, 0))

ball = Ball()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
