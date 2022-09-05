from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """The Snake model"""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1001)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Add a new segment to the snake."""
        self.add_segment(self.segments[-1].position())

    def is_collision_with_food(self, food, max_distance=15):
        return self.head.distance(food) < max_distance

    def is_collision_with_wall(self, wall_border=290):
        return self.head.xcor() > wall_border or \
            self.head.xcor() < -wall_border or \
            self.head.ycor() > wall_border or \
            self.head.ycor() < -wall_border

    def is_collision_with_tail(self, max_distance=10):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < max_distance:
                return True

        return False

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
