import tkinter as tk
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
CHECKMARK = '✓'

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global timer
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text='TIMER', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'), pady=30)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if 1st/3rd/5th/7th rep , work_sec
    if reps in [1, 3, 5, 7]:
         count_down(work_sec)
         timer_label.config(text='WORK', fg=GREEN)
    
    #if 8th rep, long break
    elif reps==8:
        reps = 0
        timer_label.config(text='LONG BREAK', fg=RED)
        count_down(long_break_sec)

    #if 2nd, 4th, 6th short break
    elif reps in [2,4,6]:
        timer_label.config(text='SHORT BREAK', fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer

    #format timer (00:00)
    count_min = str(math.floor(count/60))
    count_sec = str(count % 60)

    if len(count_sec)<2:
        count_sec = '0' + count_sec
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        mark = ""
        for _ in range (0, work_sessions):
            mark += CHECKMARK
        checkmark_label.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('POMODORO')
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = tk.Label(text='TIMER', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'), pady=30)
timer_label.grid(row=0, column=1)

#tomato
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
p_image = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=p_image)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)


#buttons
start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

#checkmarks
checkmark_label = tk.Label(text="", fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()