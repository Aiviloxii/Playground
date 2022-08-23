# A program to test my idea of a RMA
from tkinter import *
import random as r
import time

root = Tk()
root.geometry("1600x700")
root.title("RESTAURANT MANAGEMENT SYSTEM")
tops = Frame(root, bg="white", width=1600, height=50, relief=SUNKEN)
tops.pack()
f1 = Frame(root,width=900, height=700, relief=SUNKEN)
f1.pack(side="left")
f2 = Frame(root,bg="white",width=400, height=700, relief=SUNKEN)
f2.pack(side="right")
# TIME
clock = time.ctime(time.time())
# For First Frame
lblinfo = Label(tops, text="RESTAURANT MANAGEMENT", font=('Arial', 20, 'bold'), bg="white", fg="dark blue", anchor="w")
lblinfo.grid(row=0, column=0)
lbl2 = Label(tops, text=clock, font=('Arial', 18, 'bold'), bg="white", fg="black", anchor=W)
lbl2.grid(row=1, column=0)
#Calculator
ti = StringVar()
op = ""
td = Entry(f2, textvariable=ti, bd=5,insertwidth=7, bg="white",justify="right", font=('arial',17, 'bold'))
td.grid(columnspan=4)
#calc functions
def click(num):
    global op
    op = op + str(num)
    ti.set(op)

def clrDisplay():
    global op
    op = ""
    ti.set("")

def equals():
    global op
    su=str(eval(op))

    ti.set(su)
    op=""

def ref():
    x = r.randint(12980, 50876)
    rr = str(x)
    reff.set(rr)
    moi = float(moimoi.get())
    dn = float(donuts.get())
    tst = float(toasts.get())
    pnc = float(pancakes.get())
    moip = moi *50
    dnp = dn * 50
    tstp = tst * 50
    pncp = pnc * 50

    d_cost = "N",str(moip + dnp + tstp + pncp)
    p_tax = ((moip + dnp + tstp + pncp) * 0.30)
    s_charge = ((moip + dnp + tstp + pncp)/99)
    oac = "N", str(p_tax + (moip + dnp + tstp + pncp) + s_charge)
    sc = "N", str(s_charge)
    tx = "N", str(p_tax)
    service_charge.set(sc)
    cost.set(d_cost)
    tax.set(tx)
    total.set(oac)

def calcexit():
    root.destroy()

def reset():
    reff.set("")
    moimoi.set("")
    donuts.set("")
    pancakes.set("")
    toasts.set("")
    total.set("")
    tax.set("")
    service_charge.set("")
    cost.set("")

b7 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="7", command=lambda:click(7))
b7.grid(row=2, column=0)
b8 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="8", command=lambda:click(8))
b8.grid(row=2, column=1)
b9 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="9", command=lambda:click(9))
b9.grid(row=2, column=2)
add = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="+", command=lambda:click("+"))
add.grid(row=2, column=3)
b4 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="4", command=lambda:click(4))
b4.grid(row=3, column=0)
b5 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="5", command=lambda:click(5))
b5.grid(row=3, column=1)
b6 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="6", command=lambda:click(6))
b6.grid(row=3, column=2)
sub = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="-", command=lambda:click("-"))
sub.grid(row=3, column=3)
b1 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="1", command=lambda:click(1))
b1.grid(row=4, column=0)
b2 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="2", command=lambda:click(2))
b2.grid(row=4, column=1)
b3 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="3", command=lambda:click(3))
b3.grid(row=4, column=2)
mul = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="*", command=lambda:click("*"))
mul.grid(row=4, column=3)
b0 = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="0", command=lambda:click(0))
b0.grid(row=5, column=0)
bc = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="C", command=clrDisplay)
bc.grid(row=5, column=1)
be = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="=", command=equals)
be.grid(columnspan=4)
dec = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text=".", command=lambda:click("."))
dec.grid(row=5, column=2)
div = Button(f2, padx=16, pady=16, bd=4,bg="black", fg="blue", font=('cursive', 14, 'bold'), text="/", command=lambda:click("/"))
div.grid(row=5, column=3)
stats = Label(f2, text="By AIVILO", font=('verdana', 12, 'bold'), bd=2, width=16,relief=SUNKEN)
stats.grid(row=7, columnspan=3)
#Textvariables
reff = StringVar()
moimoi = StringVar()
pancakes = StringVar()
donuts = StringVar()
toasts = StringVar()
total = StringVar()
service_charge = StringVar()
tax = StringVar()
cost = StringVar()

