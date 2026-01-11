import tkinter as tk
from tkinter import Toplevel, messagebox
import datetime
from datetime import datetime

def question2():
    def q2_correct():
        correct()
        question3()

    def q2_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is McLaren')
        question3

    question2_win = Toplevel()
    question2_win.geometry('320x90+0+0')
    question2_win.resizable(False,False)
    question2_win.title('F1 2025 Quiz - Q2')

    question2_button_a = tk.Button(
        question2_win,
        text='Mercedes',
        font=('Arial'),
        width=15,
        command=q2_incorrect
    )
    question2_button_a.grid(
        row=3,
        column=1
    )

    question2_button_b = tk.Button(
        question2_win,
        text='Ferrari',
        font=('Arial'),
        width=15,
        command=q2_incorrect
    )
    question2_button_b.grid(
        row=3,
        column=2
    )

    question2_button_c = tk.Button(
        question2_win,
        text='Red Bull Racing',
        font=('Arial'),
        width=15,
        command=q2_incorrect
    )
    question2_button_c.grid(
        row=4,
        column=1
    )

    question2_button_d = tk.Button(
        question2_win,
        text='McLaren',
        font=('Arial'),
        width=15,
        command=q2_correct
    )
    question2_button_d.grid(
        row=4,
        column=2
    )


def question1():
    def q1_correct():
        correct()
        question2()
    
    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Lando Norris')
        question2()

    question1_win = Toplevel()
    question1_win.geometry('320x90+0+0')
    question1_win.resizable(False,False)
    question1_win.title('F1 2025 Quiz - Q1')

    question1_label = tk.Label(
        question1_win,
        text="Who won the Driver's Championship?",
        font=('Arial',20)
    )
    question1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question1_button_a = tk.Button(
        question1_win,
        text='Max Verstappen',
        font=('Arial'),
        width=15,
        command=q1_incorrect
    )
    question1_button_a.grid(
        row=3,
        column=1
    )

    question1_button_b = tk.Button(
        question1_win,
        text='Oscar Piastri',
        font=('Arial'),
        width=15,
        command=q1_incorrect
    )
    question1_button_b.grid(
        row=3,
        column=2
    )

    question1_button_c = tk.Button(
        question1_win,
        text='Lando Norris',
        font=('Arial'),
        width=15,
        command=q1_correct
    )
    question1_button_c.grid(
        row=4,
        column=1
    )

    question1_button_d = tk.Button(
        question1_win,
        text='George Russell',
        font=('Arial'),
        width=15,
        command=q1_incorrect
    )
    question1_button_d.grid(
        row=4,
        column=2
    )


def correct():
    global score
    score += 1
    messagebox.showinfo('Result','Correct!')
    return

root = tk.Tk()
root.geometry('150x60+0+0')
root.resizable(False,False)
root.title('F1 2025 Quiz')

root_title = tk.Label(
    root,
    text='F1 2025 Quiz',
    font=('Arial',20,'bold')
)
root_title.pack()

start_button = tk.Button(
    root,
    text='Start Quiz',
    font=('Arial'),
    width=20
)
start_button.pack()

root.mainloop()