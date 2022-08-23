# A countdown app using Tkinter and threads.
from tkinter import *
from tkinter import messagebox as mb
import _thread as trd
import time
def print_time(threadName, endTime):
    count = 0
    while endTime >0:
        time.sleep(1)
        timerLabel.config(text=endTime)
        endTime -= 1
    mb.showwarning('Time Message', 'Time Up!!')

def guiCount():
    data = inputE.get()
    if len(data) > 0:
        try:
            trd.start_new_thread(print_time,("Timer", int(data)))
        except:
            mb.showerror("Error Message", "Error: unable to start thread")
    else:
        mb.showerror("Error Mesaage", "Error: enter Finish Time.")

counter = Tk()
counter.geometry("700x350")
counter.title("COUNTDOWN")
#Frames
f1 = Frame(counter, width=700, height=50, bg="#f9dff8")
f1.pack()
f1.pack_propagate(0)
f2 = Frame(counter, width=700, height=100, bg="#f9dff8")
f2.pack()
f2.pack_propagate(0)
f3 = Frame(counter, width=700, height=200, bg="#f9dff8")
f3.pack()
f3.pack_propagate(0)
#Labels
h = Label(f1, text="COUNTDOWN APP", bg="#f9dff8", fg="black",font=('verdana', 20, 'bold'))
h.pack()
h1 = Label(f2, text="Enter Finish Time here:", bg="#f9dff8", fg="black",font=('verdana', 15, 'bold'))
h1.pack(side="left", pady=4,padx=35, anchor="ne")
timerLabel = Label(f3, text="Begin!", bg="#f9dff8", fg="black",font=('verdana', 90, 'bold'))
timerLabel.pack(side="bottom")
#Entry
inputE = Entry(f2, font=('arial', 15, 'bold'), bd=4, justify="left")
inputE.pack(side="left", pady=4, anchor="ne")
#Button
s = Button(f3, text="Start", bg="#991e96", fg="black", bd=3, font=('cursive', 20, 'bold'), command=guiCount)
s.pack()
#runapp
counter.mainloop()