# Create a Tkinter  program to send student's ID, Name, Course and Age into a database.
from tkinter import *
from tkinter import messagebox as mb
import sqlite3
# ========== functions =====
con = sqlite3.connect("studentDatabase.db")
cur = con.cursor()
def createTable():
    cur.execute("CREATE TABLE IF NOT EXISTS students(sName TEXT, sCourse TEXT, sAge INTEGER)")

def insertStudent():
    createTable()
    sid = e1.get()
    sname = e2.get()
    scourse = e3.get()
    sage = e4.get()
    cur.execute(f"INSERT INTO students VALUES({sid}, '{sname}', '{scourse}', {sage})")
    con.commit()

    view()
sid =[]
def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
def clearId():
    idE.delete(0, END)

def viewStudents():
    cur.execute("SELECT * FROM students")
    result = cur.fetchall()
    return result
def view():
    sid.clear()
    result = viewStudents()
    data = "ID     |  STUDENT NAME     |  COURSE     |  STUDENT AGE\n"
    Id =1
    for i in result:
        data = f"{data} {str(Id)}     |{i[1]}     |{i[2]}    |{i[3]} \n"
        Id += 1
        sid.append(i[0])
    clear()
    txt.delete(1.0, END)
    txt.insert(INSERT, data)

def viewOne():
    print(sid)
    x = idE.get()
    test = int(x) in sid
    if x =="":
        mb.showerror("ERROR","ID must not be empty, fill and try again.")
    elif not test:
        mb.showerror("ERROR","Error: ID not found in Database.")
    else:
        cur.execute(f"SELECT * FROM students WHERE sid= {x}")
        result = cur.fetchone()
        clear()
        e1.insert(0, result[0])
        e2.insert(0, result[1])
        e3.insert(0, result[2])
        e4.insert(0, result[3])
        data = "ID     |  STUDENT NAME     |  COURSE     |  STUDENT AGE\n"
        data = f"{data} {result}"
        txt.delete(1.0, END)
        txt.insert(INSERT, data)

def updateStudent():
    x = idE.get()
    test = int(x) in sid
    if x == "":
        mb.showerror("ERROR", "ID must not be empty, fill and try again.")
    elif not test:
        mb.showerror("ERROR", "Error: ID not found in Database.")
    else:
        cur.execute(f"UPDATE students SET sName='{e2.get()}', sCourse='{e3.get()}', sAge={e4.get()} "
                    f"WHERE sid={x}")
        con.commit()
        mb.showinfo("Message", "UPDATED SUCESSFULLY")
        view()

def viewOldest():
    cur.execute(f"SELECT * FROM students ORDER BY sAge DESC")
    result = cur.fetchmany(2)
    data = "ID     |  STUDENT NAME     |  COURSE     |  STUDENT AGE\n"
    for i in result:
        data = f"{data} |{str(i[0])}     |{i[1]}     |{i[2]}    |{i[3]} \n"
    txt.delete(1.0, END)
    txt.insert(INSERT, data)
def deleteStudent():
    x = idE.get()
    if x == "":
        x=0
    test = int(x) in sid
    if not test:
        mb.showerror("ERROR", "Error: ID not found in Database.")
    else:
        option = mb.askyesno("Confirm", f"Are you sure you want delete student with Id {x}?")
        if option == 1:
            chk =cur.execute(f"DELETE FROM students WHERE sid={x}")
            if chk:
                mb.showinfo("Message", "Data deleted sucessfully!")
                view()
            else:
                mb.showerror("ERROR","Error deleting, try again")
        else:
            mb.showwarning("Message", "No changes made to your database")

# ======= creating window =====
sDb = Tk()
sDb.title("Students Records")
sDb.geometry("820x650")
# WIDGETS
#++++++++++ Frames +++++++++
f1 = Frame(sDb, width=800, height=60, bg="grey")
f2 = Frame(sDb, width=670, height=290, bg="dark gray")
f3 = Frame(sDb, width=670, height=300, bg="white")
f4 = Frame(sDb, width=200, height=600, bg="#c8bfe7")
# +++++ Label ++++++
h = Label(f1, text="STUDENTS RECORD APP", bg="grey", fg="black", font=('cursive',28))
idL = Label(f2, text="Enter Student's ID:", bg="dark gray", fg="black", font=('cursive',14))
nameL = Label(f2, text="Student Name:", bg="dark gray", fg="black", font=('cursive',14))
courseL = Label(f2, text="Course:", bg="dark gray", fg="black", font=('cursive',14))
ageL = Label(f2, text="Age:", bg="dark gray", fg="black", font=('cursive',14))
output = Label(f3, text="OUTPUT:", bg="white", fg="indigo", font=('cursive',18))
idL2 = Label(f4, text="ID:", bg="#c8bfe7", fg="black", font=('cursive',16))
#+++++++++ Entries ++++++
e1 = Entry(f2, font=('verdana', 14), bd=5)
e2 = Entry(f2, font=('verdana', 14), bd=5)
e3 = Entry(f2, font=('verdana', 14), bd=5)
e4 = Entry(f2, font=('verdana', 14), bd=5)
idE = Entry(f4, font=('verdana', 14), bd=5)
#++++++ Buttons ++++++
b1 = Button(f4, text="View All Students",bg="teal", fg="white", font=('verdana', 12), bd=3, command=view)
b2 = Button(f2, text="Submit",bg="teal", fg="white", font=('verdana', 14), bd=3, command=insertStudent)
b3 = Button(f4, text="View One",bg="teal", fg="white", font=('verdana', 12), bd=3, command=viewOne)
b4 = Button(f4, text="2 Oldest",bg="teal", fg="white", font=('verdana', 12), bd=3, command=viewOldest)
b5 = Button(f4, text="Update",bg="teal", fg="white", font=('verdana', 12), bd=3, command=updateStudent)
b6 = Button(f4, text="Delete",bg="teal", fg="white", font=('verdana', 12), bd=3, command=deleteStudent)
b7 = Button(f4, text="Clear ID",bg="teal", fg="white", font=('verdana', 12), bd=3, command=clearId)
#+++++++ Textbox ++++++
txt = Text(f3, width=450, height=250, font=('Verdana', 16), fg="black", bd=4)
#====== Placing widgets=====
f1.pack()
f4.pack(side="left")
f2.pack()
f3.pack()
f1.pack_propagate(0)
f2.pack_propagate(0)
f3.pack_propagate(0)
f4.pack_propagate(0)
h.pack()
output.pack()
txt.pack()
idL.pack()
e1.pack()
nameL.pack()
e2.pack()
courseL.pack()
e3.pack()
ageL.pack()
e4.pack()
b2.pack(side="left", pady=5, padx=55, anchor="w")
idL2.pack(padx=2, pady=7)
idE.pack(padx=2, pady=7)
b3.pack(pady=10)
b4.pack(pady=10)
b5.pack(pady=10)
b6.pack(pady=10)
b7.pack(pady=10)
b1.pack(pady=20)
view()
#==== run app =====
sDb.mainloop()