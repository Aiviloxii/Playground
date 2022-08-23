from tkinter import *
def print():
    t.delete('1.0','end')
    d = "Welcome!!!!!!"
    t.insert('1.0', d)

window = Tk()
window.geometry("700x600")
window.title("Text Example")
window.config(bg="#ffffff")

t = Text(window, font=('Verdana', 16), bg="#fdeca6", fg="#32da6a", width=50, height=20)
b = Button(window,bg="#000000", fg="silver", text="Print", font=('cooper black', 18), command=print)

t.pack()
b.pack()

window.mainloop()