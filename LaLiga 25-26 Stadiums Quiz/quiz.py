import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

from time import strftime

def correct():
    global score
    score += 1
    messagebox.showinfo('Result','Correct!')
    return

score = 0

root = tk.Tk()
root.geometry('+0+0')
root.resizable(False,False)
root.title('LaLiga 25-26 Stadiums Quiz')

root_title = tk.Label(
    root,
    text='LaLiga 25-26 Stadiums Quiz',
    font=('Arial',20,'bold')
)
root_title.pack()

continue_button = tk.Button(
    root,
    text='Continue',
    font=('Arial'),
    width=20,
    command=question1
)

root.mainloop()