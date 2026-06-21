import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

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
root.title('Ligue 1 25-26 Stadiums Quiz')

root_title = tk.Label(
    root,
    text='Ligue 1 25-26 Stadiums Quiz',
    font=('Arial',20,'bold')
)
root_title.pack()

start_button = tk.Button(
    root,
    text='Start',
    font=('Arial'),
    width=20,
    command=question1
)
start_button.pack()

root.mainloop()