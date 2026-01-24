import tkinter as tk
from tkinter import messagebox, Toplevel
from time import strftime

def question10():
    def q10_correct():
        correct()
        question11()

    def q10_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Mohamed Salah')
        question11()
    
    global question10_win

    question10_win = Toplevel()
    question10_win.geometry('320x90+0+0')
    question10_win.resizable(False,False)
    question10_win.title('European Football 24-25 Quiz - Q10')

    q10_label = tk.Label(
        question10_win,
        text='Who was the Premier League top goalscorer?',
        font=('Arial',20)
    )
    q10_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q10_button_a = tk.Button(
        question10_win,
        text='Mohamned Salah',
        font=('Arial'),
        width=15,
        command=q10_correct
    )
    q10_button_a.grid(
        row=3,
        column=1
    )

    q10_button_b = tk.Button(
        question10_win,
        text='Erling Haaland',
        font=('Arial'),
        width=15,
        command=q10_incorrect
    )
    q10_button_b.grid(
        row=3,
        column=2
    )

    q10_button_c = tk.Button(
        question10_win,
        text='Alexander Isak',
        font=('Arial'),
        width=15,
        command=q10_incorrect
    )
    q10_button_c.grid(
        row=4,
        column=1
    )

    q10_button_d = tk.Button(
        question10_win,
        text='Ollie Watkins',
        font=('Arial'),
        width=15,
        command=q10_incorrect
    )
    q10_button_d.grid(
        row=4,
        column=2
    )

    question9_win.destroy()

def question9():
    def q9_correct():
        correct()
        question10()

    def q9_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Chelsea')
        question10()

    global question9_win

    question9_win = Toplevel()
    question9_win.geometry('320x90+0+0')
    question9_win.resizable(False,False)
    question9_win.title('European Football 24-25 Quiz - Q9')

    q9_label = tk.Label(
        question9_win,
        text='Who won the Conference League?',
        font=('Arial',20)
    )
    q9_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q9_button_a = tk.Button(
        question9_win,
        text='Real Betis',
        font=('Arial'),
        width=15,
        command=q9_incorrect
    )
    q9_button_a.grid(
        row=3,
        column=1
    )

    q9_button_b = tk.Button(
        question9_win,
        text='Chelsea',
        font=('Arial'),
        width=15,
        command=q9_correct
    )
    q9_button_b.grid(
        row=3,
        column=2
    )

    q9_button_c = tk.Button(
        question9_win,
        text='Villarreal',
        font=('Arial'),
        width=15,
        command=q9_incorrect
    )
    q9_button_c.grid(
        row=4,
        column=1
    )

    q9_button_d = tk.Button(
        question9_win,
        text='Atalanta',
        font=('Arial'),
        width=15,
        command=q9_incorrect
    )
    q9_button_d.grid(
        row=4,
        column=2
    )

    question8_win.destroy()

def question8():
    def q8_correct():
        correct()
        question9()

    def q8_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Tottenham?')
        question9()

    global question8_win

    question8_win = Toplevel()
    question8_win.geometry('320x90+0+0')
    question8_win.resizable(False,False)
    question8_win.title('European Football 24-25 Quiz - Q8')

    q8_label = tk.Label(
        question8_win,
        text='Who won the Europa League?',
        font=('Arial',20)
    )
    q8_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q8_button_a = tk.Button(
        question8_win,
        text='Manchester United',
        font=('Arial'),
        width=15,
        command=q8_incorrect
    )
    q8_button_a.grid(
        row=3,
        column=1
    )

    q8_button_b = tk.Button(
        question8_win,
        text='Chelsea',
        font=('Arial'),
        width=15,
        command=q8_incorrect
    )
    q8_button_b.grid(
        row=3,
        column=2
    )

    q8_button_c = tk.Button(
        question8_win,
        text='Aston Villa',
        font=('Arial'),
        width=15,
        command=q8_incorrect
    )
    q8_button_c.grid(
        row=4,
        column=1
    )

    q8_button_d = tk.Button(
        question8_win,
        text='Tottenham',
        font=('Arial'),
        width=15,
        command=q8_correct
    )
    q8_button_d.grid(
        row=4,
        column=2
    )

    question7_win.destroy()

def question7():
    def q7_correct():
        correct()
        question8()

    def q7_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is PSG?')
        question8()

    global question7_win

    question7_win = Toplevel()
    question7_win.geometry('320x90+0+0')
    question7_win.resizable(False,False)
    question7_win.title('European Football 24-25 Quiz - Q7')

    q7_label = tk.Label(
        question7_win,
        text='Who won the Champions League',
        font=('Arial',20)
    )
    q7_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q7_button_a = tk.Button(
        question7_win,
        text='Real Madrid',
        font=('Arial'),
        width=15,
        command=q7_incorrect
    )
    q7_button_a.grid(
        row=3,
        column=1
    )

    q7_button_b = tk.Button(
        question7_win,
        text='Bayern Munich',
        font=('Arial'),
        width=15,
        command=q7_incorrect
    )
    q7_button_b.grid(
        row=3,
        column=2
    )

    q7_button_c = tk.Button(
        question7_win,
        text='Inter Milan',
        font=('Arial'),
        width=15,
        command=q7_incorrect
    )
    q7_button_c.grid(
        row=4,
        column=1
    )
    
    q7_button_d = tk.Button(
        question7_win,
        text='PSG',
        font=('Arial'),
        width=15,
        command=q7_correct
    )
    q7_button_d.grid(
        row=4,
        column=2
    )

    question6_win.destroy()

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