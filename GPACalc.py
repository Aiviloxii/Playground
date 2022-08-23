# GPA calculator
from tkinter import *
# Function to clear the values.
def clear():
    gr1.set("")
    gr2.set("")
    gr3.set("")
    gr4.set("")
    gr5.set("")
    sc.set("")
    sc1.set('')
    sc2.set('')
    sc3.set('')
    sc4.set('')
# Function to calculate scores and give grades.
def calc():
    x = int(gr1.get())
    y = int(gr2.get())
    z = int(gr3.get())
    a = int(gr4.get())
    c = int(gr5.get())
    d = int(gr6.get())
    e = int(gr7.get())
    f = int(gr8.get())
    h = int(gr9.get())
    if 70 <= x < 101:
        sc.set('A')
    elif 56 <= x < 69:
        sc.set('B')
    elif 50 <= x < 54:
        sc.set('C')
    elif 40 <= x < 50:
        sc.set('D')
    elif 30 <= x < 40:
        sc.set('E')
    else:
        sc.set('F')
    if 70 <= y < 101:
        sc1.set('A')
    elif 56 <= y < 69:
        sc1.set('B')
    elif 50 <= y < 55:
        sc1.set('C')
    elif 40 <= y < 50:
        sc1.set('D')
    elif 30 <= y < 40:
        sc1.set('E')
    else:
        sc1.set('F')
    if 70 <= z < 101:
        sc2.set('A')
    elif 55 <= z < 69:
        sc2.set('B')
    elif 50 <= z < 55:
        sc2.set('C')
    elif 40 <= z < 50:
        sc2.set('D')
    elif 30 <= z < 40:
        sc2.set('E')
    else:
        sc2.set('F')
    if 70 <= a < 101:
        sc3.set('A')
    elif 55 <= a < 69:
        sc3.set('B')
    elif 50 <= a < 55:
        sc3.set('C')
    elif 40 <= a < 50:
        sc3.set('D')
    elif 30 <= a < 40:
        sc3.set('E')
    else:
        sc3.set('F')
    if 70 <= c < 101:
        sc4.set('A')
    elif 55 <= c < 69:
        sc4.set('B')
    elif 50 <= c < 55:
        sc4.set('C')
    elif 40 <= c < 50:
        sc4.set('D')
    elif 30 <= c < 40:
        sc4.set('E')
    else:
        sc4.set('F')
    if 70 <= d < 101:
        sc5.set('A')
    elif 55 <= d < 69:
        sc5.set('B')
    elif 50 <= d < 55:
        sc5.set('C')
    elif 40 <= d < 50:
        sc5.set('D')
    elif 30 <= d < 40:
        sc5.set('E')
    else:
        sc5.set('F')
    if 70 <= e < 101:
        sc6.set('A')
    elif 55 <= e < 69:
        sc6.set('B')
    elif 50 <= e < 55:
        sc6.set('C')
    elif 40 <= e < 50:
        sc6.set('D')
    elif 30 <= e < 40:
        sc6.set('E')
    else:
        sc6.set('F')
    if 70 <= f < 101:
        sc7.set('A')
    elif 55 <= f < 69:
        sc7.set('B')
    elif 50 <= f < 55:
        sc7.set('C')
    elif 40 <= f < 50:
        sc7.set('D')
    elif 30 <= f < 40:
        sc7.set('E')
    else:
        sc7.set('F')
    if 70 <= h < 101:
        sc8.set('A')
    elif 55 <= h < 69:
        sc8.set('B')
    elif 50 <= h < 55:
        sc8.set('C')
    elif 40 <= h < 50:
        sc8.set('D')
    elif 30 <= h < 40:
        sc8.set('E')
    else:
        sc8.set('F')


cal = Tk()
cal.title("CALCULATOR")
cal.geometry("1000x650")
cal.config(bg="royal blue")

# Labels for headings.
h1 = Label(cal, text="Welcome to GPA Calculator", bg="royal blue", fg="#ffe9dc", font=('cooper black',22))
txt = Label(cal, text="Fill in your scores", bg="royal blue", fg="yellow", font=('Arial',14))
css = Label(cal, text="Enter your courses", bg="royal blue", fg="#000000", font=('Arial',16))
s = Label(cal, text="CREDITS", bg="royal blue", fg="#000000", font=('Verdana',17))
pt = Label(cal, text="GRADES", bg="royal blue", fg="#000000", font=('Verdana',17))
gc = Label(cal, text="POINTS", bg="royal blue", fg="#000000", font=('Verdana',17))
gp = Label(cal, text="GPA:", bg="royal blue", fg="#ffffff", font=('Verdana',17))

