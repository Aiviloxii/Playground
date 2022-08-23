# A GUI that accepts age and print if the user is an adult or a kid.
from tkinter import *
def tell():
    age = fdvar.get()
    if int(age) >= 18:
        pri.set(f"You are {int(age)} years old and  an adult.\nWelcome to Greg & CO Hub.")
    else:
        pri.set(f"You are {int(age)} years old and a kid")


ager = Tk()
ager.title("Age Checker")
ager.geometry("600x400")
ager.config(bg="black")
text = Label(ager, text="Welcome to GUI Programming",bg="black",font=('Trebuchet MS',22), fg="white")
text2 = Label(ager,text="Enter your age:",bg="black",font=('Verdana',22),fg="#7092be")
fdvar = StringVar()
field1=Entry(ager, font=('Verdana',14),textvariable=fdvar)
but1 = Button(ager,text="Submit",font=('cursive',15), bg="#7f7f7f", fg="#0a2e84", command=tell)
pri = StringVar()
prin = Label(ager, font=('Verdana',14),textvariable=pri,bg="black",fg="purple")
text.pack()
text2.pack(pady=10)
field1.pack()
but1.pack(pady=15)
prin.pack(pady=20)

ager.mainloop()