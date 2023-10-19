import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "D:\\Python\\Study Project\\U.S. States Game\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("D:\\Python\\Study Project\\U.S. States Game\\50_states.csv")
all_states = data["state"].to_list()
guessed = []

while len(guessed) < 50:
    answer = screen.textinput(title = f"{len(guessed)}/50 States.", prompt = "What's another state's name??").capitalize()
    if answer == "Exit":
        states_left = []
        for state in all_states:
            if state not in guessed:
                states_left.append(state)
        new_file = pd.DataFrame(states_left)
        new_file.to_csv("D:\\Python\\Study Project\\U.S. States Game\\states_to_learn.csv")
        break
    if answer in all_states:
        guessed.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(answer)