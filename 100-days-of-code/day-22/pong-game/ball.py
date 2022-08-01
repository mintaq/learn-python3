from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_ball(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def create_ball(self, position):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=1)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.95

    def is_collision_with_paddle(self, paddle, max_distance=10):
        return self.distance(paddle) < max_distance

    def is_collision_with_wall(self, wall_border=280):
        return self.ycor() > wall_border or \
               self.ycor() < -wall_border

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
