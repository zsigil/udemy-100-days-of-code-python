from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red", "blue")
screen = Screen()
screen.screensize(500,500)
print(screen.window_width())
screen.colormode(255)
timmy.speed(10)

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.reset()

for _ in range(15):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

timmy.reset()
base = 70

def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

for i in range(3, 5):
    #sokszög belső szögeinek összege (n-2)*180
    timmy.pencolor(random_color())
    for j in range(i):
        timmy.forward(base)
        timmy.right((180-((i-2)*180)/i))


timmy.reset()

# random walk
directions = [0, 90, 180, 270]
timmy.pensize(5)

for _ in range(5):
    timmy.pencolor(random_color())
    timmy.right(random.choice(directions))
    timmy.forward(20)


timmy.reset()
timmy.speed('fastest')

number_of_circles = 36
for i in range(number_of_circles):
    timmy.pencolor(random_color())
    timmy.circle(100)
    timmy.penup()
    timmy.right(10)
    # timmy.forward(10)
    timmy.pendown()


timmy.reset()
timmy.speed(10)

colorlist = []
for i in range(30):
    colorlist.append(random_color())


win_height = screen.window_height()
win_width = screen.window_width()
circle_size = 20

timmy.penup()
timmy.setpos(-win_width/2 + 2*circle_size, -win_height/2+2*circle_size)
timmy.pendown()


for i in range(1,101):
    timmy.fillcolor(random.choice(colorlist))
    timmy.begin_fill()
    timmy.circle(circle_size)
    timmy.end_fill()
    timmy.penup()
    
    if i % 20 == 0:
        timmy.right(90)
        timmy.forward(2*circle_size)
        timmy.right(90)

    elif i % 10 == 0:
        timmy.right(270)
        timmy.forward(6*circle_size)
        timmy.right(270)

    else:
        timmy.forward(4*circle_size)
    
    timmy.pendown()




screen.exitonclick()