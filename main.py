from tkinter import *
import math
from turtle import color

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    header_text.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        header_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        header_text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        header_text.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps > 0:
            check_marks = ""
            work_sessions = math.floor(reps/2)
            for time in range(work_sessions):
                check_marks += "✓"
            check.config(text=check_marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


header_text = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
header_text.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

button_start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
button_start.grid(column=1, row=3)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=2, row=4)

button_reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
button_reset.grid(column=3, row=3)


window.mainloop()
