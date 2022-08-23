# Create a login form for at least 5 registered users.
from tkinter import *
from tkinter import messagebox as mb
validUser = ['Phillip', 'Terdoo', 'Bakwo', 'Olivia', 'Uba', 'Aivilo']
validPassword = ['$1234', '$5678', '$91011', '$1213', '$1415', '$1617']
def clear():
    username.set("")
    password.set("")

def submit():
    x = username.get()
    y = password.get()
    if x == "":
        mb.showerror('Error Message', 'Username cannot be empty, \n fill and try again')
    elif y =="":
        mb.showwarning('Warning', 'Password cannot be empty, \n fill and try again')
    elif x == validUser[0] and y == validPassword[0]:
        b = mb.askyesno('Confirm Message', 'Do you want to be logged in')
        if b == 1:
            mb.showinfo('Success Message', 'You are logged in successfully')
        else:
            mb.showwarning('Warning', "You won't be logged in")
    elif x == validUser[1] and y == validPassword[1]:
        b = mb.askyesno('Confirm Message', 'Do you want to be logged in')
        if b == 1:
            mb.showinfo('Success Message', 'You are logged in successfully')
        else:
            mb.showwarning('Warning', "You won't be logged in")
    elif x == validUser[2] and y == validPassword[2]:
        b = mb.askyesno('Confirm Message', 'Do you want to be logged in')
        if b == 1:
            mb.showinfo('Success Message', 'You are logged in successfully')
        else:
            mb.showwarning('Warning', "You won't be logged in")
    elif x == validUser[3] and y == validPassword[3]:
        b = mb.askyesno('Confirm Message', 'Do you want to be logged in')
        if b == 1:
            mb.showinfo('Success Message', 'You are logged in successfully')
        else:
            mb.showwarning('Warning', "You won't be logged in")
    elif x == validUser[4] and y == validPassword[4]:
        b = mb.askyesno('Confirm Message', 'Do you want to be logged in')
        if b == 1:
            mb.showinfo('Success Message', 'You are logged in successfully')
        else:
            mb.showwarning('Warning', "You won't be logged in")
    elif x == validUser[5] and y == validPassword[5]:
        b = mb.askyesno('Confirm Message', 'Do you want to be logged in')
        if b == 1:
            mb.showinfo('Success Message', 'You are logged in successfully')
        else:
            mb.showwarning('Warning', "You won't be logged in")
    else:
        mb.showerror('Error', 'Invalid username or password! \n Check your details and try again')

log = Tk()
log.title("LOGIN")
log.geometry("600x400")
log.config(bg="#f9dff8")
text = Label(log, text="LOGIN FORM",bg="#f9dff8",font=('Trebuchet MS',22), fg="#000000")
user = Label(log,text="Username:",bg="#f9dff8",font=('Verdana',22),fg="#000000")
pword = Label(log,text="Password:",bg="#f9dff8",font=('Verdana',22),fg="#000000")
username = StringVar()
password = StringVar()
field1=Entry(log, font=('Verdana',14),textvariable=username)
field2 = Entry(log,font=('Verdana',14),textvariable=password)
but1 = Button(log,text="Clear",font=('cursive',15), bg="#084040", fg="lime", bd=5, command=clear)
but2 = Button(log,text="Log In",font=('cursive',15), bg="#084040", fg="cyan",activeforeground='yellow',activebackground='blue',bd=5, command=submit)
text.place(x=200, y=0)
user.place(x=25,y=50)
field1.place(x=200, y=60)
pword.place(x=25, y=90)
field2.place(x=200, y=100)
but1.place(x=27, y=150)
but2.place(x=200, y=150)

log.mainloop()
