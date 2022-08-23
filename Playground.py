import sys
from tkinter import *
from tkinter import messagebox as mb
import random as r
import sqlite3
import qrcode as qr

def srp():
    # Function to view available courses with their period
    sn = []

    # ======List of available courses in program

    def viewCourses():
        def close():
            cor.destroy()

        cor = Tk()
        cor.title("Course Page")
        cor.geometry("600x350")
        cor.config()
        cF = Frame(cor, width=600, height=50, bd=5, bg="#abeebd")
        cF.pack()
        cF.pack_propagate(0)
        cF2 = Frame(cor, width=600, height=300, bd=5, bg="#abeebd")
        cF2.pack()
        cF2.grid_propagate(0)
        cH = Label(cF, bg="#abeebd", text="View all the courses with their days of lecture.",
                   font=("impact", 14, "bold"), fg="indigo")
        cH.pack()
        course = Label(cF2, text="COURSES", bg="#abeebd", font=("Verdana", 12, "bold"), fg="black")
        course.grid(row=0, column=1)
        timer = Label(cF2, text="DAYS of the Week", bg="#abeebd", font=("Verdana", 12, "bold"), fg="black")
        timer.grid(row=0, column=4, padx=80)
        # course names
        pyt = Label(cF2, text="Python Programming", bg="#abeebd", fg="indigo", font=("verdana", 10, 'bold'))
        pyt.grid(row=1, column=1, pady=5)
        jav = Label(cF2, text="Java Programming", bg="#abeebd", fg="indigo", font=("verdana", 10, 'bold'))
        jav.grid(row=2, column=1, pady=5)
        dbms = Label(cF2, text="Database Management System", bg="#abeebd", fg="indigo", font=("verdana", 10, 'bold'))
        dbms.grid(row=3, column=1, pady=5)
        wbd = Label(cF2, text="Web Development", bg="#abeebd", fg="indigo", font=("verdana", 10, 'bold'))
        wbd.grid(row=4, column=1, pady=5)
        cme = Label(cF2, text="Computer Engineering", bg="#abeebd", fg="indigo", font=("verdana", 10, 'bold'))
        cme.grid(row=5, column=1, pady=5)
        mpd = Label(cF2, text="Mobile App Devp", bg="#abeebd", fg="indigo", font=("verdana", 10, 'bold'))
        mpd.grid(row=6, column=1, pady=5)
        # days of the week
        pytd = Label(cF2, bg="#abeebd", fg="indigo", text="Monday,Tuesday,Wednesday.", font=('verdana', 10, 'bold'))
        pytd.grid(row=1, column=4, padx=8)
        javd = Label(cF2, bg="#abeebd", fg="indigo", text="Tuesday,Wednesday,Thursday", font=('verdana', 10, 'bold'))
        javd.grid(row=2, column=4, padx=8)
        wbdd = Label(cF2, bg="#abeebd", fg="indigo", text="Monday,Wednesday,Friday", font=('verdana', 10, 'bold'))
        wbdd.grid(row=4, column=4, padx=8)
        dbmsd = Label(cF2, bg="#abeebd", fg="indigo", text="Monday,Thursday,Friday", font=('verdana', 10, 'bold'))
        dbmsd.grid(row=3, column=4, padx=8)
        cmed = Label(cF2, bg="#abeebd", fg="indigo", text="Tuesday,Wednesday,Friday", font=('verdana', 10, 'bold'))
        cmed.grid(row=5, column=4, padx=8)
        mpdd = Label(cF2, bg="#abeebd", fg="indigo", text="Monday,Wednesday,Thursday", font=('verdana', 10, 'bold'))
        mpdd.grid(row=6, column=4, padx=8)
        but = Button(cF2, bg="indigo", fg="#abeebd", text="Exit Courses", font=("cursive", 14, 'bold'), bd=2,
                     command=close)
        but.grid(row=8, column=1, pady=10)

        cor.mainloop()

    con1 = sqlite3.connect("Playground.db")

    cur1 = con1.cursor()

    # =====Creating the table in database
    def createTable():
        cur1.execute(
            "CREATE TABLE IF NOT EXISTS students(sid INTEGER PRIMARY KEY, sName TEXT,sGender TEXT, sCourse TEXT, sAge INTEGER)")

    # ======To display  courses chosen

    def showCourses():
        m = c1.get()
        n = c2.get()
        o = c3.get()
        p = c4.get()
        q = c5.get()
        t = c6.get()
        if m:
            return "Java Programming"
        if n:
            return "Python Programming"
        if o:
            return "Database Mgt System"
        if p:
            return "Mobile App Dev"
        if q:
            return "Computer Engineering"
        if t:
            return "Web Development"
        if m and n:
            return "Java Programming,Python Programming"
        if m and n and o and p and q and t:
            return "Java Programming,Python Programming,Database Mgt System,Mobile App Dev,Computer Engineering,Web Development"
        if m and n and o and p and q:
            return "Java Programming,Python Programming,Database Mgt System,Mobile App Dev,Computer Engineering"
        if m and n and o and p:
            return "Java Programming,Python Programming,Database Mgt System,Mobile App Dev"
        if m and n and o:
            return "Java Programming,Python Programming,Database Mgt System"
        if n and o and p and q and t:
            return "Python Programming,Database Mgt System,Mobile App Dev,Computer Engineering,Web Development"
        if n and o and p and q:
            return "Python Programming,Database Mgt System,Mobile App Dev,Computer Engineering"
        if n and o and p:
            return "Python Programming,Database Mgt System,Mobile App Dev."
        if n and o:
            return "Python Programming,Database Mgt System"
        if m and o:
            return "Java Programming,Database Mgt System."
        if m and p:
            return "Java Programming,Mobile App Dev."
        if m and q:
            return "Java Programming,Computer Engineering."
        if m and t:
            return "Java Programming,Web Development."
        if n and p:
            return "Python Programming,Mobile App Dev."
        if n and q:
            return "Python Programming,Computer Engineering."
        if n and t:
            return "Python Programming,Web Development."
        if o and p and q and t:
            return "Database Mgt System,Mobile App Dev,Computer Engineering,Web Development"
        if o and p and q:
            return "Database Mgt System,Mobile App Dev,Computer Engineering."
        if o and p:
            return "Database Mgt System,Mobile App Dev."
        if o and q:
            return "Database Mgt System,Computer Engineering."
        if o and t:
            return "Database Mgt System,Web Development."
        if p and q and t:
            return "Mobile App Dev,Computer Engineering,Web Development"
        if p and q:
            return "Mobile App Dev,Computer Engineering."
        if p and t:
            return "Mobile App Dev,Web Development"
        if q and t:
            return "Computer Engineering,Web Development"

    # ======To insert details in database
    def regStudent():
        a = nameE.get()
        b = ageE.get()
        c = gend.get()
        d, e, f, g, i, j = c1.get(), c2.get(), c3.get(), c4.get(), c5.get(), c6.get()
        if a == "" and b == "":
            mb.showwarning("Warning", "Name and Age cannot be empty!")
        elif a == "":
            mb.showwarning("Warning", "Name field cannot be empty!")
        elif b == "":
            mb.showwarning("Warning", "Age field cannot be empty!")
        elif c == "":
            mb.showwarning("Warning", "Student's gender is unknown!")
        elif d == "" and e == "" and f == "" and g == "" and i == "" and j == "":
            mb.showerror("ERROR MESSAGE", "ERROR: at last one course should be selected!!")
        else:
            createTable()
            sname = nameE.get()
            gender = str(gend.get())
            course = showCourses()
            age = ageE.get()
            cur1.execute(f"INSERT INTO students VALUES({v}, '{sname}','{gender}', '{course}', {age})")
            con1.commit()
            mb.showinfo('MESSAGE', "New Student successfully registered!")
            view()

    # =====Database function to select values
    def viewStudents():
        cur1.execute("SELECT * FROM students")
        result = cur1.fetchall()
        return result

    # =====To clear entries
    def clear():
        nameE.delete(0, END)
        ageE.delete(0, END)
        gend.set("")
        c1.set("")
        c2.set("")
        c3.set("")
        c4.set("")
        c5.set("")
        c6.set("")

    def clrId():
        IDE.delete(0, END)

    # ==== Function to generate Qrcode
    def view():
        x = viewStudents()
        Id = 1
        for i in x:
            stats = f"S/N: {str(Id)}\nSTUDENT ID: {i[0]}\nSTUDENT NAME: {i[1]}\nGENDER: {i[2]}\nCOURSE: {i[3]}\nSTUDENT AGE: {i[4]}"
            Id += 1
            sn.append(i[0])
            q = qr.QRCode(
                version=1,
                box_size=5,
                border=5
            )
            q.add_data(stats)
            q.make(fit=True)
            img = q.make_image(fill_color="brown", back_color="white")
            img.save(f"{nameE.get()}.png")
            s = PhotoImage(file=f"{nameE.get()}.png")
            qrL.config(image=s)
            showL.config(text=f"QRCode for ID:{i[0]}")

    # ++++++ Function to view one student's detaiils.
    def viewOne():
        x = IDE.get()
        if x == "":
            mb.showerror("ERROR", "ID must not be empty, fill and try again.")
        elif int(x) not in sn:
            mb.showerror("ERROR", "Error: Not found in database.")
        else:
            cur1.execute(f"SELECT * FROM students WHERE sid= {x}")
            result = cur1.fetchone()
            clear()
            nameE.insert(0, result[1])
            ageE.insert(0, result[4])
            gend.set(result[2])
            c1.set(result[3])
            c2.set(result[3])
            c3.set(result[3])
            c4.set(result[3])
            c5.set(result[3])
            c6.set(result[3])

            def qrc():
                stats = f"STUDENT ID: {result[0]}\nSTUDENT NAME: {result[1]}\nGENDER: {result[2]}\nCOURSE: {result[3]}\nSTUDENT AGE: {result[4]}"
                q = qr.QRCode(
                    version=1,
                    box_size=5,
                    border=5
                )
                q.add_data(stats)
                q.make(fit=True)
                img = q.make_image(fill_color="brown", back_color="white")
                img.save(f"{nameE.get()}2.png")
                s = PhotoImage(file=f"{nameE.get()}2.png")
                qrL.config(image=s)
                showL.config(text=f"QRCode for ID:{result[0]}")
            qrc()

    # ===== To update student's information in database
    def updateStudent():
        x = IDE.get()
        if x == "":
            mb.showwarning("WARNING!!", "ID must not be empty, fill and try again.")
        elif int(x) not in sn:
            mb.showerror("ERROR", "Error: Not found in database.")
        else:
            cur1.execute(f"UPDATE students SET sName = '{nameE.get()}', sGender='{gend.get()}',"
                         f" sCourse='{showCourses()}', sAge={ageE.get()} WHERE sid={x}")
            con1.commit()
            mb.showinfo("Success Message", "Student's Info updated sucessfully!!")
            viewOne()

    # ===== To delete from database
    def deleteStudent():
        x = IDE.get()
        if x == "":
            mb.showwarning("WARNING!!", "ID must not be empty, fill and try again.")
        elif int(x) not in sn:
            mb.showerror("ERROR", "Error: Not found in database.")
        else:
            option = mb.askyesno("Confirm", f"Are you sure you want delete student with Id {x}?")
            if option == 1:
                chk = cur1.execute(f"DELETE FROM students WHERE sid={x}")
                if chk:
                    mb.showinfo("Message", "Data deleted sucessfully!")
                    con1.commit()
                else:
                    mb.showerror("ERROR", "Error deleting, try again")
            else:
                mb.showwarning("Message", "No changes made to your database")

    # =====Show general overview of students.
    def records():
        def show():
            x = viewStudents()
            stats = "S/N | ID  | STUDENT NAME |\n"
            Id = 1
            for i in x:
                stats = f"{stats}{str(Id)}      | {i[0]} | {i[1]}  \n"
                Id += 1
            txt.delete(1.0, END)
            txt.insert(INSERT, stats)

        rec = Tk()
        rec.title("STUDENTS GENERAL RECORDS")
        rec.geometry("500x300")
        rec.config(bg="#87bdc7")
        L = Label(rec, text="REGISTERED STUDENTS:", font=('candara', 14, 'bold'), bg="#87bdc7", fg="#ffffff")
        L.pack()
        txt = Text(rec, width=500, height=100, font=('candara', 14, 'bold'), fg="#000000")
        txt.pack()
        show()
        rec.mainloop()

    def exxit():
        sr.destroy()

    # =====Creating the application window.
    sr = Tk()
    sr.title("STUDENTS REGISTRATION")
    sr.geometry("1200x600")
    # FRAMES
    f1 = Frame(sr, width=1200, height=50, bd=3, bg="dark gray")
    f2 = Frame(sr, width=1200, height=100, bd=3, bg="white")
    f3 = Frame(sr, width=630, height=450, bg="dark gray", bd=3)
    f4 = Frame(sr, width=180, height=600, bg="grey", bd=3)
    f5 = Frame(sr, width=390, height=600, bg="#eeeeee", bd=3)
    # LABELS
    h = Label(f1, text="STUDENT REGISTRATION APP", bg="dark gray", font=('tahoma', 20, 'bold'))
    h.pack()
    h1 = Label(f2, text="Welcome to this app that makes registration  easy.", bg="white", font=('tahoma', 11, 'bold'))
    h1.pack()
    h2 = Label(f2, text="Click the COURSE button to view all available courses.", bg="white",
               font=('tahoma', 11, 'bold'), fg="blue")
    h2.pack()
    header = Label(f3, text="REGISTRATION FORM", bg="dark gray", font=('tahoma', 20, 'bold'))
    nameL = Label(f3, text="Name:", font=('tahoma', 13, 'bold'), bg="dark gray", fg="black")
    ageL = Label(f3, text="Age:", font=('tahoma', 13, 'bold'), bg="dark gray", fg="black")
    gendL = Label(f3, text="Gender:", font=('tahoma', 13, 'bold'), bg="dark gray", fg="black")
    courseL = Label(f3, text="Course:", font=('tahoma', 13, 'bold'), bg="dark gray", fg="black")
    IDL = Label(f4, text="Enter ID:", font=('tahoma', 13, 'bold'), bg="grey", fg="white")
    qrL = Label(f5, text="QRCODE \n \n  will be \n \n  displayed \n \n  here.", font=('tahoma', 13, 'bold'),
                bg="#eeeeee", fg="black")
    showL = Label(f5, font=('tahoma', 13, 'bold'), bg="#eeeeee", fg="black")
    # ID generated randomly
    v = r.randint(1, 600)
    # ENTRIES
    nameE = Entry(f3, font=("verdana", 13, "bold"), bd=3, justify="left")
    ageE = Entry(f3, font=("verdana", 13, "bold"), bd=3, justify="left")
    IDE = Entry(f4, font=("verdana", 13, "bold"), bd=3, justify="left")
    # RADIOBUTTONS
    gend = StringVar()
    rd1 = Radiobutton(f3, text="MALE", bg="dark gray", value="Male", variable=gend, font=("tahoma", 10, "bold"))
    rd2 = Radiobutton(f3, text="FEMALE", bg="dark gray", value="Female", variable=gend, font=("tahoma", 10, "bold"))
    # CHECKBOXES
    c1 = StringVar()
    c2 = StringVar()
    c3 = StringVar()
    c4 = StringVar()
    c5 = StringVar()
    c6 = StringVar()
    chbx1 = Checkbutton(f3, text="Java", variable=c1, bg="dark gray", font=('Consolas', 12, "bold"), onvalue='Java',
                        offvalue='')
    chbx2 = Checkbutton(f3, text="Python", variable=c2, bg="dark gray", font=("Consolas", 12, "bold"), onvalue="Python",
                        offvalue='')
    chbx3 = Checkbutton(f3, text="DBMS", variable=c3, bg="dark gray", font=("Consolas", 12, "bold"), onvalue="DBMS",
                        offvalue='')
    chbx4 = Checkbutton(f3, text="Mobile App Devt", variable=c4, bg="dark gray", font=("Consolas", 12, "bold"),
                        onvalue="Mobile App Devt", offvalue='')
    chbx5 = Checkbutton(f3, text="Computer Eng", variable=c5, bg="dark gray", font=("Consolas", 12, "bold"),
                        onvalue="Computer Eng", offvalue='')
    chbx6 = Checkbutton(f3, text="Web Development", variable=c6, bg="dark gray", font=("Consolas", 12, "bold"),
                        onvalue="Web Development", offvalue='')
    # BUTTONS
    b1 = Button(f2, text="COURSES", bg="silver", fg="black", font=('tahoma', 14, 'bold'), bd=3, command=viewCourses)
    b2 = Button(f3, bg="ivory", fg="cyan", text="View All Students", font=("tahoma", 12, "bold"), bd=3, command=records)
    b3 = Button(f3, bg="ivory", fg="cyan", text="REGISTER", font=("tahoma", 16, "bold"), bd=3, command=regStudent)
    b4 = Button(f4, bg="ivory", fg="cyan", text="UPDATE", font=("tahoma", 16, "bold"), bd=3, command=updateStudent)
    b5 = Button(f4, bg="ivory", fg="cyan", text="DELETE", font=("tahoma", 16, "bold"), bd=3, command=deleteStudent)
    b6 = Button(f4, bg="ivory", fg="cyan", text="View Student", font=("tahoma", 16, "bold"), bd=3, command=viewOne)
    b7 = Button(f3, bg="ivory", fg="cyan", text="CLEAR", font=("tahoma", 16, "bold"), bd=3, command=clear)
    b8 = Button(f4, bg="ivory", fg="cyan", text="Clear ID", font=("tahoma", 16, "bold"), bd=3, command=clrId)
    b9 = Button(f4, bg="ivory", fg="cyan", text="EXIT", font=("tahoma", 16, "bold"), bd=3, command=exxit)
    # Add widgets
    f1.pack()
    f2.pack()
    f4.pack(side="left")
    f5.pack(side="right")
    f3.pack()
    f1.pack_propagate(0)
    f2.pack_propagate(0)
    f3.grid_propagate(0)
    f4.pack_propagate(0)
    f5.pack_propagate(0)
    header.grid(row=0, column=0, columnspan=4, pady=10)
    nameL.grid(row=1, column=0, pady=10)
    ageL.grid(row=2, column=0, pady=10)
    gendL.grid(row=3, column=0, pady=10)
    courseL.grid(row=4, column=0, pady=10)
    nameE.grid(row=1, column=1, pady=10)
    ageE.grid(row=2, column=1, pady=10)
    rd1.grid(row=3, column=1, pady=10, sticky="nw")
    rd2.grid(row=3, column=2, pady=10, sticky="nw")
    b1.pack()
    chbx1.grid(row=4, column=1)
    chbx2.grid(row=4, column=2)
    chbx3.grid(row=5, column=1)
    chbx4.grid(row=6, column=1)
    chbx5.grid(row=5, column=2)
    chbx6.grid(row=6, column=2)
    b2.grid(row=9, column=1, pady=15, padx=10)
    b3.grid(row=8, column=0, pady=15, padx=10)
    b7.grid(row=8, column=2, pady=15, padx=10)
    showL.pack(pady=10)
    qrL.pack()
    IDL.pack(pady=10)
    IDE.pack(pady=10)
    b6.pack(pady=12)
    b4.pack(pady=12)
    b5.pack(pady=12)
    b8.pack(pady=15)
    b9.pack(pady=15)
    # RUN APP
    sr.mainloop()

