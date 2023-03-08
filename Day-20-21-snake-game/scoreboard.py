from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update()

    
    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('Arial', 16, 'bold'))
    

    def add_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Arial', 30, 'bold'))