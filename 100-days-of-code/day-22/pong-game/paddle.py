from turtle import Turtle

STARTING_POSITIONS = [(-280, 20), (-280, 0), (-280, -20)]


class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        segment.shapesize(stretch_wid=5, stretch_len=1)
        self.segments.append(segment)
