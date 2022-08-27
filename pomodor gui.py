from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text , text = "00:00")
    title_label.config(text = "Timer")
    check_mark.config(text = "")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    reps += 1
    work_secs = WORK_MIN*60
    BREAK_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    
    
    if reps%8 ==0:
        count_down(long_break_sec)
        title_label.config(text = "BREAK" , fg = RED)
         
    elif reps%2 == 0:
        count_down(BREAK_sec)
        title_label.config(text = "BREAK" , fg = PINK)
    else:
        count_down(work_secs)
        title_label.config(text = "WORK" , fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec< 10:
        count_sec =     f"0{count_sec}"
    
    canvas.itemconfig(timer_text , text = f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down , count-1) 
         
    else:
        start_timer()
        mark = ""
        work_session= math.floor(reps/2)
        for _ in range(work_session): 
            mark+= "✔️" 
        check_mark.config(text = mark)
            
  # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx = 100, pady =50 , bg = YELLOW ,highlightthickness=0)


title_label = Label(text = "Timer" ,fg = GREEN ,bg = YELLOW,font = (FONT_NAME,40)) 
title_label.grid(column = 1, row = 0)



canvas = Canvas(width =200 , height = 224 , bg = YELLOW) 
tomato__img = PhotoImage(file = "/Users/mohit/Desktop/ LINKS/255 pomodoro-start/tomato.png")
canvas.create_image(103,112, image = tomato__img) 
timer_text = canvas.create_text(103,130, text = "00:00" , fill ="white" , font = (FONT_NAME , 35 , "bold") )
canvas.grid(column = 1, row = 1)



start_button = Button(text = "START" ,highlightthickness=0 , command = start_timer)
start_button.grid(column=0,row=2)


reset_button = Button(text = "RESET" ,highlightthickness=0 , command = reset_timer)
reset_button.grid(column=2,row=2)


check_mark = Label( fg= GREEN, bg= YELLOW) 
check_mark.grid(column = 1, row = 3) 
window.mainloop()