from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_screen = Screen()
game_screen.setup(width=600, height=600)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
game_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_screen.listen()
game_screen.onkey(snake.up,"Up")
game_screen.onkey(snake.down,"Down")
game_screen.onkey(snake.left,"Left")
game_screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    game_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)< 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

game_screen.exitonclick()