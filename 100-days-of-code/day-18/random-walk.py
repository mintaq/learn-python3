import turtle as t
import random

tim = t.Turtle()
tim.dot(1)
tim.pensize(10)
tim.speed("fastest")
t.colormode(255)

# Challenge 4 - Random Walk #
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def random_walk():
    direction = random.choice([0, 90, 180, 270])
    tim.color(random_color(), random_color())
    tim.right(direction)
    tim.forward(30)


while True:
    random_walk()
