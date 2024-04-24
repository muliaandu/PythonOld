import turtle
import random

class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len = 1, stretch_wid = 1)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-500, 500)
        random_y = random.randint(-500, 500)
        self.goto(random_x, random_y)
