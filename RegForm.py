# Create a registration form for students using checkbuttons to select courses.
# For a student to be registered he/she must select one or more course(s).
from tkinter import *
from tkinter import messagebox as mb

def clear():
    n.set("")
    rn.set("")
    c.set(0)
    c1.set(0)
    c2.set(0)
    c3.set(0)
    outfield.delete(1.0, END)

# def chk():
#     if c.get() == 1:
#         return "Java"
# def chk1():
#     if c1.get() == 1:
#         return "C++"
#
# def chk2():
#     if c2.get() == 1:
#         return "SQL"
#
#
# def chk3():
#     if c3.get() == 1:
#         return "Python"

def submit():
    x = n.get()
    y = rn.get()
    a = c.get()
    b = c1.get()
    cy = c2.get()
    d = c3.get()
    if a == "" and b == "" and cy == "" and d == "":
        mb.showerror('Error Message', 'You must choose at least one course \n to be registered.')
    elif x == "" and y =="":
        mb.showwarning('Warning', 'Name and Reg Number cannot be empty')
    elif x =="":
        mb.showwarning('Warning', 'Fullname  cannot be empty, \n fill and try again')
    elif y =="":
        mb.showwarning('Warning', 'Reg Number cannot be empty, \n fill and try again')
    else:
        mb.showinfo('Success', "Registration successful")
        xx = (a, b, cy, d)
        data = f'Student details \n\nName: {x}\nReg No: {y}\nGender: {gend.get()}\nYour course(s): {xx}'
        outfield.delete(1.0, END)
        outfield.insert('1.0', data)


reg = Tk()
reg.title("Registration Form")
reg.geometry("700x500")
reg.config(bg="#abeebd")
# Labels and Text
r = Label(reg, text="Registration Form", bg="#abeebd", fg="#ed1c24", font=('Verdana', 20))
name = Label(reg, text="Fullname:", bg="#abeebd", fg="#000000", font=('Consolas', 14))
regNo = Label(reg, text="Reg Number:", bg="#abeebd", fg="#000000", font=('Consolas', 14))
courses = Label(reg, text="Courses:", bg="#abeebd", fg="#000000", font=('Consolas', 14))
gender = Label(reg, text="Gender:", bg="#abeebd", fg="#000000", font=('Consolas', 14))
output = Label(reg, text="OUTPUT", bg="#abeebd", fg="#000000", font=('Consolas', 14))
outfield = Text(reg, font=('Consolas', 14), bd=5, fg='blue', width=45, height=8)
# All the "Vars"
n = StringVar()
rn = StringVar()
c = StringVar()
c1 = StringVar()
c2 = StringVar()
c3 = StringVar()
gend = StringVar()
# Entries
eName = Entry(reg, textvariable=n, fg="#7f7f7f", font=('Consolas', 14))
eReg = Entry(reg, textvariable=rn, fg="#7f7f7f", font=('Consolas', 14))
# Checkboxes
chkbx = Checkbutton(reg, text="Java",variable=c, bg="#abeebd", font=('Consolas', 12), onvalue='Java', offvalue='')
chkbx1 = Checkbutton(reg, text="C++", variable=c1, bg="#abeebd", font=('Consolas', 12), onvalue='C++', offvalue='')
chkbx2 = Checkbutton(reg, text="SQL", variable=c2, bg="#abeebd", font=('Consolas', 12), onvalue='SQL', offvalue='')
chkbx3 = Checkbutton(reg, text="Python", variable=c3, bg="#abeebd", font=('Consolas', 12), onvalue='Python', offvalue='')
# Radio buttons
radbut = Radiobutton(reg, text="Male", value='male',variable=gend, bg="#abeebd", font=('Consolas', 12))
radbut1 = Radiobutton(reg, text="Female", value='female', variable=gend, bg="#abeebd", font=('Consolas', 12))
# Buttons
but1= Button(reg, text="SUBMIT", bg="navy blue", font=('Arial',12),fg="cyan", command=submit)
but2= Button(reg, text="CLEAR", bg="navy blue", font=('Arial',12),fg="#7f7f7f", command=clear)
# Place widgets
r.grid(column=1, row=0, columnspan=4)
name.grid(column=0, row=2, pady=5)
eName.grid(column=1, row=2, columnspan=1,pady=5)
regNo.grid(column=0, row=3,pady=5)
eReg.grid(column=1, row=3, columnspan=1,pady=5)
courses.grid(column=0, row=4, pady=5)
chkbx.grid(column=1, row=4)
chkbx1.grid(column=2, row=4)
chkbx2.grid(column=1,row=5)
chkbx3.grid(column=2, row=5)
gender.grid(column=0, row=6)
radbut.grid(column=1,row=6)
radbut1.grid(column=2, row=6)
but1.grid(column=0, row=7)
but2.grid(column=1,row=7)
output.grid(column=1, row=8, pady=7)
outfield.grid(column=1, row=9)

reg.mainloop()