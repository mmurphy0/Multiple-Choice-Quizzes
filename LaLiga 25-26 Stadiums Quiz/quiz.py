import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

from time import strftime

def question3(question2_win):
    def q3_correct():
        correct()
        question4(question3_win)

    def q3_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Estadio de la Cerámica')
        question4(question3_win)

    question3_win = Toplevel()
    question3_win.geometry('+0+0')
    question3_win.resizable(False,False)
    question3_win.title('LaLiga 25-26 Stadiums Quiz - Q3')

    q3_label = tk.Label(
        question3_win,
        text='What is the Villareal Stadium called?',
        font=('Arial',20)
    )
    q3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q3_button_a = tk.Button(
        question3_win,
        text='RCDE Stadium',
        font=('Arial'),
        width=20,
        command=q3_incorrect
    )
    q3_button_a.grid(
        row=3,
        column=1
    )

    q3_button_b = tk.Button(
        question3_win,
        text='Son Moix',
        font=('Arial'),
        width=20,
        command=q3_incorrect
    )
    q3_button_b.grid(
        row=3,
        column=2
    )

    q3_button_c = tk.Button(
        question3_win,
        text='Camp Nou',
        font=('Arial'),
        width=20,
        command=q3_incorrect
    )
    q3_button_c.grid(
        row=4,
        column=1
    )

    q3_button_d = tk.Button(
        question3_win,
        text='Estadio de la Cerámica',
        font=('Arial'),
        width=20,
        command=q3_correct
    )
    q3_button_d.grid(
        row=4,
        column=2
    )

    question2_win.destroy()

def question2(question1_win):
    def q2_correct():
        correct()
        question3(question2_win)

    def q2_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Bernabéu')
        question3(question2_win)

    question2_win = Toplevel()
    question2_win.geometry('+0+0')
    question2_win.resizable(False,False)
    question2_win.title('LaLiga 25-26 Stadiums Quiz - Q2')

    q2_label = tk.Label(
        question2_win,
        text='What is the Real Madrid Stadium called?',
        font=('Arial',20)
    )
    q2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q2_button_a = tk.Button(
        question2_win,
        text='El Sadar Stadium',
        font=('Arial'),
        width=20,
        command=q2_incorrect
    )
    q2_button_a.grid(
        row=3,
        column=1
    )

    q2_button_b = tk.Button(
        question2_win,
        text='Benito Villamarín Stadium',
        font=('Arial'),
        width=20,
        command=q2_incorrect
    )
    q2_button_b.grid(
        row=3,
        column=2
    )

    q2_button_c = tk.Button(
        question2_win,
        text='Bernabéu',
        font=('Arial'),
        width=20,
        command=q2_correct
    )
    q2_button_c.grid(
        row=4,
        column=1
    )

    q2_button_d = tk.Button(
        question2_win,
        text='Montilivi Stadium',
        font=('Arial'),
        width=20,
        command=q2_incorrect
    )
    q2_button_d.grid(
        row=4,
        column=2
    )

    question1_win.destroy()

def question1():
    def q1_correct():
        correct()
        question2(question1_win)

    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Camp Nou')
        question2(question1_win)

    question1_win = Toplevel()
    question1_win.geometry('+0+0')
    question1_win.resizable(False,False)
    question1_win.title('LaLiga 25-26 Stadiums Quiz - Q1')

    q1_label = tk.Label(
        question1_win,
        text='What is the Barcelona Stadium called?',
        font=('Arial',20)
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = tk.Button(
        question1_win,
        text='Camp Nou',
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
        text='Reale Arena',
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
        text='Mestalla Stadium',
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
        text='Coliseum Stadium',
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
root.title('LaLiga 25-26 Stadiums Quiz')

root_title = tk.Label(
    root,
    text='LaLiga 25-26 Stadiums Quiz',
    font=('Arial',20,'bold')
)
root_title.pack()

continue_button = tk.Button(
    root,
    text='Continue',
    font=('Arial'),
    width=20,
    command=question1
)
continue_button.pack()

root.mainloop()