# =============== REGISTRATION PORTAL FUNCTION==========================================================

window = Tk()
window.title("LOgIN")
window.geometry("500x450")
# FRAMES
frm1 = Frame(window, width=500, height=50, bg="brown")
frm1.pack()
frm1.pack_propagate(0)
frm2 = Frame(window, width=500, height=70, bg="white")
frm2.pack()
frm2.pack_propagate(0)
frm3 = Frame(window, width=500, height=330, bg="brown")
frm3.pack()
frm3.pack_propagate(0)
# List to hold username and passwords for reference
users = []
passw = []
# FUNCTIONS
con = sqlite3.connect("Playground.db")
cur = con.cursor()

def createTab():
    cur.execute("CREATE TABLE IF NOT EXISTS login(username TEXT PRIMARY KEY, password TEXT)")


def insertTab():
    a = usernE.get()
    b = passwE.get()
    if a == "" and b == "":
        mb.showwarning("Warning", "Username and Password cannot be empty!")
    elif a == "":
        mb.showwarning("Warning", "Username field cannot be empty!")
    elif b == "":
        mb.showwarning("Warning", "Password field cannot be empty!")
    else:
        createTab()
        cur.execute(f"INSERT INTO login VALUES('{a}', '{b}')")
        con.commit()
        mb.showinfo("Welcome Message", "Welcome to Lio!\nPlease proceed to the registration portal.")
        window.destroy()
        srp()


