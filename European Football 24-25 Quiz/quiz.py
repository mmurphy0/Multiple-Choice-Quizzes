import tkinter as tk
from tkinter import messagebox, Toplevel
from time import strftime

def question24():
    def q24_correct():
        correct()
        question25()

    def q24_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Barcelona')
        question25()

    global question24_win

    question24_win = Toplevel()
    question24_win.geometry('320x90+0+0')
    question24_win.resizable(False,False)
    question24_win.title('European Football 24-25 Quiz - Q24')

    q24_label = tk.Label(
        question24_win,
        text='Who won the Copa del Rey?',
        font=('Arial',20)
    )
    q24_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q24_button_a = tk.Button(
        question24_win,
        text='Real Madrid',
        font=('Arial'),
        width=15,
        command=q24_incorrect
    )
    q24_button_a.grid(
        row=3,
        column=1
    )

    q24_button_b = tk.Button(
        question24_win,
        text='Athletic Club',
        font=('Arial'),
        width=15,
        command=q24_incorrect
    )
    q24_button_b.grid(
        row=3,
        column=2
    )

    q24_button_c = tk.Button(
        question24_win,
        text='Barcelona',
        font=('Arial'),
        width=15,
        command=q24_correct
    )
    q24_button_c.grid(
        row=4,
        column=1
    )

    q24_button_d = tk.Button(
        question24_win,
        text='Real Betis',
        font=('Arial'),
        width=15,
        command=q24_incorrect
    )
    q24_button_d.grid(
        row=4,
        column=2
    )

    question23_win.destroy()

def question23():
    def q23_correct():
        correct()
        question24()

    def q23_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is France')
        question24()

    global question23_win

    question23_win = Toplevel()
    question23_win.geometry('320x90+0+0')
    question23_win.resizable(False,False)
    question23_win.title('European Football 24-25 Quiz - Q23')

    q23_label = tk.Label(
        question23_win,
        text='Which country is Ligue 1 played in?',
        font=('Arial',20)
    )
    q23_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q23_button_a = tk.Button(
        question23_win,
        text='Italy',
        font=('Arial'),
        width=15,
        command=q23_incorrect
    )
    q23_button_a.grid(
        row=3,
        column=1
    )

    q23_button_b = tk.Button(
        question23_win,
        text='France',
        font=('Arial'),
        width=15,
        command=q23_correct
    )
    q23_button_b.grid(
        row=3,
        column=2
    )

    question22_win.destroy()

def question22():
    def q22_correct():
        correct()
        question23()

    def q22_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Newcastle')
        question23()

    global question22_win

    question22_win = Toplevel()
    question22_win.geometry('320x90+0+0')
    question22_win.resizable(False,False)
    question22_win.title('European Football 24-25 Quiz - Q22')

    q22_label = tk.Label(
        question22_win,
        text='Which Premier League team was 5th?',
        font=('Arial',20)
    )
    q22_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q22_button_a = tk.Button(
        question22_win,
        text='Newcastle United',
        font=('Arial'),
        width=15,
        command=q22_correct
    )
    q22_button_a.grid(
        row=3,
        column=1
    )

    q22_button_b = tk.Button(
        question22_win,
        text='Aston Villa',
        font=('Arial'),
        width=15,
        command=q22_incorrect
    )
    q22_button_b.grid(
        row=3,
        column=2
    )

    q22_button_c = tk.Button(
        question22_win,
        text='Nottingham Forest',
        font=('Arial'),
        width=15,
        command=q22_incorrect
    )
    q22_button_c.grid(
        row=4,
        column=1
    )

    q22_button_d = tk.Button(
        question22_win,
        text='Brighton',
        font=('Arial'),
        width=15,
        command=q22_incorrect
    )
    q22_button_d.grid(
        row=4,
        column=2
    )

    question21_win.destroy()

def question21():
    def q21_correct():
        correct()
        question22()
    
    def q21_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Raphina')
        question22()

    global question21_win

    question21_win = Toplevel()
    question21_win.geometry('320x90+0+0')
    question21_win.resizable(False,False)
    question21_win.title('European Football 24-25 Quiz - Q22')

    q21_label = tk.Label(
        question21_win,
        text='Who was the top scorer for Barcelona?',
        font=('Arial',20)
    )
    q21_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q21_button_a = tk.Button(
        question21_win,
        text='Lamine Yamal',
        font=('Arial'),
        width=15,
        command=q21_incorrect
    )
    q21_button_a.grid(
        row=3,
        column=1
    )

    q21_button_b = tk.Button(
        question21_win,
        text='Robert Lewandoski',
        font=('Arial'),
        width=15,
        command=q21_incorrect
    )
    q21_button_b.grid(
        row=3,
        column=2
    )

    q21_button_c = tk.Button(
        question21_win,
        text='Raphina',
        font=('Arial'),
        width=15,
        command=q21_correct
    )
    q21_button_c.grid(
        row=4,
        column=1
    )

    q21_button_d = tk.Button(
        question21_win,
        text='Pedri',
        font=('Arial'),
        width=15,
        command=q21_incorrect
    )
    q21_button_d.grid(
        row=4,
        column=2
    )

    question20_win.destroy()

