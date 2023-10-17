import turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(turtle.Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("green")
        self.score = 0
        self.penup()
        self.goto (position)
        self.write(f"{self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}", align = ALIGNMENT, font = FONT)

    def r_game_over(self):
        self.goto(0, 0)
        self.write(f"RIGHT WIN", align = ALIGNMENT, font = FONT)

    def l_game_over(self):
        self.goto(0, 0)
        self.write(f"LEFT WIN", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()