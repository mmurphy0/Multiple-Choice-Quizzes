import tkinter as tk
from tkinter import messagebox, Toplevel
from time import strftime
score = 0

def result():
    def reset():
        global score
        score = 0
        result_win.destroy()

    def save():
        time = strftime('%H:%M:%S %D')
        with open('Premier League 24-25 Quiz/scorebook.txt','a') as file:
            file.write(time + '\n' + (f'Score: {score} /20') + '\n' + '----------' + '\n')
            messagebox.showinfo('Confirmation','Score successfully saved')
            reset()

    global result_win

    result_win = Toplevel()
    result_win.geometry('117x90+0+0')
    result_win.resizable(False,False)
    result_win.title('Premier League 24-25 Quiz - Results')

    result_title = tk.Label(
        result_win,
        text='Results',
        font=('Arial',20,'bold')
    )
    result_title.pack()

    result_label = tk.Label(
        result_win,
        text=(f'Score: {score}/20'),
        font=('Arial',20)
    )
    result_label.pack()

    continue_button = tk.Button(
        result_win,
        text='Continue',
        font=('Arial'),
        width=20,
        command=save
    )
    continue_button.pack()

    question20_win.destroy()


def question20():
    def q20_correct():
        correct()
        result()

    def q20_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is All of the Above')
        result()

    global question20_win

    question20_win = Toplevel()
    question20_win.geometry('393x90+0+0')
    question20_win.resizable(False,False)
    question20_win.title('Premier League 24-25 Quiz - Q20')

    question20_label = tk.Label(
        question20_win,
        text='Mohamed Salah won the Golden Boot and?',
        font=('Arial',20)
    )
    question20_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question20_button_a = tk.Button(
        question20_win,
        text='Playmaker',
        font=('Arial'),
        width=15,
        command=q20_incorrect
    )
    question20_button_a.grid(
        row=3,
        column=1
    )

    question20_button_b = tk.Button(
        question20_win,
        text='Golden Boot',
        font=('Arial'),
        width=15,
        command=q20_incorrect
    )
    question20_button_b.grid(
        row=3,
        column=2
    )

    question20_button_c = tk.Button(
        question20_win,
        text='Player of the Season',
        font=('Arial'),
        width=15,
        command=q20_incorrect
    )
    question20_button_c.grid(
        row=4,
        column=1
    )

    question20_button_d = tk.Button(
        question20_win,
        text='All of the Above',
        font=('Arial'),
        width=15,
        command=q20_correct
    )
    question20_button_d.grid(
        row=4,
        column=2
    )

    question19_win.destroy()


def question19():
    def q19_correct():
        correct()
        question20()

    def q19_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Mohamed Salah')
        question20()

    global question19_win

    question19_win = Toplevel()
    question19_win.geometry('417x90+0+0')
    question19_win.resizable(False,False)
    question19_win.title('Premier League 24-25 Quiz - Q19')

    question19_label = tk.Label(
        question19_win,
        text='Which player scored 29 goals & led in assists?',
        font=('Arial',20)
    )
    question19_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question19_button_a = tk.Button(
        question19_win,
        text='Mohamed Salah',
        font=('Arial'),
        width=15,
        command=q19_correct
    )
    question19_button_a.grid(
        row=3,
        column=1
    )

    question19_button_b = tk.Button(
        question19_win,
        text='Alexander Isak',
        font=('Arial'),
        width=15,
        command=q19_incorrect
    )
    question19_button_b.grid(
        row=3,
        column=2
    )

    question19_button_c = tk.Button(
        question19_win,
        text='Son Heung-min',
        font=('Arial'),
        width=15,
        command=q19_incorrect
    )
    question19_button_c.grid(
        row=4,
        column=1
    )

    question19_button_d = tk.Button(
        question19_win,
        text='Erling Haaland',
        font=('Arial'),
        width=15,
        command=q19_incorrect
    )
    question19_button_d.grid(
        row=4,
        column=2
    )

    question18_win.destroy()


