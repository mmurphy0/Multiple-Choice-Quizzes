import tkinter as tk
from tkinter import messagebox, Toplevel
import datetime
from datetime import datetime

score = 0

def question_1():
    def correct():
        messagebox.showinfo('Result','Correct!')
        score = score + 1

    def incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is London')

    question1_win = Toplevel()
    question1_win.geometry('280x90')
    question1_win.minsize(280,90)
    question1_win.minsize(280,90)

    text = tk.Label(
        question1_win,
        text='What is the capital of England?',
        font=('Arial',20)
    )
    text.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question1_button_a = tk.Button(
        question1_win,
        text='London',
        font=('Arial'),
        width=10,
        command=correct
    )
    question1_button_a.grid(
        row=3,
        column=1
    )

    question1_button_b = tk.Button(
        question1_win,
        text='Liverpool',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question1_button_b.grid(
        row=4,
        column=1
    )

    question1_button_c = tk.Button(
        question1_win,
        text='Manchester',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question1_button_c.grid(
        row=3,
        column=2
    )

    question1_button_d = tk.Button(
        question1_win,
        text='Birmingham',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question1_button_d.grid(
        row=4,
        column=2
    )


root = tk.Tk()
root.geometry('155x60')
root.minsize(155,60)
root.maxsize(155,60)
root.title('Capital City Quiz')

root_title = tk.Label(
    root,
    text='Capital City Quiz',
    font=('Arial',20)
)
root_title.pack()

start_button = tk.Button(
    root,
    text='Start Quiz',
    font=('Arial'),
    command=question_1
)
start_button.pack()

root.mainloop()