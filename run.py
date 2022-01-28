from tkinter import *
import random

color = "blue"

window = Tk()
window.title("TicTacToe by vh64g")
window.configure(bg="black")


def reset_all():
    aa.configure(bg="black")
    ab.configure(bg="black")
    ac.configure(bg="black")
    ba.configure(bg="black")
    bb.configure(bg="black")
    bc.configure(bg="black")
    ca.configure(bg="black")
    cb.configure(bg="black")
    cc.configure(bg="black")
    print("reset all")


def reset_color():
    global color
    gb = ["blue", "orange"]
    color = random.choice(gb)
    print("random color set")


def next_color():
    global color
    if color == "blue":
        color = "orange"
        sc.configure(bg=color)
        print("color set to orange")
    elif color == "orange":
        color = "blue"
        sc.configure(bg=color)
        print("color set to blue")
    else:
        color = "red"
        sc.configure(bg=color)
        print("failed to set new color")


def choose_aa():
    aa.configure(bg=color)
    next_color()


def choose_ab():
    ab.configure(bg=color)
    next_color()


def choose_ac():
    ac.configure(bg=color)
    next_color()


def choose_ba():
    ba.configure(bg=color)
    next_color()


def choose_bb():
    bb.configure(bg=color)
    next_color()


def choose_bc():
    bc.configure(bg=color)
    next_color()


def choose_ca():
    ca.configure(bg=color)
    next_color()


def choose_cb():
    cb.configure(bg=color)
    next_color()


def choose_cc():
    cc.configure(bg=color)
    next_color()


reset_color()

aa = Button(window, pady=25, padx=30, bg="black", command=choose_aa)
ab = Button(window, pady=25, padx=30, bg="black", command=choose_ab)
ac = Button(window, pady=25, padx=30, bg="black", command=choose_ac)

ba = Button(window, pady=25, padx=30, bg="black", command=choose_ba)
bb = Button(window, pady=25, padx=30, bg="black", command=choose_bb)
bc = Button(window, pady=25, padx=30, bg="black", command=choose_bc)

ca = Button(window, pady=25, padx=30, bg="black", command=choose_ca)
cb = Button(window, pady=25, padx=30, bg="black", command=choose_cb)
cc = Button(window, pady=25, padx=30, bg="black", command=choose_cc)

scl = Label(window, text="color : ", fg="#FF00FF", bg="black")
sc = Label(window, bg=color, pady=5, padx=30)
reset = Button(window, padx=15, bg="black", fg="red", text="reset", command=reset_all)

aa.grid(row=1, column=1)
ab.grid(row=1, column=2)
ac.grid(row=1, column=3)

ba.grid(row=2, column=1)
bb.grid(row=2, column=2)
bc.grid(row=2, column=3)

ca.grid(row=3, column=1)
cb.grid(row=3, column=2)
cc.grid(row=3, column=3)

scl.grid(row=4, column=1)
sc.grid(row=4, column=2)
reset.grid(row=4, column=3)

window.mainloop()
