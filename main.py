import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#00FF00"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.1
# ---------------------------------------------------------------------- #

reps = 0
timer_on = False


def start_timer():
    global reps, timer_on
    timer_on = True
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    cycles.config(text=f"{int((reps - 1) / 2)*CHECKMARK}")

    if reps > 8:
        timer_on = False
        cycles.config(text="")
        timer_label.config(text="Pomodoro!", fg=GREEN)

    elif reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break!", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break!", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work!", fg=GREEN)


def countdown(seconds):
    if not timer_on:
        return

    minutes = int(math.floor(seconds / 60))
    seconds = int(seconds % 60)

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")

    seconds = int(minutes) * 60 + int(seconds)

    if seconds > 0:
        window.after(1000, countdown, seconds - 1)
    else:
        start_timer()


def start():
    global timer_on
    if not timer_on:
        timer_on = True
        start_timer()


def reset():
    global reps, timer_on
    reps = 0
    timer_on = False
    canvas.itemconfig(timer, text="00:00")
    timer_label.config(text="Pomodoro!", fg=GREEN)
    cycles.config(text="")


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tk.Label(text="Pomodoro!", font=(FONT_NAME, 28), bg=YELLOW, fg=GREEN)
timer_label.config(pady=10)
timer_label.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

cycles = tk.Label(text="", font=(FONT_NAME, 14), bg=YELLOW, fg=GREEN)
cycles.config(pady=30)
cycles.grid(column=1, row=2)

start_button = tk.Button(text="Start", font=(FONT_NAME, 14), bg=YELLOW, command=start, activebackground=YELLOW, borderwidth=0)
start_button.grid(column=0, row=2)

reset_button = tk.Button(text="Reset", font=(FONT_NAME, 14), bg=YELLOW, command=reset, activebackground=YELLOW, borderwidth=0)
reset_button.grid(column=2, row=2)

window.mainloop()
