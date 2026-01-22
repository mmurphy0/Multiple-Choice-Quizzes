import tkinter as tk
from tkinter import messagebox, Toplevel
from time import strftime


def correct():
    global score
    score += 1
    messagebox.showinfo('Result','Correct!')
    return

root = tk.Tk()
root.geometry('280x60+0+0')
root.resizable(False,False)
root.title('European Football 24-25 Quiz')

root_label = tk.Label(
    root,
    text='European Football 24-25 Quiz',
    font=('Arial',20)
)
root_label.pack()

startquiz_button = tk.Button(
    root,
    text='Start Quiz',
    font=('Arial'),
    width=20,
    # command=question1
)
startquiz_button.pack()

root.mainloop()