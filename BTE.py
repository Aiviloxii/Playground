# Create a GUI that uses a button to open a text file and places the contents in your text area.
from tkinter import *
def show():
    filename = "bteFile.txt"
    obj = open(filename, 'r')
    d = (obj.read())
    txt.delete(1.0, END)
    txt.insert('1.0', d)

bte = Tk()
bte.geometry("720x650")
bte.title("Text Editor")
# frames
f1 = Frame(bte, width=720, height=80, bg="#117fbe")
f2 = Frame(bte, width=720,height=450,bg="#ffffff")
# labels
t = Label(f1, text="BAKWO TEXT EDITOR", font=('Tahoma', 28), bg="#117fbe", fg="#ffffff", )
txt = Text(f2, font=('Consolas', 14), bd=5)
# button
btn= Button(bte, text="Load File", bg="#117fbe", fg="yellow", font=('Segoe UI Semibold',16), command=show)
f1.pack()
f2.pack()
f1.pack_propagate(0)
f2.pack_propagate(0)
t.pack(pady=10)
txt.pack()
btn.pack(side="bottom",anchor='center',pady=39,padx=4)

bte.mainloop()