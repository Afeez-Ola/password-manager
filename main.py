import tkinter as tk
from tkinter import messagebox
from random import *
import pyperclip
import string
import json


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    try:
        with open("data.json", "r") as dataFile:
            data = json.load(dataFile)
            keys = list(data.keys())
            for key in keys:
                if website_input.get() in key:
                    messagebox.showinfo(title=f"{website_input.get()} data", message=f"Email: {data[key]['email']}\nPassword:{data[key]['password']} ")
                else:
                    messagebox.showerror(title="Error", message=f"There's no data for {website_input.get()}")
    except FileNotFoundError:
        print("File not found!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.delete(0, tk.END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = id_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title="Oops", message=f"Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as dataFile:
                data = json.load(dataFile)

        except FileNotFoundError:
            with open("data.json", "w") as dataFile:
                json.dump(new_data, dataFile, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as dataFile:
                json.dump(data, dataFile, indent=4)
        finally:
            website_input.delete(0, tk.END)
            id_input.delete(0, tk.END)
            id_input.insert(0, "@gmail.com")
            password_input.delete(0, tk.END)
            website_input.focus_set()


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# The Label UI
website_label = tk.Label(text="Website:", font=("Arial", 12))
website_label.grid(column=0, row=1)

id_label = tk.Label(text="Email/Username:", font=("Arial", 12), pady=12)
id_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:", font=("Arial", 12), padx=12)
password_label.grid(column=0, row=3)

# The input UI
website_input = tk.Entry(width=35)
website_input.focus_set()
website_input.grid(column=1, row=1, columnspan=2)

id_input = tk.Entry(width=35)
id_input.insert(0, "@gmail.com")
id_input.grid(column=1, row=2, columnspan=2)

password_input = tk.Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2)

# The Button UI
search_button = tk.Button(text="Search", width=13,command=search_password)
search_button.grid(column=3, row=1,padx=7)

generate_button = tk.Button(text="Generate Password",width=13, command=generate_password)
generate_button.grid(column=3, row=3,padx=7)

add_button = tk.Button(text="Add", width=39, justify="center", command=save_password)
add_button.grid(column=1, row=4, columnspan=3,pady=12 )

window.mainloop()
