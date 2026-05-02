import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

from time import strftime

def question3(question2_win):
    def q3_correct():
        correct()
        question4(question3_win)
    
    def q3_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Red Bull Arena')
        question4(question3_win)

    question3_win = Toplevel()
    question3_win.geometry('+0+0')
    question3_win.resizable(False,False)
    question3_win.title('Bundesliga 25-26 Stadiums Quiz - Q3')

    q3_label = tk.Label(
        question3_win,
        text='What is the RB Leipzig stadium called?',
        font=('Arial',20)
    )
    q3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q3_button_a = tk.Button(
        question3_win,
        text='BayArena',
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
        text='WWK Arena',
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
        text='Red Bull Arena',
        font=('Arial'),
        width=20,
        command=q3_correct
    )
    q3_button_c.grid(
        row=4,
        column=1
    )

    q3_button_d = tk.Button(
        question3_win,
        text='RheinEnergieStadion',
        font=('Arial'),
        width=20,
        command=q3_incorrect
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
        messagebox.showinfo('Result','Incorrect, The answer is Signal Iduna Park')
        question3(question2_win)

    question2_win = Toplevel()
    question2_win.geometry('+0+0')
    question2_win.resizable(False,False)
    question2_win.title('Bundesliga 25-26 Stadiums Quiz - Q2')

    q2_label = tk.Label(
        question2_win,
        text='What is the Dortmund stadium called?',
        font=('Arial',20)
    )
    q2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q2_button_a = tk.Button(
        question2_win,
        text='Allianz Arena',
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
        text='MHP Arena',
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
        text='Volkwagen Arena',
        font=('Arial'),
        width=20,
        command=q2_incorrect
    )
    q2_button_c.grid(
        row=4,
        column=1
    )

    q2_button_d = tk.Button(
        question2_win,
        text='Signal Iduna Park',
        font=("Arial"),
        width=20,
        command=q2_correct
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
        messagebox.showinfo('Result','Incorrect, The answer is the Allianz Arena')
        question2(question1_win)

    question1_win = Toplevel()
    question1_win.geometry('+0+0')
    question1_win.resizable(False,False)
    question1_win.title('Bundesliga 25-26 Stadiums Quiz - Q1')

    q1_label = tk.Label(
        question1_win,
        text='What is the Bayern stadium called?',
        font=('Arial',20)
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )
    
    q1_button_a = tk.Button(
        question1_win,
        text='Allianz Arena',
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
        text='Signal Iduna Park',
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
        text='Red Bull Arena',
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
        text='BayArena',
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

root_win = tk.Tk()
root_win.geometry('+0+0')
root_win.resizable(False,False)
root_win.title('Bundesliga 25-26 Stadiums Quiz')

root_label = tk.Label(
    root_win,
    text='Bundesliga 25-26 Stadiums Quiz',
    font=('Arial',20,'bold')
)
root_label.pack()

startquiz_button = tk.Button(
    root_win,
    text='Start',
    font=('Arial')
)
startquiz_button.pack()

root_win.mainloop()