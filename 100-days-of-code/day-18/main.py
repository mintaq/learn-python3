from turtle import Turtle
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("green")


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for num_sizes in range(2, 11):
    draw_shape(num_sizes)
