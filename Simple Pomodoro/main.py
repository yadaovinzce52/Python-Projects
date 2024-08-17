from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_window = ''


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer_window, reps

    check.config(text='')
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer', fg=GREEN)
    reps = 0

    if timer_window:
        window.after_cancel(timer_window)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        timer_label.config(text='Work', fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_window
    mins = count // 60
    if mins < 10:
        mins = f'0{mins}'
    second = count % 60
    if second < 10:
        second = f'0{second}'

    canvas.itemconfig(timer_text, text=f'{mins}:{second}')
    if count > 0:
        timer_window = window.after(1000, count_down, count - 1)
    else:
        start()
        text = '✔' * (reps // 2)
        check.config(text=text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', highlightthickness=0, command=start)
start_button.grid(row=2, column=0)

reset = Button(text='Reset', highlightthickness=0, command=reset)
reset.grid(row=2, column=2)

check = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 10, 'bold'))
check.grid(row=3, column=1)

window.mainloop()
