# python3 week-3/password-manager-day29/main.py

from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    input_pass.delete(0, END)

    letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' 
    ]
    symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}", "\\", "|", ";", ":", "'", '"', ",", ".", "/", "<", ">", "?", "`", "~"
    ]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    password_list = []

    for _ in range(random.randint(6, 10)):
        password_list.append(random.choice(letters))

    for _ in range(random.randint(3, 5)):
        password_list.append(random.choice(symbols))

    for _ in range(random.randint(3, 5)):
        password_list.append(random.choice(numbers))

    random.shuffle(password_list)
    password = ''.join(password_list) 

    input_pass.insert(0, password)   


# ---------------------------- SAVE PASSWORD ------------------------------- #

def append_data():
    # grab the enteries data into vars
    site_name = input_site.get()
    user = input_user.get()
    password = input_pass.get()

    if len(site_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please enter all feilds")
        return

    is_ok = messagebox.askokcancel(title=site_name, message=f"Email: {user}\nPassword: {password}\n Is this ok?")

    if is_ok:
        # NOTE -> if running from the project dir
        # with open("data.txt", "a") as file:
        #    
        # NOTE -> if running from the home/ root dir
        with open("week-3/password-manager-day29/data.txt", "a") as file:

            # append the data to the file
            file.write(f"{site_name} | {user} | {password}\n")   

            # reset the input enteries and set cursor back to website entery
            input_site.delete(0, END)
            input_pass.delete(0, END) 
            input_site.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# NOTE -> for static images it is better to use a label, if more interactivity is neaded use canvas
# img = PhotoImage(file="week-3/password-manager-day29/logo.png", width=200, height=200) 
# label_img = Label(image=img)
# label_img.pack()

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="week-3/password-manager-day29/logo.png") # NOTE -> running from the home dir, if running from project dir use "logo.png"
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
label_site = Label(text="Website:")
label_site.grid(row=1, column=0)

label_user = Label(text="Email/Username:")
label_user.grid(row=2, column=0)

label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

# Enteries
input_site = Entry(width=35)
input_site.focus()
input_site.grid(row=1, column=1, columnspan=2)


input_user = Entry(width=35)
input_user.insert(0, "default@gmail.com") # (index(pos), text)
input_user.grid(row=2, column=1, columnspan=2)


input_pass = Entry(width=21)
input_pass.grid(row=3, column=1)

# Buttons
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=append_data)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()