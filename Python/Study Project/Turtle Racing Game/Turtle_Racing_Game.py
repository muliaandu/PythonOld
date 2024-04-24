from turtle import Turtle, Screen
import random

is_racing = True
screen = Screen()
screen.setup(width = 1100, height = 1100)
colors = ["red", "orange", "gold", "spring green", "green", "blue", "purple", "black", "brown", "pink", "grey"]
all_turtle = []

def turtle_prepare(all_turtle):
    x = -500
    y = -500
    for color in colors:
        tim = Turtle(shape = "turtle")
        tim.color(color)
        tim.penup()
        tim.goto(x, y)
        y += 100
        tim.pendown()
        all_turtle.append(tim)
    return all_turtle

all_turtle = turtle_prepare(all_turtle)
user_bet = screen.textinput(title = "Make your bet.", prompt = 'red, orange, gold, spring green, green, blue, purple, black, brown, pink, grey \nWhich turtle will win the race? Enter a color: ')

while is_racing:
        for turtle in all_turtle:
            if turtle.xcor() > 500:
                is_racing = False
                winning_color = turtle.fillcolor()
                if winning_color == user_bet:
                    print(f"You've WON! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've LOSE! The {winning_color} turtle is the winner!")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


screen.exitonclick()