def checker():
    cur.execute("SELECT * FROM login")
    result = cur.fetchall()
    return result

def mini():
    wrap = checker()
    for i in wrap:
        users.append(i[0])
        passw.append(i[1])

def login():
    mini()
    x = usernE.get()
    y = passwE.get()
    if x == "" and y == "":
        mb.showwarning("Warning Message", "Enter valid username and password!")
    elif x == "":
        mb.showwarning("Warning!", "Enter valid username.")
    elif y == "":
        mb.showwarning("Warning!", "Enter valid password.")
    elif x not in users:
        mb.showerror("ERROR", "Error: invalid username,clear and try again.")
    elif y not in passw:
        mb.showerror("ERROR", "Error: invalid password,clear and try again.")
    else:
        mb.showinfo("Welcome Message", "Welcome back!\nProceed to the registration portal.")
        window.destroy()
        srp()


def clean():
    usernE.delete(0, END)
    passwE.delete(0, END)

# LABELS
hd = Label(frm1, text="WELCOME TO LiO REGISTRATION PLATFORM", bg="brown", fg="white", font=('Verdana', 14, 'bold'))
hd.pack()
hd2 = Label(frm2, text="Click SIGN-IN to sign up.\nIf already a member,\nclick LOGIN to go to student's portal.",
            bg="white", fg="brown", font=('Verdana', 11, 'bold'))
