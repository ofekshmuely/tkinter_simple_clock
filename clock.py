

from tkinter import *
from time import strftime


root = Tk()
root.title("Digital Clock")


def timeDisplay():
    str = strftime("%H:%M:%S")
    lbl.config(text=str)
    lbl.after(1000, timeDisplay)


lbl = Label(root, font=("ariel", 160, "bold"), bg='black', fg="white")
lbl.pack(anchor="center", fill="both", expand=1)


timeDisplay()
mainloop()
