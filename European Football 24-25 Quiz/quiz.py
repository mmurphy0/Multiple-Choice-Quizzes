import tkinter as tk
from tkinter import messagebox, Toplevel
from time import strftime

def question6():
    def q6_correct():
        correct()
        question7()

    def q6_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is PSG')
        question7()

    global question6_win

    question6_win = Toplevel()
    question6_win.geometry('320x90+0+0')
    question6_win.resizable(False,False)
    question6_win.title('European Football 24-25 Quiz - Q6')

    q6_label = tk.Label(
        question6_win,
        text='Who won Ligue 1?',
        font=('Arial',20)
    )
    q6_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q6_button_a = tk.Button(
        question6_win,
        text='Marseille',
        font=('Arial'),
        width=15,
        command=q6_incorrect
    )
    q6_button_a.grid(
        row=3,
        column=1
    )

    q6_button_b = tk.Button(
        question6_win,
        text='PSG',
        font=('Arial'),
        width=15,
        command=q6_correct
    )
    q6_button_b.grid(
        row=3,
        column=2
    )

    q6_button_c = tk.Button(
        question6_win,
        text='Monaco',
        font=('Arial'),
        width=15,
        command=q6_incorrect
    )
    q6_button_c.grid(
        row=4,
        column=1
    )

    q6_button_d = tk.Button(
        question6_win,
        text='Nice',
        font=('Arial'),
        width=15,
        command=q6_incorrect
    )
    q6_button_d.grid(
        row=4,
        column=2
    )

    question5_win.destroy()

def question5():
    def q5_correct():
        correct()
        question6()

    def q5_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Bayern Munich')
        question6()

    global question5_win

    question5_win = Toplevel()
    question5_win.geometry('320x90+0+0')
    question5_win.resizable(False,False)
    question5_win.title('European Football 24-25 Quiz - Q5')

    q5_label = tk.Label(
        question5_win,
        text='Who won the Bundesliga?',
        font=('Arial',20)
    )
    q5_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q5_button_a = tk.Button(
        question5_win,
        text='Bayer Leverkusen',
        font=('Arial'),
        width=15,
        command=q5_incorrect
    )
    q5_button_a.grid(
        row=3,
        column=1
    )

    q5_button_b = tk.Button(
        question5_win,
        text='Borussia Dortmund',
        font=('Arial'),
        width=15,
        command=q5_incorrect
    )
    q5_button_b.grid(
        row=3,
        column=2
    )

    q5_button_c = tk.Button(
        question5_win,
        text='Bayern Munich',
        font=('Arial'),
        width=15,
        command=q5_correct
    )
    q5_button_c.grid(
        row=4,
        column=1
    )

    q5_button_d = tk.Button(
        question5_win,
        text='RB Leipzig',
        font=('Arial'),
        width=15,
        command=q5_incorrect
    )
    q5_button_d.grid(
        row=4,
        column=2
    )

    question4_win.destroy()

def question4():
    def q4_correct():
        correct()
        question5()

    def q4_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Napoli')
        question5()

    global question4_win

    question4_win = Toplevel()
    question4_win.geometry('320x90+0+0')
    question4_win.resizable(False,False)
    question4_win.title('European Football 24-25 Quiz')

    q4_label = tk.Label(
        question4_win,
        text='Who won the Serie A?',
        font=('Arial',20)
    )
    q4_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q4_button_a = tk.Button(
        question4_win,
        text='Inter Milan',
        font=('Arial'),
        width=15,
        command=q4_incorrect
    )
    q4_button_a.grid(
        row=3,
        column=1
    )

    q4_button_b = tk.Button(
        question4_win,
        text='Napoli',
        font=('Arial'),
        width=15,
        command=q4_correct
    )
    q4_button_b.grid(
        row=3,
        column=2
    )
    
    q4_button_c = tk.Button(
        question4_win,
        text='Juventus',
        font=('Arial'),
        width=15,
        command=q4_incorrect
    )
    q4_button_c.grid(
        row=4,
        column=1
    )

    q4_button_d = tk.Button(
        question4_win,
        text='AC Milan',
        font=('Arial'),
        width=15,
        command=q4_incorrect
    )
    q4_button_d.grid(
        row=4,
        column=2
    )

    question3_win.destroy()

def question3():
    def q3_correct():
        correct()
        question4()

    def q3_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Barcelona')
        question4()

    global question3_win

    question3_win = Toplevel()
    question3_win.geometry('320x90+0+0')
    question3_win.resizable(False,False)
    question3_win.title('European Football 24-25 Quiz')

    q3_label = tk.Label(
        question3_win,
        text='Who won the LaLiga?',
        font=('Arial',20)
    )
    q3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q3_button_a = tk.Button(
        question3_win,
        text='Real Madrid',
        font=('Arial'),
        width=15,
        command=q3_incorrect
    )
    q3_button_a.grid(
        row=3,
        column=1
    )

    q3_button_b = tk.Button(
        question3_win,
        text='Atlético Madrid',
        font=('Arial'),
        width=15,
        command=q3_incorrect
    )
    q3_button_b.grid(
        row=3,
        column=2
    )

    q3_button_c = tk.Button(
        question3_win,
        text='Barcelona',
        font=('Arial'),
        width=15,
        command=q3_correct
    )
    q3_button_c.grid(
        row=4,
        column=1
    )
    
    q3_button_d = tk.Button(
        question3_win,
        text='Sevilla',
        font=('Arial'),
        width=15,
        command=q3_incorrect
    )
    q3_button_d.grid(
        row=4,
        column=2
    )

    question2_win.destroy()

def question2():
    def q2_correct():
        correct()
        question3()

    def q2_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Arsenal')
        question3()
    
    global question2_win

    question2_win = Toplevel()
    question2_win.geometry('320x90+0+0')
    question2_win.resizable(False,False)
    question2_win.title('European Football 24-25 Quiz')

    q2_label = tk.Label(
        question2_win,
        text='Who was 2nd in the Premier League?',
        font=('Arial',20)
    )
    q2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q2_button_a = tk.Button(
        question2_win,
        text='Manchester United',
        font=('Arial'),
        width=15,
        command=q2_incorrect
    )
    q2_button_a.grid(
        row=3,
        column=1,
    )

    q2_button_b = tk.Button(
        question2_win,
        text='Arsenal',
        font=('Arial'),
        width=15,
        command=q2_correct
    )
    q2_button_b.grid(
        row=3,
        column=2
    )
    
    q2_button_c = tk.Button(
        question2_win,
        text='Newcastle United',
        font=('Arial'),
        width=15,
        command=q2_incorrect
    )
    q2_button_c.grid(
        row=4,
        column=1
    )

    q2_button_d = tk.Button(
        question2_win,
        text='Chelsea',
        font=('Arial'),
        width=15,
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
        question2()

    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Liverpool')
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