def question20():
    def q20_correct():
        correct()
        question21()

    def q20_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is PSG')
        question21()

    global question20_win

    question20_win = Toplevel()
    question20_win.geometry('320x90+0+0')
    question20_win.resizable(False,False)
    question20_win.title('European Football 24-25 Quiz - Q20')

    q20_label = tk.Label(
        question20_win,
        text='Who won the Super Cup?',
        font=('Arial',20)
    )
    q20_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q20_button_a = tk.Button(
        question20_win,
        text='Tottenham',
        font=('Arial'),
        width=15,
        command=q20_incorrect
    )
    q20_button_a.grid(
        row=3,
        column=1
    )

    q20_button_b = tk.Button(
        question20_win,
        text='PSG',
        font=('Arial'),
        width=15,
        command=q20_correct
    )
    q20_button_b.grid(
        row=3,
        column=2
    )

    q20_button_c = tk.Button(
        question20_win,
        text='Chelsea',
        font=('Arial'),
        width=15,
        command=q20_incorrect
    )
    q20_button_c.grid(
        row=4,
        column=1
    )

    q20_button_d = tk.Button(
        question20_win,
        text='Real Madrid',
        font=('Arial'),
        width=15,
        command=q20_incorrect
    )
    q20_button_d.grid(
        row=4,
        column=2
    )

    question19_win.destroy()

def question19():
    def q19_correct():
        correct()
        question20()

    def q19_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Arsenal')
        question20()

    global question19_win

    question19_win = Toplevel()
    question19_win.geometry('320x90+0+0')
    question19_win.resizable(False,False)
    question19_win.title('European Football 24-25 Quiz - Q19')

    q19_label = tk.Label(
        question19_win,
        text='Which team is known as "The Reds"?',
        font=('Arial',20)
    )
    q19_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q19_button_a = tk.Button(
        question19_win,
        text='Liverpool',
        font=('Arial'),
        width=15,
        command=q19_correct
    )
    q19_button_a.grid(
        row=3,
        column=1
    )

    q19_button_b = tk.Button(
        question19_win,
        text='Manchester United',
        font=('Arial'),
        width=15,
        command=q19_incorrect
    )
    q19_button_b.grid(
        row=3,
        column=2
    )

    q19_button_c = tk.Button(
        question19_win,
        text='Arsenal',
        font=('Arial'),
        width=15,
        command=q19_incorrect
    )
    q19_button_c.grid(
        row=4,
        column=1
    )

    q19_button_d = tk.Button(
        question19_win,
        text='Nottingham Forest',
        font=('Arial'),
        width=15,
        commanf=q19_incorrect
    )
    q19_button_d.grid(
        row=4,
        column=2
    )

    question18_win.destroy()

def question18():
    def q18_correct():
        correct()
        question19()
    
    def q18_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is True')
        question19()

    global question18_win

    question18_win = Toplevel()
    question18_win.geometry('320x90+0+0')
    question18_win.resizable(False,False)
    question18_win.title('European Football 24-25 Quiz - Q18')

    q18_label = tk.Label(
        question18_win,
        text='Do AC Milan & Inter Milan share the San Siro?',
        font=('Arial'),
    )
    q18_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q18_button_a = tk.Button(
        question18_win,
        text='True',
        font=('Arial'),
        width=15,
        command=q18_correct
    )
    q18_button_a.grid(
        row=3,
        column=1
    )

    q18_button_b = tk.Button(
        question18_win,
        text='False',
        font=('Arial'),
        width=15,
        commanf=q18_incorrect
    )
    q18_button_b.grid(
        row=3,
        column=2
    )

    question17_win.destroy()