n_ = StringVar()
n = Entry(cal, textvariable=n_, bg="royal blue", fg="black", font=('Segoe UI Semibold',14))
r_ = StringVar()
r = Entry(cal, textvariable=r_, bg="royal blue", fg="black", font=('Segoe UI Semibold',14))
g_ = StringVar()
g = Entry(cal, textvariable=g_, bg="royal blue", fg="black", font=('Segoe UI Semibold',14))
b_ = StringVar()
b = Entry(cal, textvariable=b_, bg="royal blue", fg="black", font=('Segoe UI Semibold',14))
p_ = StringVar()
p = Entry(cal, textvariable=p_, bg="royal blue", fg="black", font=('Segoe UI Semibold',14))
cv_ = StringVar()
cv = Entry(cal, textvariable=cv_, bg="royal blue", fg="black", font=('Segoe UI Semibold',14))
gpy_ = StringVar()
gpy = Entry(cal, textvariable=gpy_, bg="royal blue", fg="black", font=('Segoe UI Semibold',14))
ts_ = StringVar()
ts = Entry(cal, textvariable=ts_, bg="royal blue", fg="black", font=('Segoe UI Semibold',14))
fm_ = StringVar()
fm = Entry(cal, textvariable=fm_, bg="royal blue", fg="black", font=('Segoe UI Semibold',14))
# Entries for the  labels above.
gr1 = StringVar()
gr2 = StringVar()
gr3 = StringVar()
gr4= StringVar()
gr5= StringVar()
gr6= StringVar()
gr7= StringVar()
gr8= StringVar()
gr9= StringVar()
# Entries for the grades
sc = StringVar()
scr = Label(cal, textvariable=sc, font=('Fixedsys', 22), bg="royal blue")
sc1 = StringVar()
scr1 = Label(cal, textvariable=sc1, font=('Fixedsys', 22), bg="royal blue")
sc2 = StringVar()
scr2 = Label(cal, textvariable=sc2, font=('Fixedsys', 22), bg="royal blue")
sc3 = StringVar()
scr3 = Label(cal, textvariable=sc3, font=('Fixedsys', 22), bg="royal blue")
sc4 = StringVar()
scr4 = Label(cal, textvariable=sc4, font=('Fixedsys', 22), bg="royal blue")
sc5 = StringVar()
scr5 = Label(cal, textvariable=sc5, font=('Fixedsys', 22), bg="royal blue")
sc6 = StringVar()
scr6 = Label(cal, textvariable=sc6, font=('Fixedsys', 22), bg="royal blue")
sc7 = StringVar()
scr7 = Label(cal, textvariable=sc7, font=('Fixedsys', 22), bg="royal blue")
sc8 = StringVar()
scr8 = Label(cal, textvariable=sc8, font=('Fixedsys', 22), bg="royal blue")
# GPA
gp1 = StringVar()
gpa = Label(cal, textvariable=gp1, font=('Fixedsys', 22), bg="royal blue")
# Entries for scores
n1 = Entry(cal,bg='grey', font=('Lucida Console',14), textvariable=gr1)
r1 = Entry(cal,bg='grey', font=('Lucida Console',14), textvariable=gr2)
g1 = Entry(cal,bg='grey', font=('Lucida Console',14), textvariable=gr3)
g4 = Entry(cal,bg='grey', font=('Lucida Console',14), textvariable=gr4)
g5 = Entry(cal,bg='grey', font=('Lucida Console',14), textvariable=gr5)
g6 = Entry(cal,bg='grey', font=('Lucida Console',14), textvariable=gr6)
g7 = Entry(cal,bg='grey', font=('Lucida Console',14), textvariable=gr7)
g8 = Entry(cal,bg='grey', font=('Lucida Console',14), textvariable=gr8)
g9 = Entry(cal,bg='grey', font=('Lucida Console',14), textvariable=gr9)
# Buttons
but1 = Button(cal, text="Calculate", font=('Comic Sans MS',12), bg="teal", bd=10, fg='black', command=calc)
but2 = Button(cal, text="Reset", font=('Comic Sans MS',12), bg="teal", bd=10, fg='white', command=clear)
# placing the wigdets
h1.grid(column=1, row=0, columnspan=4)
css.grid(column=0, row=1)
txt.grid(column=0, row=1, columnspan=4, padx=50)
s.grid(column=3, row=1, padx=25)
pt.grid(column=6, row=1)
gc.grid(column=9, row=1, padx=10)
n.grid(column=0, row=2, pady=7)
r.grid(column=0, row=3, pady=7)
n1.grid(column=1, row=2, columnspan=1, pady=7, padx=10)
scr.grid(column=3, row=2)
r1.grid(column=1, row=3,columnspan=1, pady=7)
scr1.grid(column=3, row=3)
g.grid(column=0, row=4)
g1.grid(column=1, row=4, columnspan=1, pady=7)
scr2.grid(column=3, row=4)
b.grid(column=0, row=5)
g4.grid(column=1, row=5, columnspan=1, pady=7)
scr3.grid(column=3, row=5)
p.grid(column=0, row=6)
g5.grid(column=1, row=6, columnspan=1, pady=7)
scr4.grid(column=3, row=6)
cv.grid(column=0, row=7)
g6.grid(column=1, row=7,columnspan=1,pady=7)
scr5.grid(column=3, row=7)
gpy.grid(column=0, row=8)
g7.grid(column=1, row=8, columnspan=1, pady=7)
scr6.grid(column=3, row=8)
ts.grid(column=0, row=9)
g8.grid(column=1, row=9, columnspan=1, pady=7)
scr7.grid(column=3, row=9)
fm.grid(column=0, row=10)
g9.grid(column=1, row=10, columnspan=1, pady=7)
scr8.grid(column=3, row=10)
gp.grid(column=0,row=11, pady=20)
gpa.grid(column=1, row=11)
but1.grid(column=0, row=12, pady=15)
but2.grid(column=1, row=12, pady=15)

cal.mainloop()