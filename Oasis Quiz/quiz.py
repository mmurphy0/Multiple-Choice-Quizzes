import tkinter as tk
from tkinter import messagebox, Toplevel
import time
from time import strftime

def question2():
    def q2_correct():
        correct()
        question3()

    def q2_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is True')
        question3()

    global question2_win

    question2_win = Toplevel()
    question2_win.geometry('380x50+0+0')
    question2_win.resizable(False,False)
    question2_win.title('Oasis Quiz - Q2')

    q2_label = tk.Label(
        question2_win,
        text='Did Oasis Reunite?',
        font=('Arial',20),
    )
    q2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q2_button_a = tk.Button(
        question2_win,
        text='True',
        font=('Arial'),
        width=15,
        command=q2_correct
    )
    q2_button_a.grid(
        row=3,
        column=1
    )

    q2_button_b = tk.Button(
        question2_win,
        text='False',
        font=('Arial'),
        width=15,
        command=q2_incorrect
    )
    q2_button_b.grid(
        row=3,
        column=2
    )

    question1_win.destroy()

def question1():
    def q1_correct():
        correct()
        question2()

    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 1991')
        question2()

    global question1_win

    question1_win = Toplevel()
    question1_win.geometry('380x90+0+0')
    question1_win.resizable(False,False)
    question1_win.title('Oasis Quiz - Q1')

    q1_label = tk.Label(
        question1_win,
        text='What year were Oasis formed?',
        font=('Arial'),
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = tk.Button(
        question1_win,
        text='1988',
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
        text='1991',
        font=('Arial'),
        width=15,
        command=q1_correct
    )
    q1_button_b.grid(
        row=3,
        column=2
    )

    q1_button_c = tk.Button(
        question1_win,
        text='1993',
        font=('Arial'),
        width=15,
        command=q1_incorrect
    )
    q1_button_c.grid(
        row=4,
        column=1
    )

    q1_button_d = tk.Button(
        question1_win,
        text='1990',
        font=('Arial'),
        width=15,
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
root.geometry('150x60+0+0')
root.resizable(False,False)
root.title('Oasis Quiz')

root_label = tk.Label(
    root,
    text='Oasis Quiz',
    font=('Arial',20,'bold')
)
root_label.pack()

startquiz_button = tk.Button(
    root,
    text='Start',
    font=('Arial'),
    width=20,
    command=question1
)

root.mainloop()