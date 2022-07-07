from turtle import *

timmy = Turtle()
timmy.shape("turtle")
timmy.color('yellow', 'green')
timmy.begin_fill()
while True:
    timmy.forward(200)
    timmy.left(170)
    if abs(timmy.pos()) < 1:
        break
timmy.end_fill()
timmy.done()

my_screen = Screen()
my_screen.exitonclick()