def question18():
    def q18_correct():
        correct()
        question19()

    def q18_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 3')
        question19()

    global question18_win

    question18_win = Toplevel()
    question18_win.geometry('312x90+0+0')
    question18_win.resizable(False,False)
    question18_win.title('Premier League 24-25 Quiz - Q18')

    question18_label = tk.Label(
        question18_win,
        text='How many teams get relegated?',
        font=('Arial',20)
    )
    question18_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question18_button_a = tk.Button(
        question18_win,
        text='3',
        font=('Arial'),
        width=15,
        command=q18_correct
    )
    question18_button_a.grid(
        row=3,
        column=1
    )

    question18_button_b = tk.Button(
        question18_win,
        text='2',
        font=('Arial'),
        width=15,
        command=q18_incorrect
    )
    question18_button_b.grid(
        row=3,
        column=2,
    )

    question18_button_c = tk.Button(
        question18_win,
        text='1',
        font=('Arial'),
        width=15,
        command=q18_incorrect
    )
    question18_button_c.grid(
        row=4,
        column=1
    )

    question18_button_d = tk.Button(
        question18_win,
        text='4',
        font=('Arial'),
        width=15,
        command=q18_incorrect
    )
    question18_button_d.grid(
        row=4,
        column=2
    )

    question17_win.destroy()


def question17():
    def q17_correct():
        correct()
        question18()

    def q17_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Brighton & Hove Albion')
        question18()

    global question17_win
    
    question17_win = Toplevel()
    question17_win.geometry('312x90+0+0')
    question17_win.resizable(False,False)
    question17_win.title('Premier League 24-25 Quiz - Q17')

    question17_label = tk.Label(
        question17_win,
        text='Which club was not relegated?',
        font=('Arial',20)
    )
    question17_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question17_button_a = tk.Button(
        question17_win,
        text='Ipswich Town',
        font=('Arial'),
        width=15,
        command=q17_incorrect
    )
    question17_button_a.grid(
        row=3,
        column=1
    )

    question17_button_b = tk.Button(
        question17_win,
        text='Leicester City',
        font=('Arial'),
        width=15,
        command=q17_incorrect
    )
    question17_button_b.grid(
        row=3,
        column=2
    )

    question17_button_c = tk.Button(
        question17_win,
        text='Brighton & Hove Albion',
        font=('Arial'),
        width=15,
        command=q17_correct
    )
    question17_button_c.grid(
        row=4,
        column=1
    )

    question17_button_d = tk.Button(
        question17_win,
        text='Southampton',
        font=('Arial'),
        width=15,
        command=q17_incorrect
    )
    question17_button_d.grid(
        row=4,
        column=2
    )

    question16_win.destroy()


def question16():
    def q16_correct():
        correct()
        question17()

    def q16_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Arsenal')
        question17()

    global question16_win

    question16_win = Toplevel()
    question16_win.geometry('347x90+0+0')
    question16_win.resizable(False,False)
    question16_win.title('Premier League 24-25 Quiz - Q16')

    question16_label = tk.Label(
        question16_win,
        text='Which club conceded the least goals?',
        font=('Arial',20)
    )
    question16_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question16_button_a = tk.Button(
        question16_win,
        text='Arsenal',
        font=('Arial'),
        width=15,
        command=q16_correct
    )
    question16_button_a.grid(
        row=3,
        column=1
    )

    question16_button_b = tk.Button(
        question16_win,
        text='Chelsea',
        font=('Arial'),
        width=15,
        command=q16_incorrect
    )
    question16_button_b.grid(
        row=3,
        column=2
    )

    question16_button_c = tk.Button(
        question16_win,
        text='Liverpool',
        font=('Arial'),
        width=15,
        command=q16_incorrect
    )
    question16_button_c.grid(
        row=4,
        column=1
    )

    question16_button_d = tk.Button(
        question16_win,
        text='Manchester United',
        font=('Arial'),
        width=15,
        command=q16_incorrect
    )
    question16_button_d.grid(
        row=4,
        column=2
    )

    question15_win.destroy()


def question15():
    def q15_correct():
        correct()
        question16()

    def q15_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Mohamed Salah')
        question16()

    global question15_win

    question15_win = Toplevel()
    question15_win.geometry('320x90+0+0')
    question15_win.resizable(False,False)
    question15_win.title('Premier League 24-25 Quiz - Q15')

    question15_label = tk.Label(
        question15_win,
        text='Which player had the most assists?',
        font=('Arial',20)
    )
    question15_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question15_button_a = tk.Button(
        question15_win,
        text='Mohamed Salah',
        font=('Arial'),
        width=15,
        command=q15_correct
    )
    question15_button_a.grid(
        row=3,
        column=1
    )

    question15_button_b = tk.Button(
        question15_win,
        text='Kevin De Bruyne',
        font=('Arial'),
        width=15,
        command=q15_incorrect
    )
    question15_button_b.grid(
        row=3,
        column=2
    )

    question15_button_c = tk.Button(
        question15_win,
        text='Jacob Murphy',
        font=('Arial'),
        width=15,
        command=q15_incorrect
    )
    question15_button_c.grid(
        row=4,
        column=1
    )

    question15_button_d = tk.Button(
        question15_win,
        text='Bukayo Saka',
        font=('Arial'),
        width=15,
        command=q15_incorrect
    )
    question15_button_d.grid(
        row=4,
        column=2
    )

    question14_win.destroy()


