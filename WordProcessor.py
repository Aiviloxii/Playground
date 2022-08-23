from tkinter import *
import re
from tkinter import messagebox as mb
#functions.
def search():
    x = txt.get(1.0, "end-1c")
    s = e1.get()
    a = re.search(s, x)
    if a:
        mb.showinfo('MESSAGE',f"The word {s} is found in the text.")
    else:
        mb.showwarning('MESSAGE', 'Word not found!')

def replace():
    x = txt.get(1.0, END)
    y = e1.get()
    z = e2.get()
    rep = re.sub(y, z, x)
    mb.showinfo('MESSAGE', 'Successful!')
    txt.delete(1.0, END)
    txt.insert(INSERT, rep)

def counter():
    x = txt.get(1.0, END)
    wc = re.split(" ", x)
    w = len(wc)
    mb.showinfo('MESSAGE', f"The number of words are {w}")

def lines():
    x = txt.get(1.0, END)
    n = re.findall("\n", x)
    mb.showinfo('MESSAGE', f'The total number of lines are: {len(n)}')

def getAll():
    x = txt.get(1.0, END)
    s = e1.get()
    sa = re.findall(s, x)
    mb.showinfo('MESSAGE', f"The word {s} is found at {len(sa)} positions.")
# create main window.
wp = Tk()
wp.title("WORD PROCESSOR")
wp.geometry("800x500")
#==============CREATE WIDGETS==============================================================
#==========frames=====================================
f1 = Frame(wp, width=800, height=60, bg="dark gray")
f2 = Frame(wp, width=800, height=280, bg="white")
f3 = Frame(wp, width=800, height=160, bg="dark gray")
#===============labels================================
h = Label(f1, text="WORD PROCESSOR", bg="dark gray", font=('Segoe UI Black', 30), fg="white")
# ==============textbox===============================
txt = Text(f2, width=450, height=250, font=('Fixedsys', 17), fg="cyan")
e1 = Entry(f3, font=('verdana', 14))
e2 = Entry(f3, font=('verdana', 14))
#===============buttons===============================
b1 = Button(f3, text="Search",  activeforeground="indigo", activebackground="pink", bg="teal", fg="white", font=('verdana', 14), bd=3, command=search)
b2 = Button(f3, text="Replace",  activeforeground="indigo", activebackground="pink", bg="teal", fg="white", font=('verdana', 14),bd=3, command=replace)
b3 = Button(f3, text="Word Count",  activeforeground="indigo", activebackground="pink", bg="teal", fg="white", font=('verdana', 14),bd=3, command=counter)
b4 = Button(f3, text="Line Count",  activeforeground="indigo", activebackground="pink", bg="teal", fg="white", font=('verdana', 14),bd=3, command=lines)
b5 = Button(f3, text="Search All",  activeforeground="indigo", activebackground="pink", bg="teal", fg="white", font=('verdana', 14),bd=3, command=getAll)
#=========add widgets to window.============
f1.pack()
f2.pack()
f3.pack()
h.pack(pady=10)
txt.pack()
e1.pack(pady=7)
b1.pack(pady=7)
e2.pack(side="left", padx=5)
b2.pack(side="left", padx=5)
b3.pack(side="left", padx=5)
b4.pack(side="left", padx=5)
b5.pack(side="left", padx=4)
f1.pack_propagate(0)
f2.pack_propagate(0)
f3.pack_propagate(0)
txt.pack_propagate(0)
#========run app===========
wp.mainloop()