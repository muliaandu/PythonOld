import turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def create_snake(self):
        for position in POSITION:
            self.add_snake(position)

    def add_snake(self, position):
            t = turtle.Turtle(shape = "square")
            t.speed("fastest")
            t.color("white")
            t.penup()
            t.goto(position)
            self.snake.append(t)

    def extend(self):
        self.add_snake(self.snake[-1].position())

    def move(self):
        for body in range(len(self.snake) - 1, 0, -1):
            body_x = self.snake[body - 1].xcor()
            body_y = self.snake[body - 1].ycor()
            self.snake[body].goto(body_x, body_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
