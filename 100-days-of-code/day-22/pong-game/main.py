import time
from turtle import Screen
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
ball_directions = (5, -1)
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(ball_directions)
    if ball.is_collision_with_paddle(r_paddle):
        ball_directions = ball.new_direction()

screen.exitonclick()
