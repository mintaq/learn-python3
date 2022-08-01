from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_ball(position)

    def create_ball(self, position):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=1)

    def move(self, directions=(5, 3)):
        new_x = self.xcor() + directions[0]
        new_y = self.ycor() + directions[1]
        self.goto(new_x, new_y)

    def new_direction(self):
        if self.heading() == RIGHT:
            return (-5, +3)

    def is_collision_with_paddle(self, paddle, max_distance=10):
        print(self.distance(paddle) < max_distance)
        return self.distance(paddle) < max_distance

    def is_collision_with_wall(self, wall_border=290):
        return self.xcor() > wall_border or \
            self.xcor() < -wall_border or \
            self.ycor() > wall_border or \
            self.ycor() < -wall_border
