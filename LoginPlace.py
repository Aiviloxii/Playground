#Create a login form using place method.
from tkinter import *

def submit():
    x = username.get()
    y = password.get()
    if len(x)==0 and len(y)==0:
        stat.set(f"You have not entered any details yet!")
    elif len(x)==0:
        stat.set(f"Please enter a valid username.")
    elif len(y)==0:
        stat.set(f"Please enter a valid password.")
    elif x==names[0] and y!=words[0]:
        stat.set(f"Incorrect password")
    elif x!=names[0] and y==words[0]:
        stat.set(f"Invalid username")
    elif x==names[1] and y!=words[1]:
        stat.set(f"Incorrect password")
    elif x!=names[1] and y==words[1]:
        stat.set(f"Invalid username")
    elif x==names[2] and y!=words[2]:
        stat.set(f"Incorrect password")
    elif x!=names[2] and y==words[2]:
        stat.set(f"Invalid username")
    elif x==names[3] and y!=words[3]:
        stat.set(f"Incorrect password")
    elif x!="xing" and y=="xing1":
        stat.set(f"Invalid username")
    elif x!=names[0] and x!=names[1] and x!=names[2] and x!=names[3]:
        stat.set("Invalid username")
    elif y!=words[0] and y!=words[1] and y!=words[2] and y!=words[3]:
        stat.set("Incorrect password")
    else:
        stat.set("Login Successful!!")
def clear():
    username.set("")
    password.set("")
    stat.set("")

log = Tk()
log.title("LOGIN")
log.geometry("600x400")
log.config(bg="black")
text = Label(log, text="LOGIN FORM",bg="black",font=('Trebuchet MS',22), fg="grey")
user = Label(log,text="Username:",bg="black",font=('Verdana',22),fg="#7092be")
pword = Label(log,text="Password:",bg="black",font=('Verdana',22),fg="#7092be")
username = StringVar()
password = StringVar()
field1=Entry(log, font=('Verdana',14),textvariable=username)
field2 = Entry(log,font=('Verdana',14),textvariable=password)
but1 = Button(log,text="Clear",font=('cursive',15), bg="#7f7f7f", fg="black", command=clear)
but2 = Button(log,text="Submit",font=('cursive',15), bg="#a84040", fg="black",activeforeground='yellow',activebackground='blue',bd=5, command=submit)
stat= StringVar()
status= Label(log, textvariable=stat, bg="black",font=('Verdana',16),fg="white")
text.place(x=200, y=0)
user.place(x=25,y=50)
field1.place(x=200, y=60)
pword.place(x=25, y=90)
field2.place(x=200, y=100)
but1.place(x=27, y=150)
but2.place(x=200, y=150)
status.place(x=0,y=200)
names=["mary", "gill","matt","xing"]
words=["mary1","gill1","matt1","xing1 "]

log.mainloop()
