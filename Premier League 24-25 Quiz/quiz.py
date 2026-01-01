import tkinter as tk
from tkinter import messagebox, Toplevel
import datetime
from datetime import datetime

score = 0

def question4():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Leicester City')

    global question4_win

    question4_win = Toplevel()
    question4_win.geometry('280x90+0+0')
    question4_win.resizable(False,False)
    question4_win.title('Premier League 24/25 Quiz - Q4')

    question4_label = tk.Label(
        question4_win,
        text='Which club was relegated?',
        font=('Arial',20)
    )
    question4_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question4_button_a = tk.Button(
        question4_win,
        text='Leicester City',
        font=('Arial'),
        width=15,
        command=correct
    )
    question4_button_a.grid(
        row=3,
        column=1
    )

    question4_button_b = tk.Button(
        question4_win,
        text='Aston Villa',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question4_button_b.grid(
        row=3,
        column=2
    )

    question4_button_c = tk.Button(
        question4_win,
        text='West Ham',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question4_button_c.grid(
        row=4,
        column=1
    )

    question4_button_d = tk.Button(
        question4_win,
        text='Wolves',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question4_button_d.grid(
        row=4,
        column=2
    )

    question3_win.destroy()


def question3():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 29')

    global question3_win

    question3_win = Toplevel()
    question3_win.geometry('280x90+0+0')
    question3_win.resizable(False,False)
    question3_win.title('Premier Leaguw 24/25 Quiz - Q3')

    question3_label = tk.Label(
        question1_win,
        text='How many goals did the top scorer score?',
        font=('Arial',20)
    ) 
    question3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question3_button_a = tk.Button(
        question3_win,
        text='25',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question3_button_a.grid(
        row=3,
        column=1
    )

    question3_button_b = tk.Button(
        question3_win,
        text='27',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question3_button_b.grid(
        row=3,
        column=2
    )

    question3_button_c = tk.Button(
        question3_win,
        text='29',
        font=('Arial'),
        width=15,
        command=correct
    )
    question3_button_c.grid(
        row=4,
        column=1
    )

    question3_button_d = tk.Button(
        question3_win,
        text='31',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question3_button_d.grid(
        row=4,
        column=2
    )

    question2_win.destroy()

def question2():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Mohamed Salah')

    global question2_win

    question2_win = Toplevel()
    question2_win.geometry('280x90+0+0')
    question2_win.resizable(False,False)
    question2_win.title('Premier League 24/25 Quiz - Q2')

    question2_label = tk.Label(
        question2_win,
        text='Which player won the Premier League Golden Boot?',
        font=('Arial',20)
    )
    question2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question2_button_a = tk.Button(
        question2_win,
        text='Erling Haaland',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question2_button_a.grid(
        row=3,
        column=1
    )

    question2_button_b = tk.Button(
        question2_win,
        text='Mohamed Salah',
        font=('Arial'),
        width=15,
        command=correct
    )
    question2_button_b.grid(
        row=3,
        column=2
    )

    question2_button_c = tk.Button(
        question2_win,
        text='Alexander Isak',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question2_button_c.grid(
        row=4,
        column=1
    )

    question2_button_d = tk.Button(
        question2_win,
        text='Bukayo Saka',
        font=('Arial'),
        width=15,
        command=incorrect
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
        messagebox.showinfo('Result','Incorrect, The answer is Liverpool')

    global question1_win

    question1_win = Toplevel()
    question1_win.geometry('323x90+0+0')
    question1_win.resizable(False,False)
    question1_win.title('Premier League 24/25 Quiz - Q1')

    question1_label = tk.Label(
        question1_win,
        text='Who won the Premier League Title?',
        font=('Arial',20)
    )
    question1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )
    
    question1_button_a = tk.Button(
        question1_win,
        text='Chelsea',
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
        text='Arsenal',
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
        text='Liverpool',
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
        text='Manchester City',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question1_button_d.grid(
        row=4,
        column=2
    )

root = tk.Tk()
root.geometry('257x60+0+0')
root.resizable(False,False)
root.title('Premier League 24/25 Quiz')

quiz_title = tk.Label(
    root,
    text='Premier League 24/25 Quiz',
    font=('Arial',20,'bold')
)
quiz_title.pack()

startquiz_button = tk.Button(
    root,
    text='Start Quiz',
    font=('Arial'),
    width=40,
    command=question1
)
startquiz_button.pack()

root.mainloop()