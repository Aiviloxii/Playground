# Create a Tkinter program to create two folders with two different files.
# The first file, a text file. The second file, a text file with info about the first file.
# Information such as name, number of words, number of characters in the first file.
from tkinter import *
import os
from tkinter import messagebox as mb
def delt():
    for widgets in f3.winfo_children():
        widgets.destroy()
def createfolder():
    delt()
    foldname = Label(f3, text='Enter the name for the folder you are creating:',bg="#874750", font=('courier',19))
    fname = StringVar()
    fdname = Entry(f3, textvariable=fname, font=('courier',18))
    newpath = r"C:\Users\Olivia\PycharmProjects\GREGG\fname.get()"
    if not os.path.exists(newpath):
        os.mkdir(newpath)

    def fd():
        mb.showinfo('SUCCESS', 'Folder created successfully\nCheck the parent folder to confirm.')

    def clrf():
        fname.set('')

    fdbut = Button(f3, text="Create Folder", bg="brown", bd=3, command=fd, font=('verdana', 16), fg="#ffffff")
    fdbut2 = Button(f3, text="Reset", bg="brown", bd=3, command=clrf, font=('verdana', 16), fg="#ffffff")
    foldname.pack(pady=10)
    fdname.pack(pady=10)
    fdbut.pack(pady=10)
    fdbut2.pack(pady=10)

def createfile():
    delt()
    os.chdir(r"C:\Users\Olivia\PycharmProjects\GREGG\a")
    filename = Label(f3, text='Enter the filename for the first folder:', bg="#874750", font=('courier', 19))
    filname = StringVar()
    flname = Entry(f3, textvariable=filname, font=('courier', 18))
    c = filname.get()
    txt = "Welcome to Bakwo's Text Editor.\nThis is your first file created\nin your first folder."
    fileobject = open(f'{c}.txt',"w")
    fileobject.write(txt)
    fileobject.close()
    os.chdir(r"C:\Users\Olivia\PycharmProjects\GREGG\fname.get()")
    filename2 = Label(f3, text='Enter the filename for second folder:', bg="#874750", font=('courier', 19))
    filname2 = StringVar()
    flname2 = Entry(f3, textvariable=filname2, font=('courier', 18))
    f = filname2.get()
    d1 = len(txt)
    d = txt.split()
    d2 = len(d)
    data = f"The number of characters in your first file is: {d1}\nThe number of words are: {d2}"
    obj = open(f'{f}.txt', 'w')
    obj.write(data)
    obj.close()

    def fl():
        mb.showinfo('SUCCESS', 'Your file has been created successfully!\nYou can check the folder.')

    def clrf():
        filname.set('')

    flbut = Button(f3, text="Create File", bg="brown", bd=3, command=fl, font=('verdana', 16), fg="#ffffff")
    flbut2 = Button(f3, text="Reset", bg="brown", bd=3, command=clrf, font=('verdana', 16), fg="#ffffff")

    filename.pack()
    flname.pack()
    filename2.pack()
    flname2.pack()
    flbut.pack(pady=20)
    flbut2.pack(pady=20)


fold = Tk()
fold.title("Folder and Files Creation")
fold.geometry("850x650")
fold.config(bg="#ffffff")
# Frames
f = Frame(fold, width=850, height=80, bd=10, bg='#874787')
f2 = Frame(fold, width=100, height=650, bd=10, bg='#874743')
f3 = Frame(fold, width=850, height=380, bg="#874750")
f4 = Frame(fold, width=850, height=250)
# First Frame
hd= Label(f, text="Welcome to Bakwo's Directory\nCreate your folders and files with a click.", bg="#874787", fg="#000000", font=('Constantia',18))
# Second Frame
but1 = Button(f2, text="Folder", bg="#ffced4", fg="#000000", font=('small fonts',14), bd=3, command=createfolder)
but2 = Button(f2, text="File", bg="#ffced4", fg="#000000", font=('small fonts',14), bd=3, command=createfile)
# Third Frame
cl = Label(f3, text="Click any of the buttons on the left\nas the case may be.", font=('Arial Black',22), bg='#874750')
# Fourth Frame
output = Text(f4, font=('Consolas', 14), bd=2, fg='teal')

f.pack()
f2.pack(side='left')
f3.pack()
f4.pack()
f.pack_propagate(0)
f2.pack_propagate(0)
f3.pack_propagate(0)
f4.pack_propagate(0)
hd.pack()
but1.pack(pady=10)
but2.pack(pady=10)
output.pack()
cl.pack()

fold.mainloop()