def question14():
    def q14_correct():
        correct()
        question15()

    def q14_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is all of the above')
        question15()

    global question14_win

    question14_win = Toplevel()
    question14_win.geometry('435x90+0+0')
    question14_win.resizable(False,False)
    question14_win.title('Premier League 24-25 Quiz - Q14')

    question14_label = tk.Label(
        question14_win,
        text='Which club qualified for the Champions League?',
        font=('Arial',20)
    )
    question14_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question14_button_a = tk.Button(
        question14_win,
        text='Liverpool',
        font=('Arial'),
        width=15,
        command=q14_incorrect
    )
    question14_button_a.grid(
        row=3,
        column=1,
    )

    question14_button_b = tk.Button(
        question14_win,
        text='Arsenal',
        font=('Arial'),
        width=15,
        command=q14_incorrect
    )
    question14_button_b.grid(
        row=3,
        column=2
    )

    question14_button_c = tk.Button(
        question14_win,
        text='Manchester City',
        font=('Arial'),
        width=15,
        command=q14_incorrect
    )
    question14_button_c.grid(
        row=4,
        column=1
    )

    question14_button_d = tk.Button(
        question14_win,
        text='All of the above',
        font=('Arial'),
        width=15,
        command=q14_correct
    )
    question14_button_d.grid(
        row=4,
        column=2
    )

    question13_win.destroy()


def question13():
    def q13_correct():
        correct()
        question14()

    def q13_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Liverpool')
        question14()

    global question13_win

    question13_win = Toplevel()
    question13_win.geometry('387x90+0+0')
    question13_win.resizable(False,False)
    question13_win.title('Premier League 24-25 Quiz - Q13')

    question13_label = tk.Label(
        question13_win,
        text='Which team had the longest unbeaten run?',
        font=('Arial',20)
    )
    question13_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question13_button_a = tk.Button(
        question13_win,
        text='Liverpool',
        font=('Arial'),
        width=15,
        command=q13_correct
    )
    question13_button_a.grid(
        row=3,
        column=1
    )

    question13_button_b = tk.Button(
        question13_win,
        text='Arsenal',
        font=('Arial'),
        width=15,
        command=q13_incorrect
    )
    question13_button_b.grid(
        row=3,
        column=2
    )

    question13_button_c = tk.Button(
        question13_win,
        text='Newcastle United',
        font=('Arial'),
        width=15,
        command=q13_incorrect
    )
    question13_button_c.grid(
        row=4,
        column=1
    )

    question13_button_d = tk.Button(
        question13_win,
        text='Manchester City',
        font=('Arial'),
        width=15,
        command=q13_incorrect
    )
    question13_button_d.grid(
        row=4,
        column=2
    )

    question12_win.destroy()


def question12():
    def q12_correct():
        correct()
        question13()

    def q12_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Arne Slot')
        question13()

    global question12_win

    question12_win = Toplevel()
    question12_win.geometry('380x90+0+0')
    question12_win.resizable(False,False)
    question12_win.title('Premier League 24/25 Quiz - Q12')

    question12_label = tk.Label(
        question12_win,
        text='Which Manager won the Premier League?',
        font=('Arial',20)
    )
    question12_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question12_button_a = tk.Button(
        question12_win,
        text='Pep Guardiola',
        font=('Arial'),
        width=15,
        command=q12_incorrect
    )
    question12_button_a.grid(
        row=3,
        column=1
    )

    question12_button_b = tk.Button(
        question12_win,
        text='Mikel Arteta',
        font=('Arial'),
        width=15,
        command=q12_incorrect
    )
    question12_button_b.grid(
        row=3,
        column=2
    )

    question12_button_c = tk.Button(
        question12_win,
        text='Arne Slot',
        font=('Arial'),
        width=15,
        command=q12_correct
    )
    question12_button_c.grid(
        row=4,
        column=1
    )

    question12_button_d = tk.Button(
        question12_win,
        text='Unai Emery',
        font=('Arial'),
        width=15,
        command=q12_incorrect
    )
    question12_button_d.grid(
        row=4,
        column=2
    )

    question11_win.destroy()


