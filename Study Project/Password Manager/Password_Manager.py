from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

website = None

# ----------------------- PASSWORD GENERATOR --------------------------- #
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

# ------------------------- SAVE PASSWORD ----------------------------- #
def save():

    website = input_website.get()
    email = input_username.get()
    password = input_password.get()
    new_data = {
                website:
                        {
                            "email": email,
                            "password": password,
                        }
                }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=f"Confirmation", message=f"These are the details entered: \n\nWebsite: {website} \nEmail: {email} \nPassword: {password} \n\nIs it ok to save?")
        if is_ok:
            try:
                with open("C:\\Users\\ASUS\\Documents\\ANDU\\Python\\Study Project\\Password Manager\\data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            except json.JSONDecodeError:
                data = {}
            
            # Updating data
            data.update(new_data)

            with open("C:\\Users\\ASUS\\Documents\\ANDU\\Python\\Study Project\\Password Manager\\data.json", "w") as data_file:
                # Saing updated data
                json.dump(new_data, data_file, indent = 4)

                # data_file.write(f"{website} | {email} | {password}\n")

                input_website.delete(0, END)
                input_username.delete(0, END)
                input_password.delete(0, END)

# ---------------------------- Search Logic---------------------------- #
def search():
    website = input_website.get()
    try:
        with open("C:\\Users\\ASUS\\Documents\\ANDU\\Python\\Study Project\\Password Manager\\data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message = "File not found.")
    except json.JSONDecodeError:
        messagebox.showinfo(title = "Error", message = f"No data about this {website}.") 
    else:        
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title = "Error", message = f"No data about this {website}.") 

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

input_website = Entry(width = 33)
input_website.grid(column = 1, row = 1)
input_website.focus()

search_button = Button(text = f"Search", width = 16, highlightthickness = 0, command = search)
search_button.grid(column = 2, row = 1)

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