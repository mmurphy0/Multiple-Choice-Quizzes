import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

import time
from time import strftime

def question3(question2_win):
    def q3_correct():
        correct()
        question4(question3_win)

    def q3_incorrect(question2_win):
        messagebox.showinfo('Result','Incorrect, The answer is Michael Scott')
        question4(question3_win)

    question3_win = Toplevel()
    question3_win.geometry('0+0')
    question3_win.resizable(False,False)
    question3_win.title('The Office (US) Quiz - Q3')

    q3_label = tk.Label(
        question3_win,
        text='Who is the Regional Manager at the start of the show?',
        font=('Arial',20)
    )
    q3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q3_button_a = tk.Button(
        question3_win,
        text='Michael Scott',
        font=('Arial'),
        width=15,
        command=q3_correct
    )
    q3_button_a.grid(
        row=3,
        column=1
    )

    q3_button_b = tk.Button(
        question3_win,
        text='Dwight Schrute',
        font=('Arial'),
        width=15,
        command=q3_incorrect
    )
    q3_button_b.grid(
        row=3,
        column=2
    )

    q3_button_c = tk.Button(
        question3_win,
        text='Jim Halpert',
        font=('Arial'),
        width=15,
        command=q3_incorrect
    )
    q3_button_c.grid(
        row=4,
        column=1
    )

    q3_button_d = tk.Button(
        question3_win,
        text='Andy Bernard',
        font=('Arial'),
        width=15,
        command=q3_incorrect
    )
    q3_button_d.grid(
        row=4,
        column=2
    )

def question2(question1_win):
    def q2_correct():
        correct()
        question3(question2_win)

    def q2_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is True')
        question3(question2_win)

    question2_win = Toplevel()
    question2_win.geometry('0+0')
    question2_win.resizable(False,False)
    question2_win.title('The Office (US) Quiz - Q2')

    q2_label = tk.Label(
        question2_win,
        text='Dwight Schrute owns a large beet farm?',
        font=('Arial',20)
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

def question1():
    def q1_correct():
        correct()
        question2(question1_win)

    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Dunder Mifflin')
        question2(question1_win)

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