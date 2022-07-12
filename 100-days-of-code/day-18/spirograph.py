import turtle as t
import random

tim = t.Turtle()
tim.dot(1)
tim.pensize(1)
tim.speed("normal")
t.colormode(255)

# Challenge 4 - Random Walk #
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color(), random_color())
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)


draw_spirograph(5)
