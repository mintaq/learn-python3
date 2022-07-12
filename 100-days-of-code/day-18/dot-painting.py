import colorgram
import turtle as t
import random

timmy = t.Turtle()
timmy.penup()
t.colormode(255)
colors = colorgram.extract('dots.webp', 126)
print(colors[0].rgb)
dot_distance = 30


def draw_dots_picture(picture_size):
    for height in range(picture_size):
        for width in range(picture_size):
            timmy.color(colors[random.randint(0, len(colors)-1)].rgb)
            timmy.dot(10)
            timmy.forward(dot_distance)
        timmy.setheading(180)
        timmy.forward(dot_distance * picture_size)
        timmy.setheading(90)
        timmy.forward(dot_distance)
        timmy.setheading(0)


draw_dots_picture(5)