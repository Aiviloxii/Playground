from tkinter import *
bio = Tk()
bio.title("My Biography")


bio.geometry("550x550")
bio.config(bg="grey")
t = Label(bio, text="Welcome to my biography!",font=('Cursive',30),fg="navy", bg="grey")
name=Label(bio,text="I am Olivia Godwin aka Aivilo,",font=('Arial',16),bg="teal")
age=Label(bio,text="I am 21 years old, quite old.",font=('Arial',16),fg="black", bg="grey")
country=Label(bio,text="I am from a state called Benue in Nigeria.",font=('Arial',16),bg="teal")
fd=Label(bio,text="My favorite food is Rice & Beans, any milk drink goes.",font=('Arial',16),bg="grey")
me=Label(bio,text="A big fan of funny,jovial people and an eager learner.",font=('Arial',16),bg="teal")
t.pack()
name.pack()
age.pack()
country.pack()
fd.pack()
me.pack()
bio.mainloop()