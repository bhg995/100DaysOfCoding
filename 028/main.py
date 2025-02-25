from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
DarkGreen = "#1D1616"
Gray = "#3C3D37"
LightGreen = "#697565"
Khaki = "#ECDFCC"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
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
        title_label.config(text="Take a longer break", fg=DarkGreen)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Take a short break", fg=Gray)
    else:
        count_down(work_sec)
        title_label.config(text="Get down on it", fg=LightGreen)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for n in range(work_sessions):
            marks += "✅"
        check_marks.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tomatoe")
window.config(padx=100, pady=75, bg=Khaki)


title_label = Label(text="Timer", background=Khaki, fg=LightGreen, font=(FONT_NAME, 45))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200,height=224, bg=Khaki, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 129, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=3, row=2)

check_marks = Label(fg=LightGreen, bg=Khaki,highlightthickness=0)
check_marks.grid(column=1, row=3)


window.mainloop()
