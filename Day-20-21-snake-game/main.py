from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen_width = 600
screen_height = 600

screen = Screen()


screen.setup(width=screen_width, height=screen_height)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)
screen.listen()

snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


food = Food()
scoreboard = Scoreboard()


while snake.is_alive():  
    screen.update()  
    time.sleep(0.25)
    snake.move_snake()

    #detect collision with food
    if snake.snake[0].distance(food) < 15:
        food.refresh()
        snake.add_segment()
        scoreboard.add_score()

scoreboard.game_over()

    

 
screen.exitonclick()


