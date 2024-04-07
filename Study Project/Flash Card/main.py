from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
data = read_csv("Study Project\\Flash Card\\data\\french_words.csv")
word_card = data.to_dict(orient = "records")
current_card = {}

def next_card():
    global current_card
    front_card()
    current_card = choice(word_card)
    key = list(current_card.keys())[0]
    canvas.itemconfig(card_title, text = key)
    canvas.itemconfig(card_word, text = current_card["French"])

def front_card():
    # Front Card
    canvas.itemconfig(card_image, image = card_front_image)

def flip_card():
    global current_card
    # Back Card
    canvas.itemconfig(card_image, image = card_back_image)
    key = list(current_card.keys())[1]
    canvas.itemconfig(card_title, text = key)
    canvas.itemconfig(card_word, text = current_card["English"])

window = Tk()
window.title("Flash")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

# Front Card
canvas = Canvas(width = 800, height = 526)
card_front_image = PhotoImage(file = "Study Project\\Flash Card\\images\\card_front.png")
card_back_image = PhotoImage(file = "Study Project\\Flash Card\\images\\card_back.png")
card_image = canvas.create_image(400, 263)
card_title = canvas.create_text(400, 150, text = "Title", font = ("Arial", 30, "italic"))
card_word = canvas.create_text(400, 263, text = "word", font = ("Arial", 60, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row = 0, column = 0, columnspan = 2)

next_card()

unknown_image = PhotoImage(file = "Study Project\\Flash Card\\images\\wrong.png")
unknown_button = Button(image = unknown_image, highlightthickness = 0, command = flip_card)
unknown_button.grid(row = 1, column = 0)

known_image = PhotoImage(file = "Study Project\\Flash Card\\images\\right.png")
known_button = Button(image = known_image, highlightthickness = 0, command = next_card)
known_button.grid(row = 1, column = 1)

window.mainloop()