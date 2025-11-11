from itertools import count
from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK     = "#e2979c"
RED      = "#e7305b"
GREEN    = "#9bdeac"
YELLOW   = "#f7f5dd"
BLUE     = "#a2d2ff"
PURPLE   = "#c8b6ff"
ORANGE   = "#ffb4a2"
TEAL     = "#80ed99"
LAVENDER = "#d8e2dc"
PEACH    = "#ffd6a5"
MINT     = "#b5ead7"
GRAY     = "#dee2e6"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_mechanism():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text = f"{00}:{00}")
    label1.config(text = "TIMER")
    label2.config(text = "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
   global reps
   reps += 1
   work_sec = WORK_MIN * 60
   short_break_sec = SHORT_BREAK_MIN * 60
   long_break_sec = LONG_BREAK_MIN * 60
   if reps%8 ==0:
        canvas.configure(background=LAVENDER)
        window.config(padx=100, pady=50, bg=LAVENDER)
        label1.config(text="Long break session", fg = PEACH,bg = LAVENDER)
        countdown(long_break_sec)
   elif reps %2 ==0:
        canvas.configure(background=BLUE)
        window.config(padx=100, pady=50, bg=BLUE)
        label1.config(text="Short break session", fg = TEAL,bg = BLUE)
        countdown(short_break_sec)
   else:
        canvas.configure(background=GREEN)
        window.config(padx=100, pady=50, bg=GREEN)
        label1.config(text="Work session", fg = RED,bg = GREEN)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_mins = int(count/60)
    count_secs = round(count%60,2)
    if count_secs < 10:
        count_secs = "0" + str(count_secs)
    canvas.itemconfig(timer_text,text = f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps %2==0:
            mark="✔"
            label2.config(text= (mark*(int(reps/2))))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50,bg = YELLOW)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(window, width=200, height=224,bg = YELLOW,highlightthickness=0)
canvas.create_image(100,112,image = tomato)
timer_text = canvas.create_text(100,130,text = "00:00", font = (FONT_NAME,35,"bold"), fill = "white")
canvas.grid(column = 1, row = 1)


label1 = Label(window, text = "TIMER", font = (FONT_NAME,35,"bold"))
label1.grid(column=1, row =0)
label1.config(bg=YELLOW,fg=GREEN)

label2 = Label(window, text = "",font = ("Ariel",15,"bold"))
label2.grid(column=1, row=3)
label2.config(bg=YELLOW,fg=GREEN)

button_start = Button(window, text = "Start", font = ("Ariel",10,"normal"),highlightthickness =0,command = start_timer)
button_start.grid(column=0, row = 2)

button_reset = Button(window, text = "Reset", font = ("Ariel",10,"normal"),highlightthickness =0,command = reset_mechanism)
button_reset.grid(column=2, row = 2)

window.mainloop()