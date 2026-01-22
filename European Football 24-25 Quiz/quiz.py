import tkinter as tk
from tkinter import messagebox, Toplevel
from time import strftime

def question1():
    def q1_correct():
        correct()
        question2()

    def q1_incorrect():
        messagebox.showinfo('Result','The answer is Liverpool')
        question2()

    global question1_win

    question1_win = Toplevel()
    question1_win.geometry('350x90+0+0')
    question1_win.resizable(False,False)
    question1_win.title('European Football 24-25 Quiz - Q1')

    q1_label = tk.Label(
        question1_win,
        text='Who won the Premier League?',
        font=('Arial',20)
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = tk.Button(
        question1_win,
        text='Liverpool',
        font=('Arial'),
        width=15,
        command=q1_correct
    )
    q1_button_a.grid(
        row=3,
        column=1
    )

    q1_button_b = tk.Button(
        question1_win,
        text='Arsenal',
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
        text='Manchester City',
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
        text='Chelsea',
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

root = tk.Tk()
root.geometry('280x60+0+0')
root.resizable(False,False)
root.title('European Football 24-25 Quiz')

root_label = tk.Label(
    root,
    text='European Football 24-25 Quiz',
    font=('Arial',20,'bold')
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