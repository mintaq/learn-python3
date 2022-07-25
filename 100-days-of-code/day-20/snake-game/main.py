import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

WALL_BORDER = 290

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > WALL_BORDER or \
            snake.head.xcor() < -WALL_BORDER or \
            snake.head.ycor() > WALL_BORDER or \
            snake.head.ycor() < -WALL_BORDER:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
