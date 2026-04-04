import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

from time import strftime

def question1():
    def q1_correct():
        correct()
        question2()

    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Anfield')
        question2()

    question1_win = Toplevel()
    question1_win.geometry('+0+0')
    question1_win.resizable(False,False)
    question1_win.title('Premier League 25/26 Stadiums Quiz - Q1')

    q1_label = tk.Label(
        question1_win,
        text=f'What is the Liverpool stadium called?',
        font=('Arial',20)
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = tk.Button(
        question1_win,
        text='Anfield',
        font=('Arial'),
        width=20,
        command=q1_correct
    )
    q1_button_a.grid(
        row=3,
        column=1
    )

    q1_button_b = tk.Button(
        question1_win,
        text='Old Trafford',
        font=('Arial'),
        width=20,
        command=q1_incorrect
    )
    q1_button_b.grid(
        row=3,
        column=2
    )

    q1_button_c = tk.Button(
        question1_win,
        text='Etihad Stadium',
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
        text='Villa Park',
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

root = tk.Tk()
root.geometry('+0+0')
root.resizable(False,False)
root.title('Premier League 25/26 Stadiums Quiz')

root_title = tk.Label(
    root,
    text='Premier League 25/26 Stadiums Quiz',
    font=('Arial',20)
)
root_title.pack(anchor='center')

startquiz_button = tk.Button(
    root,
    text='Start',
    font=('Arial'),
    width=15,
    command=question1
)
startquiz_button.pack(anchor='center')

root.mainloop()