def question11():
    def q11_correct():
        correct()
        question12()

    def q11_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Arsenal ')
        question12()

    global question11_win

    question11_win = Toplevel()
    question11_win.geometry('312x90+0+0')
    question11_win.resizable(False,False)
    question11_win.title('Premier League 24/25 Quiz - Q11')

    question11_label = tk.Label(
        question11_win,
        text='Which club finished 2nd?',
        font=('Arial',20)
    )
    question11_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question11_button_a = tk.Button(
        question11_win,
        text='Manchester City',
        font=('Arial'),
        width=15,
        command=q11_incorrect
    )
    question11_button_a.grid(
        row=3,
        column=1
    )

    question11_button_b = tk.Button(
        question11_win,
        text='Arsenal',
        font=('Arial'),
        width=15,
        command=q11_correct
    )
    question11_button_b.grid(
        row=3,
        column=2
    )

    question11_button_c = tk.Button(
        question11_win,
        text='Chelsea',
        font=('Arial'),
        width=15,
        command=q11_incorrect
    )
    question11_button_c.grid(
        row=4,
        column=1
    )

    question11_button_d = tk.Button(
        question11_win,
        text='Tottenham',
        font=('Arial'),
        width=15,
        command=q11_incorrect
    )
    question11_button_d.grid(
        row=4,
        column=2
    )

    question10_win.destroy()


def question10():
    def q10_correct():
        correct()
        question11()

    def q10_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is August-May')
        question11()

    global question10_win

    question10_win = Toplevel()
    question10_win.geometry('370x90+0+0')
    question10_win.resizable(False,False)
    question10_win.title('Premier League 24/25 Quiz - Q10')

    question10_label = tk.Label(
        question10_win,
        text='When is the start and end of the season?',
        font=('Arial',20)
    )
    question10_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question10_button_a = tk.Button(
        question10_win,
        text='August-May',
        font=('Arial'),
        width=15,
        command=q10_correct
    )
    question10_button_a.grid(
        row=3,
        column=1
    )

    question10_button_b = tk.Button(
        question10_win,
        text='June-January',
        font=('Arial'),
        width=15,
        command=q10_incorrect
    )
    question10_button_b.grid(
        row=3,
        column=2
    )

    question10_button_c = tk.Button(
        question10_win,
        text='September-July',
        font=('Arial'),
        width=15,
        command=q10_incorrect
    )
    question10_button_c.grid(
        row=4,
        column=1
    )

    question10_button_d = tk.Button(
        question10_win,
        text='July-April',
        font=('Arial'),
        width=15,
        command=q10_incorrect
    )
    question10_button_d.grid(
        row=4,
        column=2
    )

    question9_win.destroy()


def question9():
    def q9_correct():
        correct()
        question10()

    def q9_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 20')
        question10()

    global question9_win

    question9_win = Toplevel()
    question9_win.geometry('407x90+0+0')
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

    question8_win.destroy()


def question8():
    def q8_correct():
        correct()
        question9()

    def q8_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Crystal Palace')
        question9()

    global question8_win

    question8_win = Toplevel()
    question8_win.geometry('462x90+0+0')
    question8_win.resizable(False,False)
    question8_win.title('Premier League 24/25 Quiz - Q8')

    question8_label = tk.Label(
        question8_win,
        text='Which club qualified for UEFA Conference League?',
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
        question8()

    def q7_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is David Raya & Matz Sels')
        question8()

    global question7_win

    question7_win = Toplevel()
    question7_win.geometry('622x60+0+0')
    question7_win.resizable(False,False)
    question7_win.title('Premier League 24/25 Quiz - Q7')

    question7_label = tk.Label(
        question7_win,
        text='Which goalkeepers shared the Premier League Golden Glove Award?',
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
        question7()

    def q6_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 1115')
        question7()

    global question6_win

    question6_win = Toplevel()
    question6_win.geometry('482x90+0+0')
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
        question6()

    def q5_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 19th ')
        question6()

    global question5_win

    question5_win = Toplevel()
    question5_win.geometry('312x90+0+0')
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
        question5()

    def q4_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Leicester City')
        question5()

    global question4_win

    question4_win = Toplevel()
    question4_win.geometry('312x90+0+0')
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
        question4()

    def q3_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 29')
        question4()

    global question3_win

    question3_win = Toplevel()
    question3_win.geometry('380x90+0+0')
    question3_win.resizable(False,False)
    question3_win.title('Premier League 24/25 Quiz - Q3')

    question3_label = tk.Label(
        question3_win,
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
        question3()

    def q2_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Mohamed Salah')
        question3()

    global question2_win

    question2_win = Toplevel()
    question2_win.geometry('470x90+0+0')
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
        question2()

    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Liverpool')
        question2()

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