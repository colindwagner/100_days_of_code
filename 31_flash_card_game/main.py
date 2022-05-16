from cgitb import text
from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
random_entry = {}
to_learn = {}

#import csv data
try:
    es_csv = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    es_csv = pd.read_csv("./data/es.csv")
finally:
    to_learn = es_csv.to_dict(orient="records")


def next_card():
    global random_entry, flip_timer
    window.after_cancel(flip_timer)
    random_entry = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=random_entry["Spanish"], fill="black")
    canvas.itemconfig(bg_image, image=fcard_img)
    flip_timer = window.after(3000, func=flip_card)
    

def flip_card():
    canvas.itemconfig(bg_image, image=bcard_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_entry["English"], fill="white")

def remove_entry():
    to_learn.remove(random_entry)
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

#--window--#
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

#--bg---#
canvas = Canvas(width=800, height=526)
fcard_img = PhotoImage(file="./images/card_front.png")
bcard_img = PhotoImage(file="./images/card_back.png")
bg_image = canvas.create_image(400,263, image=fcard_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0,row=0, columnspan=2)

#buttons
correct_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=next_card)
correct_button.grid(column=1,row=1)

incorrect_image = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=incorrect_image, highlightthickness=0, command=remove_entry)
incorrect_button.grid(column=0,row=1)

#create first card to avoid defaults
next_card()

window.mainloop()