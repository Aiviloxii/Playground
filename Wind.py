from tkinter import *
def print1():
    txt1 = txt.get(1.0,'end')
    print(txt1)


window = Tk()
window.title("Hello World")
window.geometry("640x480")
leftFrame = Frame(window, bg="#e0d192", width=120, height=480)
rightFrame = Frame(window, bg="#a74a2f", width=520, height=480)
txt = Text(rightFrame, width=500, height=470, font=('Arial', 16)).pack()
b = Button(leftFrame, text="Print", bg="chocolate", fg="black", font=('cursive', 16), command=print1)
b.pack(side="bottom", pady=10)
leftFrame.pack(side="left")
rightFrame.pack(side="right")
leftFrame.pack_propagate(0)
rightFrame.pack_propagate(0)
window.mainloop()
