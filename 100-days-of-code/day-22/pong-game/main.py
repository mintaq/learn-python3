from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My Pong Game")
# screen.tracer(0)

paddle_1 = Paddle()


screen.exitonclick()
