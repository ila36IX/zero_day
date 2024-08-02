from tkinter import *
import itertools

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = (0,5,"Work",GREEN)
SHORT_BREAK_MIN = (0,3,"Break",PINK)
LONG_BREAK_MIN = (0,10, "Break:)",RED)
breaks=2
id_after=None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global id_after, many, cycled_periods
    window.after_cancel(id_after)
    many=0
    progress_label.config(text="")
    state_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    cycled_periods=itertools.cycle(circle)
    start_button.config(command=lambda :timer(*next(cycled_periods)))


# ---------------------------- TIMER MECHANISM ------------------------------- #

circle = [ *([WORK_MIN, SHORT_BREAK_MIN]*breaks) ,WORK_MIN ,LONG_BREAK_MIN]
cycled_periods = itertools.cycle(circle)

many=0

def change_timer(state):
    timer(*next(cycled_periods))
    global many
    if state=="Work":
        many +=1
        progress_label.config(text="X"*many)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def timer(m, s, state, color):
    start_button.config(command="")
    state_label.config(text=state, fg=color)

    if s<10  :
        s="0"+str(s)
    if m<10 :
        m="0"+str(m)

    canvas.itemconfig(timer_text, text=f"{m}:{s}")
    s=int(s)
    m=int(m)
    s -= 1
    if s==-1 and m==0:
        return change_timer(state)

    if s==-1 :
        s=59
        m-=1
    global id_after
    id_after=window.after(1000, lambda x=m,y=s,z=state,Z=color: timer(x,y,z,Z))

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Promodo")
window.maxsize(width=550,height=450)
window.minsize(width=550, height=450)
window.config(padx=100,pady=50)
window.config(bg=YELLOW)


canvas= Canvas(width=200, height=238, bg=YELLOW, highlightthickness=0)

tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100, 117, image=tomato_image)

timer_text=canvas.create_text(100, 135, fill="white",text="00:00", font=(FONT_NAME, 25,"bold"))
canvas.grid(row=1, column=1)


state_label=Label(text="Timer",bg=YELLOW,fg=GREEN ,font=(FONT_NAME, 40,"bold"))
state_label.grid(column=1 ,row=0)

start_button=Button(text="Start", padx=20, pady=5, command=lambda :timer(*next(cycled_periods)))
start_button.grid(row=2, column=0)

reset_button=Button(text="Reset", padx=20, pady=5, command=reset)
reset_button.grid(row=2, column=2)

progress_label=Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME,17,"bold"))
progress_label.grid(row=3, column=1)







window.mainloop()
