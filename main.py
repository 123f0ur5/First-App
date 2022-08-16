from tkinter import ACTIVE, DISABLED, Button, Label, Tk

window = Tk()

#Setting Variables
running = True
hour = 0; minute = 0; second = 0

#Function called by Start Button to start the stopwatch
def start_time():
    global running
    running = True
    btn_Start.config(state=DISABLED)
    count_time()

#Function that count time
def count_time():
    global second; global minute; global hour; global running
    if running:
        label_Time.config(text=f'{hour:02d}:{minute:02d}:{second:02d}')
        if second < 59:
            second += 1
        elif second == 59:
            second = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
        #Call method after that wait 1000ms and call count_time()
        window.after(1000, count_time)

#Function that reset time, and set Start button to active       
def reset_time():
    global hour; global minute; global second
    label_Time.config(text='00:00:00')
    hour = 0; minute = 0; second = 0
    btn_Start.config(state=ACTIVE)
    pause_time()

#Function that pauses the count and also re-active the start button
def pause_time():
    global running
    running = False
    btn_Start.config(state=ACTIVE)

window.title("Stopwatch")
window.configure(width='335', height='200')
window.minsize(335,200)
window.maxsize(335,200)
#Setting the display
label_Time = Label(window, text='00:00:00', fg='Blue', font=('',33))
label_Time.place(x=85, y=50)
#setting the start button
btn_Start = Button(window, text='Start', font=('',12), width='7', height='2', command=start_time)
btn_Start.place(x = 10, y = 130)
#setting pause button
btn_Pause = Button(window, text='Pause', font=('',12), width='7', height='2', command=pause_time)
btn_Pause.place(x = 90, y = 130)
#setting reset button
btn_Reset = Button(window, text='Reset', font=('',12), width='7', height='2', command=reset_time)
btn_Reset.place(x = 170, y = 130)
#setting exit button
btn_Exit = Button(window, text='Exit', font=('',12), width='7', height='2', command=quit)
btn_Exit.place(x = 250, y = 130)
window.mainloop()