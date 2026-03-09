import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

import time
from time import strftime

def correct():
    messagebox.showinfo('Result','Correct!')
    global score
    score += 1
    return

score = 0

root_win = tk.Tk()
root_win.geometry('')
root_win.resizable(False,False)
root_win.title('The Office (US) Quiz')

root_label = tk.Label(
    root_win,
    text='The Office (US) Quiz',
    font=('Arial',20,'bold')
)
root_label.pack()

startquiz_button = tk.Button(
    root_win,
    text='Start',
    font=('Arial'),
    width=20
    # command=question1
)
startquiz_button.pack()

root_win.mainloop()