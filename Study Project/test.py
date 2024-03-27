from tkinter import *

def button_clicked():
    word = "I GOT CLICKED"
    if input.get() != "":
        word = input.get()
    my_label.config(text = word)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
    
# Label
word = "I am a label"
my_label = Label(text = word, font = ("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text = "New Text")
my_label.grid(column = 0, row = 0)

# Button
button = Button(text = "Click Me", command = button_clicked)
button.grid(column = 1, row = 1)

# New Button
button = Button(text = "Click Me", command = button_clicked)
button.grid(column = 2, row = 0)

# Entry
input = Entry(width = 10)
input.grid(column = 3, row = 2)

window.mainloop()