hd2.pack()
rgL = Label(frm3, text="LOGIN FORM", bg="brown", fg="black", font=('Verdana', 22, 'bold'))
rgL.pack()
usernL = Label(frm3, text="Username:", bg="brown", fg="white", font=('Verdana', 15, 'bold'))
usernL.pack()
usernE = Entry(frm3, font=('Verdana', 15, 'bold'), fg="brown", )
usernE.pack()
passwL = Label(frm3, text="Password:", bg="brown", fg="white", font=('Verdana', 15, 'bold'))
passwL.pack()
passwE = Entry(frm3, font=('Verdana', 15, 'bold'), fg="brown", show="*")
passwE.pack()
# BUTTONS
btn1 = Button(frm3, text="SIGN-UP", fg="brown", bg="white", font=('Verdana', 15, 'bold'), command=insertTab)
btn1.pack(side="left", anchor="ne", pady=15, padx=20)
btn2 = Button(frm3, text="LOGIN", fg="brown", bg="white", font=('Verdana', 15, 'bold'), command=login)
btn2.pack(side="right", anchor="n", pady=15, padx=40)
btn3 = Button(frm3, text="Clear", fg="brown", bg="white", font=('Verdana', 15, 'bold'), command=clean)
btn3.pack(pady=15, padx=40)
# RUNAPP
window.mainloop()