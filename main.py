from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=500, width=500)
screen.bgcolor("black")
screen.title("My Snake Game.")
screen.tracer(0)
scoreboard = Scoreboard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_updator()
        snake.extend()
        print("nom nom nom")

    if snake.head.xcor() > 248 or snake.head.xcor() < -248 or snake.head.ycor() > 248 or snake.head.ycor() < -248:
        game_is_on = False
        scoreboard.game_over()

    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
