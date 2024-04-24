import turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.score = 0
        with open("D:\Python\Study Project\Snake\High_Score.txt") as file:
            self.highscore = int(file.read())
        self.penup()
        self.goto (0, 500)
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("D:\Python\Study Project\Snake\High_Score.txt", mode = "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()