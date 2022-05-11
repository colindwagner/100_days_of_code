
from tkinter import *
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
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = SHORT_BREAK_MIN*60

    if REPS % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="LONG BREAK",fg=RED)
    elif REPS % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="SHORT BREAK", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    if count_sec <= 9:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown, count-1)
    elif count == 0:
        start_timer()
        marks = ""
        for _ in range(math.floor(REPS/2)):
            marks += "✓"
        check_label.config(text=marks, fg=GREEN)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,122, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)


#timer label
timer_label = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35,"bold"))
timer_label.grid(column=2, row=1)

#start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1,row=3)

#reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3,row=3)

#checkmark button
check_label = Label(text="", fg=GREEN)
check_label.grid(column=2,row=4)

window.mainloop()