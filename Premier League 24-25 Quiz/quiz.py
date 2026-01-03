import tkinter as tk
from tkinter import messagebox, Toplevel
import datetime
from datetime import datetime

score = 0

def question9():
    def q9_correct():
        correct()

    def q9_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 20')

    global question9_win

    question9_win = Toplevel()
    question9_win.geometry('280x90+0+0')
    question9_win.resizable(False,False)
    question9_win.title('Premier League 24/25 Quiz - Q9')

    question9_label = tk.Label(
        question9_win,
        text='How many teams are in the Premier League?',
        font=('Arial',20)
    )
    question9_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question9_button_a = tk.Button(
        question9_win,
        text='22',
        font=('Arial'),
        width=15,
        command=q9_incorrect
    )
    question9_button_a.grid(
        row=3,
        column=1
    )

    question9_button_b = tk.Button(
        question9_win,
        text='20',
        font=('Arial'),
        width=15,
        command=q9_correct
    )
    question9_button_b.grid(
        row=3,
        column=2
    )

    question9_button_c = tk.Button(
        question9_win,
        text='18',
        font=('Arial'),
        width=15,
        command=q9_incorrect
    )
    question9_button_c.grid(
        row=4,
        column=1
    )

    question9_button_d = tk.Button(
        question9_win,
        text='24',
        font=('Arial'),
        width=15,
        command=q9_incorrect
    )
    question9_button_d.grid(
        row=4,
        column=2
    )



def question8():
    def q8_correct():
        correct()

    def q8_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Crystal Palace')

    global question8_win

    question8_win = Toplevel()
    question8_win.geometry('280x90+0+0')
    question8_win.resizable(False,False)
    question8_win.title('Premier League 24/25 Quiz - Q8')

    question8_label = tk.Label(
        question8_win,
        text='Which club qualified for UEFA Conference League through position in the league?',
        font=('Arial',20)
    )
    question8_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question8_button_a = tk.Button(
        question8_win,
        text='Chelsea',
        font=('Arial'),
        width=15,
        command=q8_incorrect
    )
    question8_button_a.grid(
        row=3,
        column=1
    )
    
    question8_button_b = tk.Button(
        question8_win,
        text='Brighton',
        font=('Arial'),
        width=15,
        command=q8_incorrect
    )
    question8_button_b.grid(
        row=3,
        column=2
    )

    question8_button_c = tk.Button(
        question8_win,
        text='Crystal Palace',
        font=('Arial'),
        width=15,
        command=q8_correct
    )
    question8_button_c.grid(
        row=4,
        column=1
    )

    question8_button_d = tk.Button(
        question8_win,
        text='Everton',
        font=('Arial'),
        width=15,
        command=q8_incorrect
    )
    question8_button_d.grid(
        row=4,
        column=2
    )

    question7_win.destroy()


def question7():
    def q7_correct():
        correct()

    def q7_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is David Raya & Matz Sels')

    global question7_win

    question7_win = Toplevel()
    question7_win.geometry('280x90')
    question7_win.resizable(False,False)
    question7_win.title('Premier League 24/25 Quiz - Q7')

    question7_label = tk.Label(
        question7_win,
        text='WHich goalkeepers shared the Premier League Golden Glove Award?',
        font=('Arial',20)
    )
    question7_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question7_button_a = tk.Button(
        question7_win,
        text='David Raya & Matz Sels',
        font=('Arial'),
        width=20,
        command=q7_correct
    )
    question7_button_a.grid(
        row=3,
        column=1
    )

    question7_button_b = tk.Button(
        question7_win,
        text='Alisson & Ederson',
        font=('Arial'),
        width=20,
        command=q7_incorrect
    )
    question7_button_b.grid(
        row=3,
        column=2
    )

    question6_win.destroy()


def question6():
    def q6_correct():
        correct()

    def q6_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 1115')

    global question6_win

    question6_win = Toplevel()
    question6_win.geometry('280x90+0+0')
    question6_win.resizable(False,False)
    question6_win.title('Premier League 24/25 Quiz - Q6')

    question6_label = tk.Label(
        question6_win,
        text='How many goals were scored in the Premier League?',
        font=('Arial',20)
    )
    question6_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question6_button_a = tk.Button(
        question6_win,
        text='850',
        font=('Arial'),
        width=15,
        command=q6_incorrect
    )
    question6_button_a.grid(
        row=3,
        column=1
    )

    question6_button_b = tk.Button(
        question6_win,
        text='980',
        font=('Arial'),
        width=15,
        command=q6_incorrect
    )
    question6_button_b.grid(
        row=3,
        column=2
    )

    question6_button_c = tk.Button(
        question6_win,
        text='1200',
        font=('Arial'),
        width=15,
        command=q6_incorrect
    )
    question6_button_c.grid(
        row=4,
        column=1
    )

    question6_button_d = tk.Button(
        question6_win,
        text='1115',
        font=('Arial'),
        width=15,
        command=q6_correct
    )
    question6_button_d.grid(
        row=4,
        column=2
    )

    question5_win.destroy()


def question5():
    def q5_correct():
        correct()

    def q5_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 19th ')

    global question5_win

    question5_win = Toplevel()
    question5_win.geometry('280x90+0+0')
    question5_win.resizable(False,False)
    question5_win.title('Premier League 24/25 Quiz - Q5')

    question5_label = tk.Label(
        question5_win,
        text='Where did Ipswich Town Finish?',
        font=('Arial',20)
    )
    question5_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question5_button_a = tk.Button(
        question5_win,
        text='19th',
        font=('Arial'),
        width=15,
        command=q5_correct
    )
    question5_button_a.grid(
        row=3,
        column=1
    )

    question5_button_b = tk.Button(
        question5_win,
        text='1st',
        font=('Arial'),
        width=15,
        command=q5_incorrect
    )
    question5_button_b.grid(
        row=3,
        column=2
    )

    question5_button_c = tk.Button(
        question5_win,
        text='6th',
        font=('Arial'),
        width=15,
        command=q5_incorrect
    )
    question5_button_c.grid(
        row=4,
        column=1
    )

    question5_button_d = tk.Button(
        question5_win,
        text='10th',
        font=('Arial'),
        width=15,
        command=q5_incorrect
    )
    question5_button_d.grid(
        row=4,
        column=2
    )

    question4_win.destroy()


def question4():
    def q4_correct():
        correct()

    def q4_incorrect():
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
        command=q4_correct
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
        command=q4_incorrect
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
        command=q4_incorrect
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
        command=q4_incorrect
    )
    question4_button_d.grid(
        row=4,
        column=2
    )

    question3_win.destroy()


def question3():
    def q3_correct():
        correct()

    def q3_incorrect():
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
        command=q3_incorrect
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
        command=q3_incorrect
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
        command=q3_correct
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
        command=q3_incorrect
    )
    question3_button_d.grid(
        row=4,
        column=2
    )

    question2_win.destroy()

def question2():
    def q2_correct():
        correct()

    def q2_incorrect():
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
        command=q2_incorrect
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
        command=q2_correct
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
        command=q2_incorrect
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
        command=q2_incorrect
    )
    question2_button_d.grid(
        row=4,
        column=2
    )

    question1_win.destroy()


def question1():
    def q1_correct():
        correct()

    def q1_incorrect():
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
        command=q1_incorrect
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
        command=q1_incorrect
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
        command=q1_correct
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
        command=q1_incorrect
    )
    question1_button_d.grid(
        row=4,
        column=2
    )

def correct():
    global score
    messagebox.showinfo('Result','Correct!')
    score += 1
    return 

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