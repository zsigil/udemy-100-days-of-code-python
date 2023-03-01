from turtle import Turtle, Screen
import random

def draw_line():
    referee = Turtle()
    referee.hideturtle()
    referee.penup()
    referee.goto(x=210, y=-200)
    referee.pendown()
    referee.left(90)
    referee.forward(400)

screen = Screen()
screen.setup (width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []

bet = screen.textinput("Who will win?", "Input the color of your bet turtle")
print(f"Your bet: {bet} turtle.")
draw_line()

for col in colors:
    t = Turtle()
    t.shape('turtle')
    t.penup()
    t.fillcolor(col)
    i = colors.index(col)
    y = -60 + 30* i
    t.goto(x=-235, y=y)
    turtles.append(t)


race_is_on = True
winner = ""

while race_is_on:
    for t in turtles:
        step = random.randint(10,30)
        t.forward(step)
        if t.position()[0] > 210:
            winner = t.fillcolor()
            race_is_on = False


if bet == winner:
    print("You won.")
else: 
    print('You lost.')

print(f"The winner is the {winner} turtle.")

screen.exitonclick()