def question17():
    def q17_correct():
        correct()
        question18()

    def q17_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Celtic')
        question18()

    global question17_win

    question17_win = Toplevel()
    question17_win.geometry('320x90+0+0')
    question17_win.resizable(False,False)
    question17_win.title('European Football 24-25 Quiz - Q18')

    q17_label = tk.Label(
        question17_win,
        text='Who won the Scottish Premiership?',
        font=('Arial',20)
    )
    q17_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q17_button_a = tk.Button(
        question17_win,
        text='Hearts',
        font=('Arial'),
        width=15,
        command=q17_correct
    )
    q17_button_a.grid(
        row=3,
        column=1
    )

    q17_button_b = tk.Button(
        question17_win,
        text='Rangers',
        font=('Arial'),
        width=15,
        command=q17_incorrect
    )
    q17_button_b.grid(
        row=3,
        column=2
    )
    
    q17_button_c = tk.Button(
        question17_win,
        text='Hibernian',
        font=('Arial'),
        width=15,
        command=q17_incorrect
    )
    q17_button_c.grid(
        row=4,
        column=1
    )

    q17_button_d = tk.Button(
        question17_win,
        text='Celtic',
        font=('Arial'),
        width=15,
        command=q17_correct
    )
    q17_button_d.grid(
        row=4,
        column=2
    )

    question16_win.destroy()

def question16():
    def q16_correct():
        correct()
        question17()

    def q16_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Newcastle United')
        question17()

    global question16_win

    question16_win = Toplevel()
    question16_win.geometry('320x90+0+0')
    question16_win.resizable(False,False)
    question16_win.title('European Football 24-25 Quiz - Q16')

    q16_label = tk.Label(
        question16_win,
        text='Who won the EFL Cup?',
        font=('Arial',20),
    )
    q16_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q16_button_a = tk.Button(
        question16_win,
        text='Manchester City',
        font=('Arial'),
        width=15,
        command=q16_incorrect
    )
    q16_button_a.grid(
        row=3,
        column=1
    )

    q16_button_b = tk.Button(
        question16_win,
        text='Liverpool',
        font=('Arial'),
        width=15,
        command=q16_correct
    )
    q16_button_b.grid(
        row=3,
        column=2
    )

    q16_button_c = tk.Button(
        question16_win,
        text='Newcastle United',
        font=('Arial'),
        width=15,
        command=q16_incorrect
    )
    q16_button_c.grid(
        row=4,
        column=1
    )

    q16_button_d = tk.Button(
        question16_win,
        text='Arsenal',
        font=('Arial'),
        width=15,
        command=q16_incorrect
    )
    q16_button_d.grid(
        row=4,
        column=2
    )

    question15_win.destroy()

def question15():
    def q15_correct():
        correct()
        question16()
    
    def q15_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Anfield')
        question16()

    global question15_win

    question15_win = Toplevel()
    question15_win.geometry('320x90+0+0')
    question15_win.resizable(False,False)
    question15_win.title('European Football Quiz - Q15')

    q15_label = tk.Label(
        question15_win,
        text='Which clubs stadium is Anfield?',
        font=('Arial'),
    )
    q15_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q15_button_a = tk.Button(
        question15_win,
        text='Liverpool',
        font=('Arial'),
        width=15,
        command=q15_correct
    )
    q15_button_a.grid(
        row=3,
        column=1
    )

    q15_button_b = tk.Button(
        question15_win,
        text='Everton',
        font=('Arial'),
        width=15,
        command=q15_incorrect
    )
    q15_button_b.grid(
        row=3,
        column=2
    )

    q15_button_c = tk.Button(
        question15_win,
        text='Leeds United',
        font=('Arial'),
        width=15,
        command=q15_incorrect
    )
    q15_button_c.grid(
        row=4,
        column=1
    )

    q15_button_d = tk.Button(
        question15_win,
        text='Manchester United',
        font=('Arial'),
        width=15,
        command=q15_incorrect
    )
    q15_button_d.grid(
        row=4,
        column=2
    )

    question14_win.destroy()

def question14():
    def q14_correct():
        correct()
        question15()

    def q14_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Chelsea')
        question15()

    global question14_win

    question14_win = Toplevel()
    question14_win.geometry('320x90+0+0')
    question14_win.resizable(False,False)
    question14_win.title('European Football 24-25 Quiz - Q14')

    q14_label = tk.Label(
        question14_win,
        text='Who was 4th in the Premier League',
        font=('Arial',20)
    )
    q14_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q14_button_a = tk.Button(
        question14_win,
        text='Chelsea',
        font=('Arial'),
        width=15,
        command=q14_correct
    )
    q14_button_a.grid(
        row=3,
        column=1
    )

    q14_button_b = tk.Button(
        question14_win,
        text='Newcastle United',
        font=('Arial'),
        width=15,
        command=q14_incorrect
    )
    q14_button_b.grid(
        row=3,
        column=2
    )

    q14_button_c = tk.Button(
        question14_win,
        text='Aston Villa',
        font=('Arial'),
        width=15,
        command=q14_incorrect
    )
    q14_button_c.grid(
        row=4,
        column=1
    )

    q14_button_d = tk.Button(
        question14_win,
        text='Manchester United',
        font=('Arial'),
        width=15,
        command=q14_incorrect
    )
    q14_button_d.grid(
        row=4,
        column=2
    )

    question13_win.destroy()

