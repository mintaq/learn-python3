import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

WALL_BORDER = 290
FOOD_COLLISION_DISTANCE = 15
TAIL_COLLISION_DISTANCE = 10

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
    if snake.is_collision_with_food(food, FOOD_COLLISION_DISTANCE):
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.is_collision_with_wall(WALL_BORDER):
        game_is_on = False
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    if snake.is_collision_with_tail(TAIL_COLLISION_DISTANCE):
        game_is_on = False
        scoreboard.reset()
        snake.reset()

screen.exitonclick()
