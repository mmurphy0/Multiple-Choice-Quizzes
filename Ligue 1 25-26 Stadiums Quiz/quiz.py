import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

from time import strftime

def question1():
    def q1_correct():
        correct()
        question2(question1_win)

    def q1_incorrect():
        messagebox.showinfo('Result','The answer is the Parc des Princes')
        question2(question1_win)

    question1_win = Toplevel()
    question1_win.geometry('+0+0')
    question1_win.resizable(False,False)
    question1_win.title('Ligue 1 25-26 Stadiums Quiz')

    q1_label = tk.Label(
        question1_win,
        text='What is the PSG Stadium called?',
        font=('Arial',20)
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = tk.Button(
        question1_win,
        text='Stade Bollaert-Delelis',
        font=('Arial'),
        width=20,
        command=q1_incorrect
    )
    q1_button_a.grid(
        row=3,
        column=1
    )

    q1_button_b = tk.Button(
        question1_win,
        text='Parc des Princes',
        font=('Arial'),
        width=20,
        command=q1_correct
    )
    q1_button_b.grid(
        row=3,
        column=2
    )

    q1_button_c = tk.Button(
        question1_win,
        text='Groupama Stadium',
        font=('Arial'),
        width=20,
        command=q1_incorrect
    )
    q1_button_c.grid(
        row=4,
        column=1
    )

    q1_button_d = tk.Button(
        question1_win,
        text='Orange Vélodrome',
        font=('Arial'),
        width=20,
        command=q1_incorrect
    )
    q1_button_d.grid(
        row=4,
        column=2
    )

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