def question13():
    def q13_correct():
        correct()
        question14()

    def q13_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Ousmane Dembélé')
        question14()

    global question13_win

    question13_win = Toplevel()
    question13_win.geometry('320x90+0+0')
    question13_win.resizable(False,False)
    question13_win.title('European Football 24-25 Quiz')

    q13_label = tk.Label(
        question13_win,
        text="Whow on the Ballon d'Or?",
        font=('Arial',20)
    )
    q13_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q13_button_a = tk.Button(
        question13_win,
        text='Kylian Mbappé',
        font=('Arial'),
        width=15,
        command=q13_incorrect
    )
    q13_button_a.grid(
        row=3,
        column=1
    )

    q13_button_b = tk.Button(
        question13_win,
        text='Jude Bellingham',
        font=('Arial'),
        width=15,
        command=q13_incorrect
    )
    q13_button_b.grid(
        row=3,
        column=2
    )

    q13_button_c = tk.Button(
        question13_win,
        text='Ousmane Dembélé',
        font=('Arial'),
        width=15,
        command=q13_correct
    )
    q13_button_c.grid(
        row=4,
        column=1
    )

    q13_button_d = tk.Button(
        question13_win,
        text='Mohamed Salah',
        font=('Arial'),
        width=15,
        command=q13_incorrect
    )
    q13_button_d.grid(
        row=4,
        column=2
    )

    question12_win.destroy()

def question12():
    def q12_correct():
        correct()
        question13()

    def q12_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Brennan Johnson')
        question13()

    global question12_win

    question12_win = Toplevel()
    question12_win.geometry('320x90+0+0')
    question12_win.resizable(False,False)
    question12_win.title('European Football 24-25 Quiz - Q12')

    q12_label = tk.Label(
        question12_win,
        text='Who scored in the Europa League Final?',
        font=('Arial',20),
    )
    q12_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q12_button_a = tk.Button(
        question12_win,
        text='Son Heung-min',
        font=('Arial'),
        width=15,
        command=q12_incorrect
    )
    q12_button_a.grid(
        row=3,
        column=1,
    )

    q12_button_b = tk.Button(
        question12_win,
        text='Brennan Johnson',
        font=('Arial'),
        width=15,
        command=q12_correct
    )
    q12_button_b.grid(
        row=3,
        column=2
    )

    q12_button_c = tk.Button(
        question12_win,
        text='Luke Shaw',
        font=('Arial'),
        width=15,
        command=q12_incorrect
    )
    q12_button_c.grid(
        row=4,
        column=1
    )

    q12_button_d = tk.Button(
        question12_win,
        text='Rasmus Hojlund',
        font=('Arial'),
        width=15,
        command=q12_incorrect
    )
    q12_button_d.grid(
        row=4,
        column=2
    )

    question11_win.destroy()

def question11():
    def q11_correct():
        correct()
        question12()

    def q11_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Harry Kane')
        question12()

    global question11_win

    question11_win = Toplevel()
    question11_win.geometry('320x90+0+0')
    question11_win.resizable(False,False)
    question11_win.title('European Football 24-25 Quiz - Q11')

    q11_label = tk.Label(
        question12_win,
        text='Who was the Bundesliga top goalscorer?',
        font=('Arial',20)
    )
    q11_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q11_button_a = tk.Button(
        question12_win,
        text='Leroy Sané',
        font=('Arial'),
        width=15,
        command=q11_incorrect
    )
    q11_button_a.grid(
        row=3,
        column=2
    )

    q11_button_b = tk.Button(
        question11_win,
        text='Harry Kane',
        font=('Arial'),
        width=15,
        command=q11_correct
    )
    q11_button_b.grid(
        row=3,
        column=2
    )

    q11_button_c = tk.Button(
        question11_win,
        text='Niclas Füllkrug',
        font=('Arial'),
        width=15,
        command=q11_incorrect
    )
    q11_button_c.grid(
        row=4,
        column=1
    )
    
    q11_button_d = tk.Button(
        question11_win,
        text='Jonas Hofmann',
        font=('Arial'),
        width=15,
        command=q11_incorrect
    )
    q11_button_d.grid(
        row=4,
        column=2
    )

    question10_win.destroy()

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