from tkinter import *
from pandas import *
from pandas.errors import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_card = {}

try :
    data = read_csv("Study Project\\Flash Card\\data\\words_to_learn.csv")
except FileNotFoundError:
    data = read_csv("Study Project\\Flash Card\\data\\french_words.csv")
    word_card = data.to_dict(orient = "records")
except EmptyDataError:
    data = read_csv("Study Project\\Flash Card\\data\\french_words.csv")
    word_card = data.to_dict(orient = "records")
else:
    word_card = data.to_dict(orient = "records")

def next_card():
    global current_card, flip_timer, word_card
    front_card()
    window.after_cancel(flip_timer)
    try:
        current_card = choice(word_card)
    except IndexError:
        data = read_csv("Study Project\\Flash Card\\data\\french_words.csv")
        word_card = data.to_dict(orient = "records")
        current_card = choice(word_card)
    else:
        pass
    key = list(current_card.keys())[0]
    canvas.itemconfig(card_title, text = key, fill = "black")
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    flip_timer = window.after(10000, func = flip_card)
    return current_card

def is_known():
    global word_card, current_card
    try:
        word_card.remove(current_card)
    except ValueError:
        data = read_csv("Study Project\\Flash Card\\data\\french_words.csv")
        word_card = data.to_dict(orient = "records")
        word_card.remove(current_card)
        new_data = DataFrame(word_card)
        new_data.to_csv("Study Project\\Flash Card\\data\\words_to_learn.csv", index = False)
    else:
        new_data = DataFrame(word_card)
        new_data.to_csv("Study Project\\Flash Card\\data\\words_to_learn.csv", index = False)
    finally:
        next_card()

def front_card():
    # Front Card
    canvas.itemconfig(card_image, image = card_front_image)

def flip_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # Back Card
    canvas.itemconfig(card_image, image = card_back_image)
    key = list(current_card.keys())[1]
    canvas.itemconfig(card_title, text = key, fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")

window = Tk()
window.title("Flash")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
flip_timer = window.after(10000, func = flip_card)

# Front Card
canvas = Canvas(width = 800, height = 526)
card_front_image = PhotoImage(file = "Study Project\\Flash Card\\images\\card_front.png")
card_back_image = PhotoImage(file = "Study Project\\Flash Card\\images\\card_back.png")
card_image = canvas.create_image(400, 263)
card_title = canvas.create_text(400, 150, text = "Title", font = ("Arial", 30, "italic"))
card_word = canvas.create_text(400, 263, text = "word", font = ("Arial", 60, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(row = 0, column = 0, columnspan = 2)

unknown_image = PhotoImage(file = "Study Project\\Flash Card\\images\\wrong.png")
unknown_button = Button(image = unknown_image, highlightthickness = 0, command = flip_card)
unknown_button.grid(row = 1, column = 0)

known_image = PhotoImage(file = "Study Project\\Flash Card\\images\\right.png")
known_button = Button(image = known_image, highlightthickness = 0, command = is_known)
known_button.grid(row = 1, column = 1)

next_card()

window.mainloop()