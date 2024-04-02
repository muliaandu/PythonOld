from tkinter import *

# Calculate The Result
def button_calculate():
    miles = input.get()
    km = int(miles) * 1.609344
    text_result.config(text = str(km))

# Title
title = "Mile to Km Converter"
window = Tk()
window.title(title)
window.minsize(width = 1000, height = 1000)
window.config(padx = 20, pady = 20)

# Entry Miles
input = Entry(width = 20)
input.grid(column = 2, row = 1)
# input.config(padx = 5, pady = 5)

# Text Miles
text_miles = Label(text = "Miles", font = ("Arial", 20, "bold"))
text_miles.grid(column = 3, row = 1)
text_miles.config(padx = 5, pady = 5)

# Text Km
text_km = Label(text = "Km", font = ("Arial", 20, "bold"))
text_km.grid(column = 3, row = 2)
text_km.config(padx = 5, pady = 5)

# Text (is equal to)
text_equal = Label(text = "is equal to", font = ("Arial", 20, "bold"))
text_equal.grid(column = 1, row = 2)
text_equal.config(padx = 5, pady = 5)

# Result
km = "0"
text_result = Label(text = km, font = ("Arial", 20, "bold"))
text_result.grid(column = 2, row = 2)
text_result.config(padx = 5, pady = 5)


# Button Calculate
button = Button(text = "Calculate", font = ("Arial", 10, "bold"), foreground = "Blue", command = button_calculate)
button.grid(column = 2, row = 3)
button.config(padx = 5, pady = 5)


window.mainloop()