refL = Label(f1, text="Order No.", fg="blue", bd=10, font=('verdana', 16, 'bold'), anchor="w")
refL.grid(row=0, column=0)
refE = Entry(f1, textvariable=reff, bd=6, insertwidth=4, font=('arial', 16, 'bold'), justify='right')
refE.grid(row=0, column=1)
moiL = Label(f1, text="Moimoi", fg="blue", bd=10, font=('verdana', 16, 'bold'), anchor="w")
moiL.grid(row=1, column=0)
moiE = Entry(f1, textvariable=moimoi, bd=6, insertwidth=4, font=('arial', 16, 'bold'), justify='right')
moiE.grid(row=1, column=1)
panL = Label(f1, text="Pancakes", fg="blue", bd=10, font=('verdana', 16, 'bold'), anchor="w")
panL.grid(row=2, column=0)
panE = Entry(f1, textvariable=pancakes, bd=6, insertwidth=4, font=('arial', 16, 'bold'), justify='right')
panE.grid(row=2, column=1)
donL = Label(f1, text="Donuts", fg="blue", bd=10, font=('verdana', 16, 'bold'), anchor="w")
donL.grid(row=3, column=0)
donE = Entry(f1, textvariable=donuts, bd=6, insertwidth=4, font=('arial', 16, 'bold'), justify='right')
donE.grid(row=3, column=1)
toaL = Label(f1, text="Toasts", fg="blue", bd=10, font=('verdana', 16, 'bold'), anchor="w")
toaL.grid(row=4, column=0)
toaE = Entry(f1, textvariable=toasts, bd=6, insertwidth=4, font=('arial', 16, 'bold'), justify='right')
toaE.grid(row=4, column=1)
costL = Label(f1, text="Cost:", fg="blue", bd=10, font=('verdana', 16, 'bold'), anchor="w")
costL.grid(row=0, column=2)
costE = Entry(f1, textvariable=cost, bd=6, insertwidth=4, font=('arial', 16, 'bold'), justify='right')
costE.grid(row=0, column=3)
taxL = Label(f1, text="TAX:", fg="blue", bd=10, font=('verdana', 16, 'bold'), anchor="w")
taxL.grid(row=1, column=2)
taxE = Entry(f1, textvariable=tax, bd=6, insertwidth=4, font=('arial', 16, 'bold'), justify='right')
taxE.grid(row=1, column=3)
service_chargeL = Label(f1, text="Service Charge", fg="blue", bd=10, font=('verdana', 16, 'bold'), anchor="w")
service_chargeL.grid(row=2, column=2)
service_chargeE = Entry(f1, textvariable=service_charge, bd=6, insertwidth=4, font=('arial', 16, 'bold'), justify='right')
service_chargeE.grid(row=2, column=3)
totalL = Label(f1, text="Total", fg="blue", bd=10, font=('verdana', 16, 'bold'), anchor="w")
totalL.grid(row=3, column=2)
totalE = Entry(f1, textvariable=total, bd=6, insertwidth=4, font=('arial', 16, 'bold'), justify='right')
totalE.grid(row=3, column=3)
#buttons
totb = Button(f1, padx=16, pady=8, bd=10, fg="white", bg="teal", width=10, text="TOTAL",font=('cursive', 16, 'bold'),command=ref)
totb.grid(row=6, column=1)
resetb = Button(f1, padx=16, pady=8, bd=10, fg="white", bg="teal", width=10, text="RESET",font=('cursive', 16, 'bold'),command=reset)
resetb.grid(row=6, column=2)
exitb = Button(f1, padx=16, pady=8, bd=10, fg="white", bg="teal", width=10, text="EXIT",font=('cursive', 16, 'bold'),command=calcexit)
exitb.grid(row=6, column=3)

def price():
    branch = Tk()
    branch.geometry("600x220")
    branch.title("Price List")
    branch.config(bg="dark blue")
    prod = Label(branch, text="PRODUCTS", bg="dark blue", fg="#c8bfe7", font=("impact", 15, 'bold'), bd=5)
    prod.grid(row=0, column=0)
    line = Label(branch, text="-------------", bg="dark blue", fg="white", font=("impact", 15, 'bold'), bd=5)
    line.grid(row=0, column=2)
    pric = Label(branch, text="PRICE", bg="dark blue", fg="#c8bfe7", font=("impact", 15, 'bold'),anchor=W)
    pric.grid(row=0, column=3)
    mmi = Label(branch, text="MOIMOI", bg="dark blue", fg="white", font=("impact", 15, 'bold'), anchor=W)
    mmi.grid(row=1, column=0)
    mm = Label(branch, text="N50", bg="dark blue", fg="white", font=("impact", 15, 'bold'), anchor=W)
    mm.grid(row=1, column=3)
    pci = Label(branch, text="PANCAKES", bg="dark blue", fg="white", font=("impact", 15, 'bold'), anchor=W)
    pci.grid(row=2, column=0)
    pc = Label(branch, text="N50", bg="dark blue", fg="white", font=("impact", 15, 'bold'), anchor=W)
    pc.grid(row=2, column=3)
    dni = Label(branch, text="DONUTS", bg="dark blue", fg="white", font=("impact", 15, 'bold'), anchor=W)
    dni.grid(row=3, column=0)
    dn = Label(branch, text="N50", bg="dark blue", fg="white", font=("impact", 15, 'bold'), anchor=W)
    dn.grid(row=3, column=3)
    tsi = Label(branch, text="TOASTS", bg="dark blue", fg="white", font=("impact", 15, 'bold'), anchor=W)
    tsi.grid(row=4, column=0)
    ts = Label(branch, text="N50", bg="dark blue", fg="white", font=("impact", 15, 'bold'), anchor=W)
    ts.grid(row=4, column=3)

    branch.mainloop()

priceb = Button(f1, padx=16, pady=8, bd=10, fg="white", bg="teal", width=10, text="PRICE",font=('cursive', 16, 'bold'),command=price)
priceb.grid(row=6, column=0)


root.mainloop()