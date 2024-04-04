from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = input_website.get()
    email = input_username.get()
    password = input_password.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("C:\\Users\\ASUS\\Documents\\ANDU\\Python\\Study Project\\Password Manager\\data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                input_website.delete(0, END)
                input_username.delete(0, END)
                input_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = 200, height = 200)
lock_img = PhotoImage(file = "C:\\Users\\ASUS\\Documents\\ANDU\\Python\\Study Project\\Password Manager\\logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(column = 1, row = 0)

text_website = Label(text = f"Website :")
text_website.grid(column = 0, row = 1)

input_website = Entry(width = 53)
input_website.grid(column = 1, row = 1, columnspan = 2)
input_website.focus()

text_username = Label(text = f"Email / Username :")
text_username.grid(column = 0, row = 2)

input_username = Entry(width = 53)
input_username.grid(column = 1, row = 2, columnspan = 2)

text_password = Label(text = f"Password :")
text_password.grid(column = 0, row = 3)

input_password = Entry(width = 33)
input_password.grid(column = 1, row = 3)

generate_button = Button(text = f"Generate Password", width = 16, highlightthickness = 0, command = generate_password)
generate_button.grid(column = 2, row = 3)

add_button = Button(text = f"add", width = 45, command = save)
add_button.grid(column = 1, row = 4, columnspan = 2)


window.mainloop()