#A GUI grade calculator for either WAEC, NECO or semester results.
from tkinter import *
# Function to clear the values.
def clear():
    gr1.set("")
    gr2.set("")
    gr3.set("")
    gr4.set("")
    gr5.set("")
    gr6.set("")
    gr7.set("")
    gr8.set("")
    gr9.set("")
    sc.set("")
    sc1.set('')
    sc2.set('')
    sc3.set('')
    sc4.set('')
    sc5.set('')
    sc6.set('')
    sc7.set('')
    sc8.set('')
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
    elif 56 <= x < 70:
        sc.set('B')
    elif 50 <= x < 56:
        sc.set('C')
    elif 40 <= x < 50:
        sc.set('D')
    elif 0 <= x < 40:
        sc.set('E')
    else:
        sc.set('Invalid score!')
    if 70 <= y < 101:
        sc1.set('A')
    elif 56 <= y < 70:
        sc1.set('B')
    elif 50 <= y < 56:
        sc1.set('C')
    elif 40 <= y < 50:
        sc1.set('D')
    elif 0 <= y < 40:
        sc1.set('E')
    else:
        sc1.set('Invalid score!')
    if 70 <= z < 101:
        sc2.set('A')
    elif 55 <= z < 70:
        sc2.set('B')
    elif 50 <= z < 55:
        sc2.set('C')
    elif 40 <= z < 50:
        sc2.set('D')
    elif 0 <= z < 40:
        sc2.set('E')
    else:
        sc2.set('Invalid score!')
    if 70 <= a < 101:
        sc3.set('A')
    elif 55 <= a < 70:
        sc3.set('B')
    elif 50 <= a < 55:
        sc3.set('C')
    elif 40 <= a < 50:
        sc3.set('D')
    elif 0 <= a < 40:
        sc3.set('E')
    else:
        sc3.set('Invalid score!')
    if 70 <= c < 101:
        sc4.set('A')
    elif 55 <= c < 70:
        sc4.set('B')
    elif 50 <= c < 55:
        sc4.set('C')
    elif 40 <= c < 50:
        sc4.set('D')
    elif 0 <= c < 40:
        sc4.set('E')
    else:
        sc4.set('Invalid score!')
    if 70 <= d < 101:
        sc5.set('A')
    elif 55 <= d < 70:
        sc5.set('B')
    elif 50 <= d < 55:
        sc5.set('C')
    elif 40 <= d < 50:
        sc5.set('D')
    elif 0 <= d < 40:
        sc5.set('E')
    else:
        sc5.set('Invalid score!')
    if 70 <= e < 101:
        sc6.set('A')
    elif 55 <= e < 70:
        sc6.set('B')
    elif 50 <= e < 55:
        sc6.set('C')
    elif 40 <= e < 50:
        sc6.set('D')
    elif 0 <= e < 40:
        sc6.set('E')
    else:
        sc6.set('Invalid score!')
    if 70 <= f < 101:
        sc7.set('A')
    elif 55 <= f < 70:
        sc7.set('B')
    elif 50 <= f < 55:
        sc7.set('C')
    elif 40 <= f < 50:
        sc7.set('D')
    elif 0 <= f < 40:
        sc7.set('E')
    else:
        sc7.set('Invalid score!')
    if 70 <= h < 101:
        sc8.set('A')
    elif 55 <= h < 70:
        sc8.set('B')
    elif 50 <= h < 55:
        sc8.set('C')
    elif 40 <= h < 50:
        sc8.set('D')
    elif 0 <= h < 40:
        sc8.set('E')
    else:
        sc8.set('Invalid score!')

cal = Tk()
cal.title("CALCULATOR")
cal.geometry("900x500")
cal.config(bg="white")

