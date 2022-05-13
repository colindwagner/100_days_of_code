from tkinter import *
from tkinter import messagebox
import random

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    generated_password = []

    for letter in range(0, 4):
        generated_password.append(letters[random.randint(0,len(letters)-1)])

    for symbol in range(0, 4):
        generated_password.append(symbols[random.randint(0,8)])

    for number in range(0, 4):
        generated_password.append(numbers[random.randint(0,9)])

    random.shuffle(generated_password)
    password = ''.join(generated_password)
    pyperclip.copy(password)
    password_tb.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_clicked():
    website = website_tb.get()
    username = username_tb.get()
    password = password_tb.get()

    #validate
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(message="Please fill out all entries")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n {website} \n {username} \n {password}\n Is it okay to save?")
        
        if is_ok:
            with open(f"passwords.txt", mode="a") as password_file:
                password_file.writelines(f"{website} | {username} | {password}\n")
                clear_entires()
        

def clear_entires():
   website_tb.delete(0, END)
   password_tb.delete(0, END)
   website_tb.focus()

# ---------------------------- UI SETUP ------------------------------- #

#--window--#
window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40)

#--bg---#
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0)

#--labels--#

# website label
website_label = Label(text="Website: ", font=("Arial", 10))
website_label.grid(column=0,row=1)

# username label
username_label = Label(text="Email/Username: ", font=("Arial", 10))
username_label.grid(column=0,row=2)

# password label
password_label = Label(text="Password: ", font=("Arial", 10))
password_label.grid(column=0,row=3)

#--textboxes--#
website_tb = Entry(width=35)
website_tb.grid(column=1,row=1, columnspan=2, sticky='w')
website_tb.focus()

username_tb = Entry(width=35)
username_tb.grid(column=1,row=2, columnspan=2, sticky='w')
username_tb.insert(0, "colin@email.com")

password_tb = Entry(width=21)
password_tb.grid(column=1,row=3, sticky='w')

#--buttons--#

password_btn = Button(text="Generate Password", font=("Arial, 8"), command=password_generator)
password_btn.grid(column=1,row=3, sticky='e')

add_btn = Button(text="Add",width=30, command=add_clicked)
add_btn.grid(column=1,row=4, columnspan=2)

window.mainloop()