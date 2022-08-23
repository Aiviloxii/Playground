# A Student record keeping app.
from tkinter import *
import json
from tkinter import messagebox as mb

stapp = Tk()
stapp.title("Student Record App")
stapp.geometry("900x600")
stapp.config(bg="#cbe6cc")
#frames
f0 = Frame(stapp, width=700, height=50, bg="#cbe6cc")
f1 = Frame(stapp, width=200, height=400, bg="#cbe6cc")
f2 = Frame(stapp, width=600, height=400, bg="#cbe6cc")
#labels
h0 = Label(f0, text="STUDENT RECORD KEEPING APP", bg="#cbe6cc", font=('verdana', 20))
h1 = Label(f1, text="STUDENT REGISTRATION", bg="#cbe6cc", font=('verdana', 18), fg="#000000")
h2 = Label(f2, text="View Registered Students", bg="#cbe6cc", font=('verdana', 18), fg="#000000")
h3 = Label(f1, text="DELETE REGISTERED STUDENT", bg="#cbe6cc", font=('verdana', 18), fg="#000000")
name = Label(f1, text="Name:", bg="#cbe6cc", font=('verdana', 14), fg="#000000")
course = Label(f1, text="Course:", bg="#cbe6cc", font=('verdana', 14), fg="#000000")
idL = Label(f1, text="Student ID:", bg="#cbe6cc", font=('verdana', 14), fg="#000000")
#entries
e1 = Entry(f1,font=('verdana', 14))
e2 = Entry(f1,font=('verdana', 14))
e3 = Entry(f1,font=('verdana', 14))
txt = Text(f2, width=500, height=300, font=('verdana', 14))
#functions
def view():
    with open("info.json", "r") as rf:
        data = json.load(rf)
    tableData = "ID| STUDENT NAME | COURSE | \n"
    id =1
    for i in data:
        tableData = tableData+str(id)+"|"+str(i["name"])+"|"+str(i["course"])+"|\n"
        id +=1
    txt.delete(1.0, END)
    txt.insert(INSERT, tableData)
def addStudent():
    student = e1.get()
    courses = e2.get()
    if student != "" and courses != "":
        newStudent = {"name": student, "course": courses}
        with open("info.json", "r") as f:
            oldData = json.load(f)
            oldData.append(newStudent)
            with open("info.json", "w") as w:
                json.dump(oldData, w)
                w.close()
                mb.showinfo('SUCCESS', 'Data successfully added.')
                view()
    else:
        mb.showerror('ERROR MESSAGE', 'Error: All fields must not be empty')
def delStudent():
    x = e3.get()
    with open("info.json", "r") as d:
        b = json.load(d)
    if x != "":
        z = int(x) - 1
        b.pop(z)
        mb.showinfo('MESSAGE', "Student's data has been removed!")
        tableData = "ID| STUDENT NAME | COURSE | \n"
        id = 1
        for i in b:
            tableData = tableData + str(id) + "|" + str(i["name"]) + "|" + str(i["course"]) + "|\n"
            id += 1
        txt.delete(1.0, END)
        txt.insert(INSERT, tableData)
    else:
        mb.showerror('ERROR', 'Error: Fill in a valid ID!')

#buttons
b1 = Button(f1, text="Add Student", activeforeground="red", activebackground="pink", bg="brown", fg="white", font=('verdana', 14), command=addStudent)
b2 = Button(f1, text="Delete Student", activeforeground="red", activebackground="pink", bg="brown", fg="white", font=('verdana', 14), command=delStudent)

#add widgets
f0.pack()
f1.pack(side="left", anchor="ne", pady=10)
f2.pack(side="right", anchor="nw", padx=20)
f0.pack_propagate(0)
f1.pack_propagate(0)
f2.pack_propagate(0)
h0.pack()
h1.grid(row=0, column=0, columnspan=3)
name.grid(column=0, row=1)
e1.grid(column=1, row=1, padx=4,pady=4)
course.grid(column=0, row=2)
e2.grid(column=1, row=2, padx=4,pady=4)
b1.grid(column=1, row=3, pady=4, sticky="E")
h3.grid(column=0, row=4, columnspan=3)
idL.grid(column=0, row=5)
e3.grid(column=1, row=5, padx=4, pady=4)
b2.grid(column=1, row=6, padx=4, pady=4, sticky="E")
h2.pack()
txt.pack()
view()

#runapp
stapp.mainloop()