# Labels for subjects offerred.
h1 = Label(cal, text="Welcome to Lio's Grader for SSCE and NECO", bg="white", fg="black", font=('cooper black',22))
sub = Label(cal, text="Enter your Subjects", bg="white", fg="teal", font=('cursive',14))
txt = Label(cal, text="Fill in your scores", bg="white", fg="teal", font=('cursive',14))
n = Label(cal, text="English Lang:", bg="white", fg="black", font=('Segoe UI Semibold',14))
r = Label(cal, text="Mathematics:", bg="white", fg="black", font=('Segoe UI Semibold',14))
cv = Label(cal, text="Civic Edu:", bg="white", fg="black", font=('Segoe UI Semibold',14))
g_ = StringVar()
g = Entry(cal, textvariable=g_, bg="white", fg="black", font=('Segoe UI Semibold',14))
b_ = StringVar()
b = Entry(cal, textvariable=b_, bg="white", fg="black", font=('Segoe UI Semibold',14))
p_ = StringVar()
p = Entry(cal, textvariable=p_, bg="white", fg="black", font=('Segoe UI Semibold',14))
gp_ = StringVar()
gpy = Entry(cal, textvariable=gp_, bg="white", fg="black", font=('Segoe UI Semibold',14))
ts_ = StringVar()
ts = Entry(cal, textvariable=ts_, bg="white", fg="black", font=('Segoe UI Semibold',14))
fm_ = StringVar()
fm = Entry(cal, textvariable=fm_, bg="white", fg="black", font=('Segoe UI Semibold',14))
s = Label(cal, text="GRADES", bg="white", fg="teal", font=('Verdana',17))
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
scr = Label(cal, textvariable=sc, font=('Fixedsys', 22), bg="white")
sc1 = StringVar()
scr1 = Label(cal, textvariable=sc1, font=('Fixedsys', 22), bg="white")
sc2 = StringVar()
scr2 = Label(cal, textvariable=sc2, font=('Fixedsys', 22), bg="white")
sc3 = StringVar()
scr3 = Label(cal, textvariable=sc3, font=('Fixedsys', 22), bg="white")
sc4 = StringVar()
scr4 = Label(cal, textvariable=sc4, font=('Fixedsys', 22), bg="white")
sc5 = StringVar()
scr5 = Label(cal, textvariable=sc5, font=('Fixedsys', 22), bg="white")
sc6 = StringVar()
scr6 = Label(cal, textvariable=sc6, font=('Fixedsys', 22), bg="white")
sc7 = StringVar()
scr7 = Label(cal, textvariable=sc7, font=('Fixedsys', 22), bg="white")
sc8 = StringVar()
scr8 = Label(cal, textvariable=sc8, font=('Fixedsys', 22), bg="white")
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
but1 = Button(cal, text="Calculate", font=('Comic Sans MS',12), bg="navy blue", bd=10, fg='lime', command=calc)
but2 = Button(cal, text="Reset", font=('Comic Sans MS',12), bg="navy blue", bd=10, fg='white', command=clear)
# placing the wigdets
h1.grid(column=1, row=0, columnspan=4)
sub.grid(column=0,row=1)
txt.grid(column=1, row=1)
s.grid(column=4, row=1)
n.grid(column=0, row=2, pady=7)
r.grid(column=0, row=3, pady=7)
n1.grid(column=1, row=2, columnspan=1, pady=7)
scr.grid(column=4, row=2)
r1.grid(column=1, row=3,columnspan=1, pady=7)
scr1.grid(column=4, row=3)
g.grid(column=0, row=4)
g1.grid(column=1, row=4, columnspan=1, pady=7)
scr2.grid(column=4, row=4)
b.grid(column=0, row=5)
g4.grid(column=1, row=5, columnspan=1, pady=7)
scr3.grid(column=4, row=5)
p.grid(column=0, row=6)
g5.grid(column=1, row=6, columnspan=1, pady=7)
scr4.grid(column=4, row=6)
cv.grid(column=0, row=7)
g6.grid(column=1, row=7,columnspan=1,pady=7)
scr5.grid(column=4, row=7)
gpy.grid(column=0, row=8)
g7.grid(column=1, row=8, columnspan=1, pady=7)
scr6.grid(column=4, row=8)
ts.grid(column=0, row=9)
g8.grid(column=1, row=9, columnspan=1, pady=7)
scr7.grid(column=4, row=9)
fm.grid(column=0, row=10)
g9.grid(column=1, row=10, columnspan=1, pady=7)
scr8.grid(column=4, row=10)
but1.grid(column=0, row=11, pady=8)
but2.grid(column=1, row=11, pady=8)

cal.mainloop()