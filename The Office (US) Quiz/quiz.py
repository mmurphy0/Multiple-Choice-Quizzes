import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

import time
from time import strftime

def question1():
    def q1_correct():
        correct()
        question2()

    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Dunder Mifflin')
        question2()

    question1_win = Toplevel()
    question1_win.geometry('0+0')
    question1_win.resizable(False,False)
    question1_win.title('The Office (US) Quiz - Q1')

    q1_label = tk.Label(
        question1_win,
        text='What is the name of the paper company?',
        font=('Arial',20)
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = tk.Button(
        question1_win,
        text='Penn Paper',
        font=('Arial'),
        width=15,
        command=q1_incorrect
    )
    q1_button_a.grid(
        row=3,
        column=1
    )

    q1_button_b = tk.Button(
        question1_win,
        text='Scranton Paper Co.',
        font=('Arial'),
        width=15,
        command=q1_incorrect
    )
    q1_button_b.grid(
        row=3,
        column=2
    )

    q1_button_c = tk.Button(
        question1_win,
        text='Dunder Mifflin',
        font=('Arial'),
        width=15,
        command=q1_correct
    )
    q1_button_c.grid(
        row=4,
        column=1
    )

    q1_button_d = tk.Button(
        question1_win,
        text='Northeast Paper',
        font=('Arial'),
        width=15,
        command=q1_incorrect
    )
    q1_button_d.grid(
        row=4,
        column=2
    )

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
    width=20,
    command=question1
)
startquiz_button.pack()

root_win.mainloop()