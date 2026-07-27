import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel
from tkinter import ttk

from time import strftime

import platform 

def question3(question2_win):
    def q3_correct():
        correct()
        question4(question3_win)

    def q3_incorrect():
        messagebox.showinfo('Result','The answer is the Decathlon Arena')
        question4(question3_win)

    question3_win = Toplevel()
    question3_win.geometry('+0+0')
    question3_win.resizable(False,False)
    question3_win.title('Ligue 1 25-26 Stadiums Quiz')

    q3_label = ttk.Label(
        question3_win,
        text='What is the LOSC Stadium called?',
        style='Title.TLabel'
    )
    q3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q3_button_a = ttk.Button(
        question3_win,
        text='Roazhon Park',
        style='Button.TButton',
        width=20,
        command=q3_incorrect
    )
    q3_button_a.grid(
        row=3,
        column=1,
        padx=10
    )

    q3_button_b = ttk.Button(
        question3_win,
        text='Stade Francis-Le Blé',
        style='Button.TButton',
        width=20,
        command=q3_incorrect
    )
    q3_button_b.grid(
        row=4,
        column=1,
        padx=10
    )

    q3_button_c = ttk.Button(
        question3_win,
        text='Decathlon Arena',
        style='Button.TButton',
        width=20,
        command=q3_correct
    )
    q3_button_c.grid(
        row=3,
        column=2,
        padx=10
    )

    q3_button_d = ttk.Button(
        question3_win,
        text='Stade Jean-Bouin',
        style='Button.TButton',
        width=20
    )
    q3_button_d.grid(
        row=4,
        column=2,
        padx=10
    )

    question2_win.destroy()

def question2(question1_win):
    def q2_correct():
        correct()
        question3(question2_win)

    def q2_incorrect():
        messagebox.showinfo('Result','The answer is the Stade Bollaert-Delelis')
        question3(question2_win)

    question2_win = Toplevel()
    question2_win.geometry('+0+0')
    question2_win.resizable(False,False)
    question2_win.title('Ligue 1 25-26 Stadiums Quiz')

    q2_label = ttk.Label(
        question2_win,
        style='Title.TLabel',
        text='What is the Lens Stadium called?'
    )
    q2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q2_button_a = ttk.Button(
        question2_win,
        text='Stade Bollaert-Delelis',
        style='Button.TButton',
        width=20,
        command=q2_correct
    )
    q2_button_a.grid(
        row=3,
        column=1,
        padx=10
    )

    q2_button_b = ttk.Button(
        question2_win,
        text='Decathlon Arena',
        style='Button.TButton',
        width=20,
        command=q2_incorrect
    )
    q2_button_b.grid(
        row=4,
        column=1,
        padx=10
    )

    q2_button_c = ttk.Button(
        question2_win,
        text='Stade de la Meinau',
        style='Button.TButton',
        width=20,
        command=q2_incorrect
    )
    q2_button_c.grid(
        row=3,
        column=2,
        padx=10
    )

    q2_button_d = ttk.Button(
        question2_win,
        text='Stade Louis II',
        style='Button.TButton',
        width=20,
        command=q2_incorrect
    )
    q2_button_d.grid(
        row=4,
        column=2,
        padx=10
    )

    question1_win.destroy()

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

    q1_label = ttk.Label(
        question1_win,
        style='Title.TLabel',
        text='What is the PSG Stadium called?',
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = ttk.Button(
        question1_win,
        style='Button.TButton',
        text='Stade Bollaert-Delelis',
        width=20,
        command=q1_incorrect
    )
    q1_button_a.grid(
        row=3,
        column=1,
        padx=10
    )

    q1_button_b = ttk.Button(
        question1_win,
        style='Button.TButton',
        text='Parc des Princes',
        width=20,
        command=q1_correct
    )
    q1_button_b.grid(
        row=3,
        column=2,
        padx=10
    )

    q1_button_c = ttk.Button(
        question1_win,
        style='Button.TButton',
        text='Groupama Stadium',
        width=20,
        command=q1_incorrect
    )
    q1_button_c.grid(
        row=4,
        column=1,
        padx=10
    )

    q1_button_d = ttk.Button(
        question1_win,
        style='Button.TButton',
        text='Orange Vélodrome',
        width=20,
        command=q1_incorrect
    )
    q1_button_d.grid(
        row=4,
        column=2,
        padx=10
    )

def correct():
    global score
    score += 1
    messagebox.showinfo('Result','Correct!')
    return

def initialise_styles():
    button_style = ttk.Style()
    title_style = ttk.Style()

    current_os = platform.system()

    if current_os == 'Windows':
        button_style.theme_use('vista')
        button_style.configure(
            'Button.TButton',
            font=('Arial',10),
            bg='White',
            fg='Black'
        )

        title_style.configure(
            'Title.TLabel',
            font=('Arial',15,'bold')
        )

    elif current_os == 'Darwin':
        button_style.configure(
            'Button.TButton',
            font=('Arial')
        )

        title_style.configure(
            'Title.TLabel',
            font=('Arial',20,'bold')
        )

score = 0

root = tk.Tk()
root.geometry('+0+0')
root.resizable(False,False)
root.title('Ligue 1 25-26 Stadiums Quiz')

initialise_styles()

root_title = ttk.Label(
    root,
    style='Title.TLabel',
    text='Ligue 1 25-26 Stadiums Quiz',
)
root_title.pack()

start_button = ttk.Button(
    root,
    style='Button.TButton',
    text='Start',
    width=20,
    command=question1
)
start_button.pack()

root.mainloop()