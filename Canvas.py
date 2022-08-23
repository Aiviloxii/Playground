# Create a canvas that shows only one shape at a time.
from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
def clear():
    vas.delete("all")
def drawCircle():
    clear()
    vas.create_oval(300, 300, 20, 20, fill="cyan", outline="#000000")
def drawRect():
    clear()
    vas.create_rectangle(450, 300, 10, 10, fill="indigo", outline="black")

def drawImage():
    clear()
    vas.create_image(90, 35, anchor=NW, image=s)


def drawArc():
    clear()
    vas.create_arc(400, 400, 5, 10, fill="brown", outline="grey")

def drawLines():
    clear()
    vas.create_line(400,400, 25, 25, fill="green")
def save():
    b = mb.askyesno('Confirm', 'Do you wish to save your work')
    if b==1:
        mb.showinfo("SUCESS", 'SAVED!!')
def close():
    c = mb.askyesno( 'WARNING', 'Are you sure you want to close the program?')
    if c ==1:
        can.destroy()
def about():
    text="This an app that displays\ndifferent shapes,lines\nand images."
    mb.showinfo('ABOUT', text)
def tutorials():
    txt = "Watch videos on how to\nto use this application\nat gregicthub.net"
    mb.showinfo('Tutes', txt)
def comment():
    mb.showinfo('Feedback', 'Send any feedback\nvia greghub.org')
def discuss():
    mb.showinfo('Discussion', 'Feel free to join our Discord page\nat gregdrawboard@discord.com\nto interact with other users.')

can = Tk()
can.title("Drawboard")
can.geometry("800x600")
# Frames
f1 = Frame(can, width=800, height=80, bd=5, bg="blue")
f2 = Frame(can, width=800, height=100, bd=5, bg="#117fbe")
f3 = Frame(can, width=800, height=420, bg="#ffffff")
# Label
d = Label(f1, text="DRAWBOARD", bg="blue", fg="white", font=('Palatino Linotype',29))
# Buttons
but = Button(f2, text="Circle", bg="blue", fg="silver", font=('Comic Sans MS',16), command=drawCircle)
but1 = Button(f2, text="Rectangle", bg="blue", fg="silver", font=('Comic Sans MS',16), command=drawRect)
but2 = Button(f2, text="ARC", bg="blue", fg="silver", font=('Comic Sans MS',16), command=drawArc)
but3 = Button(f2, text="Line", bg="blue", fg="silver", font=('Comic Sans MS',16), command=drawLines)
but4 = Button(f2, text="Image", bg="blue", fg="silver", font=('Comic Sans MS',16), command=drawImage)
# Canvas
vas = Canvas(f3, width=500, height=500, bd=5, bg="#abeebd")
s=PhotoImage(file='Sonics.gif')
# menus
menubar = Menu(can)
# File
filemenu = Menu(menubar)
filemenu.add_command(label='New', command=clear)
filemenu.add_separator()
filemenu.add_command(label='Save', command=save)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=close)
menubar.add_cascade(label='FILE', menu=filemenu)
# Help
helpmenu = Menu(menubar)
helpmenu.add_command(label='About', command=about)
helpmenu.add_separator()
helpmenu.add_command(label='Tutorials', command=tutorials)
menubar.add_cascade(label='HELP', menu=helpmenu)
# Feedback
fbmenu = Menu(menubar)
fbmenu.add_command(label='Send Feedback', command=comment)
fbmenu.add_separator()
fbmenu.add_command(label='Join our Forum', command=discuss)
menubar.add_cascade(label='FEEDBACK', menu=fbmenu)
can.configure(menu=menubar)

f1.pack()
f2.pack()
f3.pack()
f1.pack_propagate(0)
f2.pack_propagate(0)
f3.pack_propagate(0)
d.pack()
but.pack(side="left")
but1.pack(side="left", padx=10)
but2.pack(side="left",padx=8)
but3.pack(side="left", padx=5)
but4.pack(side="left", padx=5)
vas.pack()
can.mainloop()