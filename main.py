from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = id_input.get()
    password = password_input.get()
    data = f"{website} | {email} | {password}\n"

    is_true = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}\nPassword:{password}")
    if is_true:
        with open("data.txt", "a") as dataFile:
            dataFile.writelines(data)
        website_input.delete(0,END)
        id_input.insert(0, "@gmail.com")
        password_input.delete(0, END)
        website_input.focus_set()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0, )

# The Label UI
website_label = Label(text="Website:", font=("Arial", 12), )
website_label.grid(column=0, row=1)

id_label = Label(text="Email/Username:", font=("Arial", 12), pady=12, )
id_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=("Arial", 12), padx=12, )
password_label.grid(column=0, row=3)

# The input UI
website_input = Entry(width=35)
website_input.focus_set()
website_input.grid(column=1, row=1, columnspan=2)

id_input = Entry(width=35)
id_input.insert(0, "@gmail.com")
id_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=35)
password_input.grid(column=1, row=3, columnspan=2)

# The Button UI
generate_button = Button(text="Generate Password", )
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, justify="center",command=save_password)
add_button.grid(column=1, row=4, columnspan=3, pady=12, )

window.mainloop()
