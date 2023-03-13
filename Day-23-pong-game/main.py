from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)
screen.listen()

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(paddle_right.move_up, 'Up')
screen.onkey(paddle_right.move_down, 'Down')
screen.onkey(paddle_left.move_up, 'w')
screen.onkey(paddle_left.move_down, 's')


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with ceiling and floor
    if ball.ycor() > 286 or ball.ycor() < -286:
        ball.bounce_y()

    #detect collision with paddles
    if (ball.distance(paddle_right)<50 and ball.xcor()>330) or (ball.distance(paddle_left)<50 and ball.xcor()<-330):
        ball.bounce_x()
    
    elif ball.xcor()>370 or ball.xcor()<-370:
        #give point
        if ball.xcor()>370:
            scoreboard.score_left()
        else:
            scoreboard.score_right()
        #reset ball position
        ball.reset()





screen.exitonclick()
