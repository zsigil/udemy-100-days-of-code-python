from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 0
        self.update()


    def update(self):
        self.clear()
        self.write(f"Level {self.level}", align='left', font=FONT)


    def level_up(self):
        self.level +=1
        self.update()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=FONT)