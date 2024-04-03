import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    window.after_cancel(timer)
    title_label.config(text = "Timer", fg = GREEN)
    canvas.itemconfig(timer_text, text = f"00:00")
    check_mark.config(text = "")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 

    reps += 1
    work_sec = 5
    short_break_sec = 5
    long_break_sec = 5
    print(f"reps {reps}")

    if reps % 2 != 0 and reps % 8 != 0:
        print(f"work")
        countdown(work_sec)
        title_label.config(text = "Work", fg = GREEN)
    elif reps % 2 == 0 and reps % 8 != 0:
        print(f"short break")
        countdown(short_break_sec)
        title_label.config(text = "Short Brake", fg = PINK)
    else :
        print(f"long break")
        countdown(long_break_sec)
        title_label.config(text = "Long Break", fg = RED)
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer

    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"

    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    print(count)
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else :
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            marks += "✔"
        check_mark.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

title_label = tkinter.Label(text = "timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 40))
title_label.grid(column = 1, row = 0)

canvas = tkinter.Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = tkinter.PhotoImage(file = r"C:\Users\ASUS\Documents\ANDU\Python\Study Project\Pomodoro\Pomodoro.png")
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100,130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

start_button = tkinter.Button(text = "Start", command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = tkinter.Button(text = "Reset", command = reset_timer)
reset_button.grid(column = 2, row = 2)

check_mark = tkinter.Label(text = "", fg = RED, bg = YELLOW, font = (FONT_NAME, 20))
check_mark.grid(column = 1, row = 3)

window.mainloop()