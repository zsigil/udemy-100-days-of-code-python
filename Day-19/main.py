from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_left():
    angle = timmy.heading()
    timmy.setheading(angle+10)

def turn_right():
    angle = timmy.heading()
    timmy.setheading(angle-10)

def home():
    timmy.reset()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(home, "c")


screen.exitonclick()