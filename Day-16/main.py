#TURTLE

# import turtle

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color('violet')
# timmy.forward(100)
# timmy.penup()
# timmy.forward(20)
# timmy.pendown()
# timmy.forward(20)

# my_screen = turtle.Screen()
# my_screen.exitonclick()

#PRETTY TABLE
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name",
["Pikachu","Squirtle","Charmander"])
table.add_column("Type",
["Electric","Water","Fire"])
table.align = "l"

print(table)



