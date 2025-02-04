import math
import sys
from tkinter import *
from datetime import datetime
import os
import pygame
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CONGRATS = "#05e7f7"

WORK_MIN = 25 * 60
#25
SHORT_BREAK_MIN = 5 * 60
#5
LONG_BREAK_MIN = 20 * 60
#20
reps = 0
timer = NONE
current_time = datetime.now()
total_session_completed = 0

pygame.mixer.init()


# ---------------------------- GET RESOURCE PATH ------------------------------- #
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and PyInstaller EXE. """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.join(base_path, relative_path)


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    reps = 0

def record_started_time():
    global  current_time
    current_time = datetime.now()
    start_time_label.config(text=f"Start time: {current_time.strftime('%H:%M:%S')}")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global total_session_completed
    reps += 1
    if reps % 8 == 0:  # Long break after 4 work sessions
        play_sound()
        count_down(LONG_BREAK_MIN)
        timer_label.config(text="Long Break", fg=RED)
    elif reps > 8:
        timer_label.config(text="Finished 🎉", fg=CONGRATS)
        total_session_completed += 1
        session_completed.config(text=f"Session Completed : {total_session_completed * '⭐' if total_session_completed > 0 else 0}")
        reps = 0
    elif reps % 2 == 0:
        play_sound()
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text="Break",fg=PINK)
    else:
        timer_label.config(text="Work",fg=GREEN)
        count_down(WORK_MIN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = int(count / 60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        bring_to_front()
        start_timer()
        work_sessions = math.floor(reps/2)
        check_marks.config(text="✔" * work_sessions)


# ---------------------------- PLAY SOUND NOTIFICATION ------------------------------- #
def play_sound():
    sound_file = "break.mp3"  # Replace with an actual sound file
    if os.path.exists(sound_file):
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

# ---------------------------- BRING WINDOW TO FRONT ------------------------------- #
def bring_to_front():
    window.deiconify()
    window.lift()
    window.attributes('-topmost', 1)  # Bring window to top
    window.focus_force()
    window.attributes('-topmost', 0)  # Reset to avoid staying always on top

# ---------------------------- UPDATE CURRENT TIME ------------------------------- #
def update_current_time():
    global current_time
    current_time = datetime.now().strftime("%H:%M:%S")
    current_time_label.config(text=f"Current Time: {current_time}")
    window.after(1000, update_current_time)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("POMODORO")
window.config(bg=YELLOW,padx=20,pady=20)

start_time_label = Label(text=f"Start time: start to begin",fg="#000", bg=YELLOW, font=(FONT_NAME, 10))
start_time_label.grid(row=0, column=0,sticky="w")

current_time_label = Label(text="Current Time:",fg="#000", bg=YELLOW, font=(FONT_NAME, 10))
current_time_label.grid(row=1, column=0,sticky="w")

session_completed = Label(text=f"Session Completed : {total_session_completed * '⭐' if total_session_completed > 0 else 0}",fg="#000", bg=YELLOW, font=(FONT_NAME, 10))
session_completed.grid(row=2, column=0, sticky="w")

update_current_time()



timer_label = Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(row=3, column=1)




canvas = Canvas(width=210, height=250, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(103,112,image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(row=4, column=1)



start_btn = Button(text="Start",highlightthickness=0, command=lambda: (start_timer(), record_started_time()))
start_btn.grid(row=5, column=0, sticky="e")

reset_btn = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_btn.grid(row=5,column=2,padx=(0,150))



check_marks = Label(fg=GREEN, font=(FONT_NAME, 12,"bold"), bg=YELLOW)
check_marks.grid(row=6,column=1)


window.mainloop()