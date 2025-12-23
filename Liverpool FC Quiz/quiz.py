import tkinter as tk
from tkinter import Toplevel, messagebox
import datetime
from datetime import datetime

score = 0

def question2():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is Anfield')

    global question2_win

    question2_win = Toplevel()
    question2_win.geometry('280x90')
    question2_win.minsize('280x90')
    question2_win.maxsize('280x90')
    question2_win.title('Liverpool FC Quiz - Question 2')

    question2_label = tk.Label(
        question2_win,
        text='What is the name of Liverpools home stadium?',
        font=('Arial',20)
    )
    question2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question2_button_a = tk.Button(
        question2_win,
        text='Hill Dickinson',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question2_button_a.grid(
        row=3,
        column=1
    )

    question2_button_b = tk.Button(
        question2_win,
        text='Old Trafford',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question2_button_b.grid(
        row=3,
        column=2
    )

    question2_button_c = tk.Button(
        question2_win,
        text='Wembley',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question2_button_c.grid(
        row=4,
        column=2
    )

    question2_button_d = tk.Button(
        question2_win,
        text='Anfield',
        font=('Arial'),
        width=10,
        command=correct
    )
    question2_button_d.grid(
        row=4,
        column=2
    )

    question1_win.destroy()


def question1():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1
    
    def incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 1892')

    global question1_win

    question1_win = Toplevel()
    question1_win.geometry('345x90')
    question1_win.minsize(345,90)
    question1_win.maxsize(345,90)
    question1_win.title('Liverpool FC Quiz - Question 1')

    question1_label = tk.Label(
        question1_win,
        text='What year was Liverpool FC founded?',
        font=('Arial',20)
    )
    question1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question1_button_a = tk.Button(
        question1_win,
        text='1888',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question1_button_a.grid(
        row=3,
        column=1
    )

    question1_button_b = tk.Button(
        question1_win,
        text='1890',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question1_button_b.grid(
        row=3,
        column=2
    )

    question1_button_c = tk.Button(
        question1_win,
        text='1892',
        font=('Arial'),
        width=15,
        command=correct
    )
    question1_button_c.grid(
        row=4,
        column=1
    )

    question1_button_d = tk.Button(
        question1_win,
        text='1896',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question1_button_d.grid(
        row=4,
        column=2
    )


root = tk.Tk()
root.geometry('200x60')
root.minsize(200,60)
root.maxsize(200,60)
root.title('Liverpool FC Quiz')

quiz_title = tk.Label(
    root,
    text='Liverpool FC Quiz',
    font=('Arial',20,'bold')
)
quiz_title.pack()

startquiz_button = tk.Button(
    root,
    text='Start Quiz',
    font=('Arial'),
    width=20,
    command=question1
)
startquiz_button.pack()

root.mainloop()