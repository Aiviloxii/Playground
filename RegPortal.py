# Create a registration portal with login,register and view tabs.
from tkinter import *
from tkinter import messagebox as mb
def clear():
    n.set("")
    rn.set("")
    c.set(0)
    c1.set(0)
    c2.set(0)
    c3.set(0)

def clearframe():
    outfield.delete("1.0", "end")

def submit():
    x = n.get()
    y = rn.get()
    if c.get() == 0 and c1.get() == 0 and c2.get() == 0 and c3.get() == 0:
        mb.showerror('Error Message', 'You must choose at least one course \n to be registered.')
    elif x == "" and y =="":
        mb.showwarning('Warning', 'Name and Reg Number cannot be empty')
    elif x =="":
        mb.showwarning('Warning', 'Fullname  cannot be empty, \n fill and try again')
    elif y =="":
        mb.showwarning('Warning', 'Reg Number cannot be empty, \n fill and try again')
    else:
        mb.showinfo('Success', "Registration successful!")

def chk():
    if c.get() == 1:
        return "Java"
def chk1():
    if c1.get() == 1:
        return "C++"
def chk2():
    if c2.get() == 1:
        return "SQL"
def chk3():
    if c3.get() == 1:
        return "Python"

def view():
    data = f"Student details\n\nName:{n.get()} \nReg No:{rn.get()} \nGender:{gend.get()} \nYour courses:{chk(), chk1(), chk2(), chk3()}"
    outfield.delete(1.0, END)
    outfield.insert('1.0', data)

reg = Tk()
reg.geometry("850x700")
reg.title("Registration Portal")
# Frames
f1 = Frame(reg, width=850, height=80, bd=5, bg="#117fbe")
f2 = Frame(reg, width=150, height=700, bd=5, bg="#32da6a")
f3= Frame(reg, width=850, height=400, bd=5, bg="#abeebd")
f4 = Frame(reg, width=850, height=300, bd=5, bg="#ffffff")
t = Label(f1, text="Welcome to LIO Registration Portal", bg="#117fbe", font=('Palatino Linotype',29), fg="#000000")
login = Button(f2, text="LOGIN", bg="navy blue", fg="cyan", font=('Corbel', 16), bd=8, command=submit)
profile = Button(f2, text="VIEW", bg="grey", fg="cyan", font=('Corbel', 16), bd=8, command=view)
clear = Button(f2, text="RESET", bg="navy blue", fg="cyan", font=('Corbel', 16), bd=8, command=clear)
reset = Button(f2, text="CLEAR", bg="black", fg="cyan", font=('Corbel', 16), bd=8, command=clearframe)
# Labels and Text
r = Label(f3, text="Registration Form", bg="#abeebd", fg="#ed1c24", font=('Verdana', 22))
name = Label(f3, text="Fullname:", bg="#abeebd", fg="#000000", font=('Consolas', 17))
regNo = Label(f3, text="Reg Number:", bg="#abeebd", fg="#000000", font=('Consolas', 17))
courses = Label(f3, text="Courses:", bg="#abeebd", fg="#000000", font=('Consolas', 17))
gender = Label(f3, text="Gender:", bg="#abeebd", fg="#000000", font=('Consolas', 17))
outfield = Text(f4, font=('Consolas', 14), bd=5, fg='blue')
# All the "Vars"
n = StringVar()
rn = StringVar()
c = IntVar()
c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
gend = StringVar()
# Entries
eName = Entry(f3, textvariable=n, fg="#7f7f7f", font=('Consolas', 14))
eReg = Entry(f3, textvariable=rn, fg="#7f7f7f", font=('Consolas', 14))
# Checkboxes
chkbx = Checkbutton(f3, text="Java",variable=c, bg="#abeebd", font=('Consolas', 12), onvalue=1, offvalue=0)
chkbx1 = Checkbutton(f3, text="C++", variable=c1, bg="#abeebd", font=('Consolas', 12), onvalue=1, offvalue=0)
chkbx2 = Checkbutton(f3, text="SQL", variable=c2, bg="#abeebd", font=('Consolas', 12), onvalue=1, offvalue=0)
chkbx3 = Checkbutton(f3, text="Python", variable=c3, bg="#abeebd", font=('Consolas', 12), onvalue=1, offvalue=0)
# Radio buttons
radbut = Radiobutton(f3, text="Male", value='male',variable=gend, bg="#abeebd", font=('Consolas', 12))
radbut1 = Radiobutton(f3, text="Female", value='female', variable=gend, bg="#abeebd", font=('Consolas', 12))

f1.pack()
f2.pack(side="left")
f3.pack()
f4.pack()
f1.pack_propagate(0)
f2.pack_propagate(0)
f3.pack_propagate(0)
f4.pack_propagate(0)
t.pack()
login.pack(pady=9)
clear.pack(pady=4)
reset.pack(side="bottom")
profile.pack(side="bottom", pady=5)
r.pack(side="top")
name.pack()
eName.pack()
regNo.pack()
eReg.pack()
gender.pack()
radbut.pack()
radbut1.pack()
courses.pack()
chkbx.pack()
chkbx2.pack()
chkbx1.pack()
chkbx3.pack()
outfield.pack()

reg.mainloop()