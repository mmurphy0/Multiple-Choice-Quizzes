import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

from time import strftime

def results(question20_win):
    def reset():
        global score
        score = 0
        result_win.destroy()
    
    def save_score():
        time = strftime('%H:%M:%S %D')
        with open('Premier League 25-26 Stadiums Quiz/scores.txt','a') as file:
            file.write(time + '\n' + (f'Score: {score}/20') + '\n' + '----------' + '\n')
            messagebox.showinfo('Confirmation','Result successfully saved')
            reset()

    result_win = Toplevel()
    result_win.geometry('+0+0')
    result_win.resizable(False,False)
    result_win.title('Results')

    result_title = tk.Label(
        result_win,
        text='Results',
        font=('Arial',20,'bold')
    )
    result_title.pack()

    result_label = tk.Label(
        result_win,
        text=f'Score: {score}/20',
        font=('Arial',20)
    )
    result_label.pack()

    continue_button = tk.Button(
        result_win,
        text='Continue',
        font=('Arial'),
        width=20,
        command=save_score
    )
    continue_button.pack()

    question20_win.destroy()

def question20(question19_win):
    def q20_correct():
        correct()
        results(question20_win)

    def q20_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Molineux Stadium')
        results(question20_win)

    question20_win = Toplevel()
    question20_win.geometry('+0+0')
    question20_win.resizable(False,False)
    question20_win.title('Premier League 25/26 Stadiums Quiz - Q20')

    q20_label = tk.Label(
        question20_win,
        text='What is the Wolves stadium called?',
        font=('Arial',20)
    )
    q20_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q20_button_a = tk.Button(
        question20_win,
        text='Selhurst Park',
        font=('Arial'),
        width=20,
        command=q20_incorrect
    )
    q20_button_a.grid(
        row=3,
        column=1
    )

    q20_button_b = tk.Button(
        question20_win,
        text='Old Trafford',
        font=('Arial'),
        width=20,
        command=q20_incorrect
    )
    q20_button_b.grid(
        row=3,
        column=2
    )

    q20_button_c = tk.Button(
        question20_win,
        text='American Express Stadium',
        font=('Arial'),
        width=20,
        command=q20_incorrect
    )
    q20_button_c.grid(
        row=4,
        column=1
    )

    q20_button_d = tk.Button(
        question20_win,
        text='Molineux Stadium',
        font=('Arial'),
        width=20,
        command=q20_correct
    )
    q20_button_d.grid(
        row=4,
        column=2
    )

    question19_win.destroy()

def question19(question18_win):
    def q19_correct():
        correct()
        question20(question19_win)

    def q19_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Turf Moor')
        question20(question19_win)
    
    question19_win = Toplevel()
    question19_win.geometry('+0+0')
    question19_win.resizable(False,False)
    question19_win.title('Premier League 25/26 Stadiums Quiz - Q19')

    q19_label = tk.Label(
        question19_win,
        text='What is the Burnley stadium called?',
        font=('Arial',20)
    )
    q19_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q19_button_a = tk.Button(
        question19_win,
        text='Elland Road',
        font=('Arial'),
        width=20,
        command=q19_incorrect
    )
    q19_button_a.grid(
        row=3,
        column=1
    )

    q19_button_b = tk.Button(
        question19_win,
        text='Turf Moor',
        font=('Arial'),
        width=20,
        command=q19_correct
    )
    q19_button_b.grid(
        row=3,
        column=2
    )

    q19_button_c = tk.Button(
        question19_win,
        text='Stamford Bridge',
        font=('Arial'),
        width=20,
        command=q19_incorrect
    )
    q19_button_c.grid(
        row=4,
        column=1
    )

    q19_button_d = tk.Button(
        question19_win,
        text='Anfield',
        font=('Arial'),
        width=20,
        command=q19_incorrect
    )
    q19_button_d.grid(
        row=4,
        column=2
    )

    question18_win.destroy()

def question18(question17_win):
    def q18_correct():
        correct()
        question19(question18_win)
    
    def q18_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the London Stadium')
        question19(question18_win)

    question18_win = Toplevel()
    question18_win.geometry('+0+0')
    question18_win.resizable(False,False)
    question18_win.title('Premier League 25/26 Stadiums Quiz - Q18')

    q18_label = tk.Label(
        question18_win,
        text='What is the West Ham stadium called?',
        font=('Arial',20)
    )
    q18_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q18_button_a = tk.Button(
        question18_win,
        text='Villa Park',
        font=('Arial'),
        width=20,
        command=q18_incorrect
    )
    q18_button_a.grid(
        row=3,
        column=1
    )

    q18_button_b = tk.Button(
        question18_win,
        text='Old Trafford',
        font=('Arial'),
        width=20,
        command=q18_incorrect
    )
    q18_button_b.grid(
        row=3,
        column=2
    )

    q18_button_c = tk.Button(
        question18_win,
        text="St James' Park",
        font=('Arial'),
        width=20,
        command=q18_incorrect
    )
    q18_button_c.grid(
        row=4,
        column=1
    )

    q18_button_d = tk.Button(
        question18_win,
        text='London Stadium',
        font=('Arial'),
        width=20,
        command=q18_correct
    )
    q18_button_d.grid(
        row=4,
        column=2
    )

    question17_win.destroy()

def question17(question16_win):
    def q17_correct():
        correct()
        question18(question17_win)

    def q17_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Tottenham Hotspur Stadium')
        question18(question17_win)

    question17_win = Toplevel()
    question17_win.geometry('+0+0')
    question17_win.resizable(False,False)
    question17_win.title('Premier League 25/26 Stadiums Quiz - Q17')

    q17_label = tk.Label(
        question17_win,
        text='What is the Tottenham Hotspur stadium called?',
        font=('Arial',20)
    )
    q17_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q17_button_a = tk.Button(
        question17_win,
        text='Emirates Stadium',
        font=('Arial'),
        width=20,
        command=q17_incorrect
    )
    q17_button_a.grid(
        row=3,
        column=1
    )

    q17_button_b = tk.Button(
        question17_win,
        text='Selhurst Park',
        font=('Arial'),
        width=20,
        command=q17_incorrect
    )
    q17_button_b.grid(
        row=3,
        column=2
    )

    q17_button_c = tk.Button(
        question17_win,
        text='Tottenham Hotspur Stadium',
        font=('Arial'),
        width=20,
        command=q17_correct
    )
    q17_button_c.grid(
        row=4,
        column=1
    )

    q17_button_d = tk.Button(
        question17_win,
        text='American Express Stadium',
        font=('Arial'),
        width=20,
        command=q17_incorrect
    )
    q17_button_d.grid(
        row=4,
        column=2
    )

    question16_win.destroy()

def question16(question15_win):
    def q16_correct():
        correct()
        question17(question16_win)
    
    def q16_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is City Ground')
        question17(question16_win)
    
    question16_win = Toplevel()
    question16_win.geometry('+0+0')
    question16_win.resizable(False,False)
    question16_win.title('Premier League 25/26 Stadiums Quiz - Q16')

    q16_label = tk.Label(
        question16_win,
        text='What is the Nottingham Forest stadium called?',
        font=('Arial',20)
    )
    q16_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q16_button_a = tk.Button(
        question16_win,
        text='City Ground',
        font=('Arial'),
        width=20,
        command=q16_correct
    )
    q16_button_a.grid(
        row=3,
        column=1
    )

    q16_button_b = tk.Button(
        question16_win,
        text='Old Trafford',
        font=('Arial'),
        width=20,
        command=q16_incorrect
    )
    q16_button_b.grid(
        row=3,
        column=2
    )

    q16_button_c = tk.Button(
        question16_win,
        text='Turf Moor',
        font=('Arial'),
        width=20,
        command=q16_incorrect
    )
    q16_button_c.grid(
        row=4,
        column=1
    )

    q16_button_d = tk.Button(
        question16_win,
        text='Gtech Community Stadium',
        font=('Arial'),
        width=20,
        command=q16_incorrect
    )
    q16_button_d.grid(
        row=4,
        column=2
    )

    question15_win.destroy()

def question15(question14_win):
    def q15_correct():
        correct()
        question16(question15_win)

    def q15_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Elland Road')
        question16(question15_win)

    question15_win = Toplevel()
    question15_win.geometry('+0+0')
    question15_win.resizable(False,False)
    question15_win.title('Premier League 25/26 Stadiums Quiz - Q15')

    q15_label = tk.Label(
        question15_win,
        text='What is the Leeds United stadium called?',
        font=('Arial',20)
    )
    q15_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q15_button_a = tk.Button(
        question15_win,
        text='Villa Park',
        font=('Arial'),
        width=20,
        command=q15_incorrect
    )
    q15_button_a.grid(
        row=3,
        column=1
    )

    q15_button_b = tk.Button(
        question15_win,
        text='Elland Road',
        font=('Arial'),
        width=20,
        command=q15_correct
    )
    q15_button_b.grid(
        row=3,
        column=2
    )

    q15_button_c = tk.Button(
        question15_win,
        text='Stamford Bridge',
        font=('Arial'),
        width=20,
        command=q15_incorrect
    )
    q15_button_c.grid(
        row=4,
        column=1
    )

    q15_button_d = tk.Button(
        question15_win,
        text='Etihad Stadium',
        font=('Arial'),
        width=20,
        command=q15_incorrect
    )
    q15_button_d.grid(
        row=4,
        column=2
    )

    question14_win.destroy()

def question14(question13_win):
    def q14_correct():
        correct()
        question15(question14_win)

    def q14_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Selhurst Park')
        question15(question14_win)

    question14_win = Toplevel()
    question14_win.geometry('+0+0')
    question14_win.resizable(False,False)
    question14_win.title('Premier League 25/26 Stadiums Quiz - Q14')

    q14_label = tk.Label(
        question14_win,
        text='What is the Crystal Palace stadium called?',
        font=('Arial',20)
    )
    q14_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q14_button_a = tk.Button(
        question14_win,
        text='Elland Road',
        font=('Arial'),
        width=20,
        command=q14_incorrect
    )
    q14_button_a.grid(
        row=3,
        column=1
    )

    q14_button_b = tk.Button(
        question14_win,
        text='London Stadium',
        font=('Arial'),
        width=20,
        command=q14_incorrect
    )
    q14_button_b.grid(
        row=3,
        column=2
    )

    q14_button_c = tk.Button(
        question14_win,
        text='Selhurst Park',
        font=('Arial'),
        width=20,
        command=q14_correct
    )
    q14_button_c.grid(
        row=4,
        column=1
    )

    q14_button_d = tk.Button(
        question14_win,
        text='Craven Cottage',
        font=('Arial'),
        width=20,
        command=q14_incorrect
    )
    q14_button_d.grid(
        row=4,
        column=2
    )

    question13_win.destroy()

def question13(question12_win):
    def q13_correct():
        correct()
        question14(question13_win)
    
    def q13_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Vitality Stadium')
        question14(question13_win)

    question13_win = Toplevel()
    question13_win.geometry('+0+0')
    question13_win.resizable(False,False)
    question13_win.title('Premier League 25/26 Stadiums Quiz - Q13')

    q13_label = tk.Label(
        question13_win,
        text='What is the Bournemouth stadium called?',
        font=('Arial',20)
    )
    q13_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q13_button_a = tk.Button(
        question13_win,
        text='American Express Stadium',
        font=('Arial'),
        width=20,
        command=q13_incorrect
    )
    q13_button_a.grid(
        row=3,
        column=1
    )

    q13_button_b = tk.Button(
        question13_win,
        text='Old Trafford',
        font=('Arial'),
        width=20,
        command=q13_incorrect
    )
    q13_button_b.grid(
        row=3,
        column=2
    )

    q13_button_c = tk.Button(
        question13_win,
        text='City Ground',
        font=('Arial'),
        width=20,
        command=q13_incorrect
    )
    q13_button_c.grid(
        row=4,
        column=1
    )

    q13_button_d = tk.Button(
        question13_win,
        text='Vitality Stadium',
        font=('Arial'),
        width=20,
        command=q13_correct
    )
    q13_button_d.grid(
        row=4,
        column=2
    )

    question12_win.destroy()

def question12(question11_win):
    def q12_correct():
        correct()
        question13(question12_win)
    
    def q12_incorrect():
        messagebox.showinfo('Result',"Incorrect, The answer is St James' Park")
        question13(question12_win)

    question12_win = Toplevel()
    question12_win.geometry('+0+0')
    question12_win.resizable(False,False)
    question12_win.title('Premier League 25/26 Stadiums Quiz - Q12')

    q12_label = tk.Label(
        question12_win,
        text='What is the Newcastle United stadium called?',
        font=('Arial',20)
    )
    q12_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q12_button_a = tk.Button(
        question12_win,
        text='St James Park',
        font=('Arial'),
        width=20,
        command=q12_correct
    )
    q12_button_a.grid(
        row=3,
        column=1
    )

    q12_button_b = tk.Button(
        question12_win,
        text='Villa Park',
        font=('Arial'),
        width=20,
        command=q12_incorrect
    )
    q12_button_b.grid(
        row=3,
        column=2
    )

    q12_button_c = tk.Button(
        question12_win,
        text='Turf Moor',
        font=('Arial'),
        width=20,
        command=q12_incorrect
    )
    q12_button_c.grid(
        row=4,
        column=1
    )

    q12_button_d = tk.Button(
        question12_win,
        text='Molineux Stadium',
        font=('Arial'),
        width=20,
        command=q12_incorrect
    )
    q12_button_d.grid(
        row=4,
        column=2
    )
    question11_win.destroy()

def question11(question10_win):
    def q11_correct():
        correct()
        question12(question11_win)
    
    def q11_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Stadium of Light')
        question12(question11_win)

    question11_win = Toplevel()
    question11_win.geometry('+0+0')
    question11_win.resizable(False,False)
    question11_win.title('Premier League 25/26 Stadiums Quiz - Q11')

    q11_label = tk.Label(
        question11_win,
        text='What is the name of the Sunderland stadium?',
        font=('Arial',20)
    )
    q11_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q11_button_a = tk.Button(
        question11_win,
        text='Selhurst Park',
        font=('Arial'),
        width=20,
        command=q11_incorrect
    )
    q11_button_a.grid(
        row=3,
        column=1
    )

    q11_button_b = tk.Button(
        question11_win,
        text="St James' Park",
        font=('Arial'),
        width=20,
        command=q11_incorrect
    )
    q11_button_b.grid(
        row=3,
        column=2
    )

    q11_button_c = tk.Button(
        question11_win,
        text='Stadium of Light',
        font=('Arial'),
        width=20,
        command=q11_correct
    )
    q11_button_c.grid(
        row=4,
        column=1
    )

    q11_button_d = tk.Button(
        question11_win,
        text='Elland Road',
        font=('Arial'),
        width=20,
        command=q11_incorrect
    )
    q11_button_d.grid(
        row=4,
        column=2
    )
    
    question10_win.destroy()

def question10(question9_win):
    def q10_correct():
        correct()
        question11(question10_win)

    def q10_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the American Express Stadium')
        question11(question10_win)

    question10_win = Toplevel()
    question10_win.geometry('+0+0')
    question10_win.resizable(False,False)
    question10_win.title('Premier League 25/26 Stadiums Quiz - Q10')

    q10_label = tk.Label(
        question10_win,
        text='What is the Brighton stadium called?',
        font=('Arial',20)
    )
    q10_label.grid(
        row=1,
        column=1,
        columnspan=2
    )
    
    q10_button_a = tk.Button(
        question10_win,
        text='Stamford Bridge',
        font=('Arial'),
        width=20,
        command=q10_incorrect
    )
    q10_button_a.grid(
        row=3,
        column=1
    )

    q10_button_b = tk.Button(
        question10_win,
        text='American Express Stadium',
        font=('Arial'),
        width=20,
        command=q10_correct
    )
    q10_button_b.grid(
        row=3,
        column=2
    )

    q10_button_c = tk.Button(
        question10_win,
        text='Etihad Stadium',
        font=('Arial'),
        width=20,
        command=q10_incorrect
    )
    q10_button_c.grid(
        row=4,
        column=1
    )

    q10_button_d = tk.Button(
        question10_win,
        text='London Stadium',
        font=('Arial'),
        width=20,
        command=q10_incorrect
    )
    q10_button_d.grid(
        row=4,
        column=2
    )

    question9_win.destroy()

def question9(question8_win):
    def q9_correct():
        correct()
        question10(question9_win)

    def q9_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Craven Cottage')
        question10(question9_win)

    question9_win = Toplevel()
    question9_win.geometry('+0+0')
    question9_win.resizable(False,False)
    question9_win.title('Premier League 25/26 Stadiums Quiz - Q9')

    q9_label = tk.Label(
        question9_win,
        text='What is the Fulham stadium called?',
        font=('Arial',20)
    )
    q9_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q9_button_a = tk.Button(
        question9_win,
        text='Emirates Stadium',
        font=('Arial'),
        width=20,
        command=q9_incorrect
    )
    q9_button_a.grid(
        row=3,
        column=1
    )

    q9_button_b = tk.Button(
        question9_win,
        text='Old Trafford',
        font=('Arial'),
        width=20,
        command=q9_incorrect
    )
    q9_button_b.grid(
        row=3,
        column=2
    )

    q9_button_c = tk.Button(
        question9_win,
        text='Villa Park',
        font=('Arial'),
        width=20,
        command=q9_incorrect
    )
    q9_button_c.grid(
        row=4,
        column=1
    )

    q9_button_d = tk.Button(
        question9_win,
        text='Craven Cottage',
        font=('Arial'),
        width=20,
        command=q9_correct
    )
    q9_button_d.grid(
        row=4,
        column=2
    )

    question8_win.destroy()

def question8(question7_win):
    def q8_correct():
        correct()
        question9(question8_win)

    def q8_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Hill Dickinson Stadium')
        question9(question8_win)

    question8_win = Toplevel()
    question8_win.geometry('+0+0')
    question8_win.resizable(False,False)
    question8_win.title('Premier League 25/26 Stadiums Quiz - Q8')

    q8_label = tk.Label(
        question8_win,
        text='What is the Everton stadium called?',
        font=('Arial',20)
    )
    q8_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q8_button_a = tk.Button(
        question8_win,
        text='Hill Dickinson Stadium',
        font=('Arial'),
        width=20,
        command=q8_correct
    )
    q8_button_a.grid(
        row=3,
        column=1
    )

    q8_button_b = tk.Button(
        question8_win,
        text='Goodison Park',
        font=('Arial'),
        width=20,
        command=q8_incorrect
    )
    q8_button_b.grid(
        row=3,
        column=2
    )

    q8_button_c = tk.Button(
        question8_win,
        text='Molineux Stadium',
        font=('Arial'),
        width=20,
        command=q8_incorrect
    )
    q8_button_c.grid(
        row=4,
        column=1
    )

    q8_button_d = tk.Button(
        question8_win,
        text='Turf Moor',
        font=('Arial'),
        width=20,
        command=q8_incorrect
    )
    q8_button_d.grid(
        row=4,
        column=2
    )

    question7_win.destroy()

def question7(question6_win):
    def q7_correct():
        correct()
        question8(question7_win)

    def q7_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Vitality Stadium')
        question8(question7_win)

    question7_win = Toplevel()
    question7_win.geometry('+0+0')
    question7_win.resizable(False,False)
    question7_win.title('Premier League 25/26 Stadiums Quiz - Q7')
    
    q7_label = tk.Label(
        question7_win,
        text='What is the Brentford stadium called?',
        font=('Arial',20)
    )
    q7_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q7_button_a = tk.Button(
        question7_win,
        text='Gtech Community Stadium',
        font=('Arial'),
        width=20,
        command=q7_incorrect
    )
    q7_button_a.grid(
        row=3,
        column=1
    )

    q7_button_b = tk.Button(
        question7_win,
        text='Old Trafford',
        font=('Arial'),
        width=20,
        command=q7_incorrect
    )
    q7_button_b.grid(
        row=3,
        column=2
    )

    q7_button_c = tk.Button(
        question7_win,
        text='Selhurst Park',
        font=('Arial'),
        width=20,
        command=q7_incorrect
    )
    q7_button_c.grid(
        row=4,
        column=1
    )

    q7_button_d = tk.Button(
        question7_win,
        text='Vitality Stadium',
        font=('Arial'),
        width=20,
        command=q7_correct
    )
    q7_button_d.grid(
        row=4,
        column=2
    )

    question6_win.destroy()

def question6(question5_win):
    def q6_correct():
        correct()
        question7(question6_win)

    def q6_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Stamford Bridge')
        question7(question6_win)

    question6_win = Toplevel()
    question6_win.geometry('+0+0')
    question6_win.resizable(False,False)
    question6_win.title('Premier League 25/26 Stadiums Quiz - Q6')

    q6_label = tk.Label(
        question6_win,
        text='What is the Chelsea stadium called?',
        font=('Arial',20)
    )
    q6_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q6_button_a = tk.Button(
        question6_win,
        text='Craven Cottage',
        font=('Arial'),
        width=20,
        command=q6_incorrect
    )
    q6_button_a.grid(
        row=3,
        column=1
    )

    q6_button_b = tk.Button(
        question6_win,
        text='Stamford Bridge',
        font=('Arial'),
        width=20,
        command=q6_correct
    )
    q6_button_b.grid(
        row=3,
        column=2
    )

    q6_button_c = tk.Button(
        question6_win,
        text='Emirates Stadium',
        font=('Arial'),
        width=20,
        command=q6_incorrect
    )
    q6_button_c.grid(
        row=4,
        column=1
    )

    q6_button_d = tk.Button(
        question6_win,
        text='London Stadium',
        font=('Arial'),
        width=20,
        command=q6_incorrect
    )
    q6_button_d.grid(
        row=4,
        column=2
    )

    question5_win.destroy()

def question5(question4_win):
    def q5_correct():
        correct()
        question6(question5_win)

    def q5_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Villa Park')
        question6(question5_win)

    question5_win = Toplevel()
    question5_win.geometry('+0+0')
    question5_win.resizable(False,False)
    question5_win.title('Premier League 25/26 Quiz - Q5')

    q5_label = tk.Label(
        question5_win,
        text='What is the Aston Villa stadium called?',
        font=('Arial',20)
    )
    q5_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q5_button_a = tk.Button(
        question5_win,
        text='Emirates Stadium',
        font=('Arial'),
        width=20,
        command=q5_incorrect
    )
    q5_button_a.grid(
        row=3,
        column=1
    )

    q5_button_b = tk.Button(
        question5_win,
        text='Elland Road',
        font=('Arial'),
        width=20,
        command=q5_incorrect
    )
    q5_button_b.grid(
        row=3,
        column=2
    )

    q5_button_c = tk.Button(
        question5_win,
        text='Villa Park',
        font=('Arial'),
        width=20,
        command=q5_correct
    )
    q5_button_c.grid(
        row=4,
        column=1
    )

    q5_button_d = tk.Button(
        question5_win,
        text='Gtech Community Stadium',
        font=('Arial'),
        width=20,
        command=q5_incorrect
    )
    q5_button_d.grid(
        row=4,
        column=2
    )

    question4_win.destroy()

def question4(question3_win):
    def q4_correct():
        correct()
        question5(question4_win)

    def q4_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Old Trafford')
        question5(question4_win)
    
    question4_win = Toplevel()
    question4_win.geometry('+0+0')
    question4_win.resizable(False,False)
    question4_win.title('Premier League 25/26 Stadiums Quiz - Q4')

    q4_label = tk.Label(
        question4_win,
        text='What is the Manchester United stadium called?',
        font=('Arial',20)
    )
    q4_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q4_button_a = tk.Button(
        question4_win,
        text='Villa Park',
        font=('Arial'),
        width=20,
        command=q4_incorrect
    )
    q4_button_a.grid(
        row=3,
        column=1
    )

    q4_button_b = tk.Button(
        question4_win,
        text='Old Trafford',
        font=('Arial'),
        width=20,
        command=q4_correct
    )
    q4_button_b.grid(
        row=3,
        column=2
    )

    q4_button_c = tk.Button(
        question4_win,
        text='Turf Moor',
        font=('Arial'),
        width=20,
        command=q4_incorrect
    )
    q4_button_c.grid(
        row=4,
        column=1
    )

    q4_button_d = tk.Button(
        question4_win,
        text='City Ground',
        font=('Arial'),
        width=20,
        command=q4_incorrect
    )
    q4_button_d.grid(
        row=4,
        column=2
    )

    question3_win.destroy()

def question3(question2_win):
    def q3_correct():
        correct()
        question4(question3_win)
    
    def q3_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is the Etihad Stadium')
        question4(question3_win)

    question3_win = Toplevel()
    question3_win.geometry('+0+0')
    question3_win.resizable(False,False)
    question3_win.title('Premier League 25/26 Stadiums Quiz - Q3')

    q3_label = tk.Label(
        question3_win,
        text='What is the Manchester City stadium called?',
        font=('Arial',20)
    )
    q3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q3_button_a = tk.Button(
        question3_win,
        text='Old Trafford',
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
        text='American Express Stadium',
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
        text='Selhurt Park',
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
        text='Etihad Stadium',
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
        messagebox.showinfo('Result','Incorrect, The answer is the Emirates Stadium')
        question3(question2_win)

    question2_win = Toplevel()
    question2_win.geometry('+0+0')
    question2_win.resizable(False,False)
    question2_win.title('Premier League 25/26 Stadiums Quiz - Q2')

    q2_label = tk.Label(
        question2_win,
        text='What is the Arsenal stadium called?',
        font=('Arial',20)
    )
    q2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q2_button_a = tk.Button(
        question2_win,
        text='Stamford Bridge',
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
        text='London Stadium',
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
        text='Emirates Stadium',
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
        text='Craven Cottage',
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
        messagebox.showinfo('Result','Incorrect, The answer is Anfield')
        question2(question1_win)

    question1_win = Toplevel()
    question1_win.geometry('+0+0')
    question1_win.resizable(False,False)
    question1_win.title('Premier League 25/26 Stadiums Quiz - Q1')

    q1_label = tk.Label(
        question1_win,
        text=f'What is the Liverpool stadium called?',
        font=('Arial',20)
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = tk.Button(
        question1_win,
        text='Anfield',
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
        text='Old Trafford',
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
        text='Etihad Stadium',
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
        text='Villa Park',
        font=('Arial'),
        width=20,
        command=q1_incorrect
    )
    q1_button_d.grid(
        row=4,
        column=2
    )

def correct():
    messagebox.showinfo('Result','Correct!')
    global score
    score += 1
    return

score = 0

root = tk.Tk()
root.geometry('+0+0')
root.resizable(False,False)
root.title('Premier League 25/26 Stadiums Quiz')

root_title = tk.Label(
    root,
    text='Premier League 25/26 Stadiums Quiz',
    font=('Arial',20,'bold')
)
root_title.pack(anchor='center')

startquiz_button = tk.Button(
    root,
    text='Start',
    font=('Arial'),
    width=20,
    command=question1
)
startquiz_button.pack(anchor='center')

root.mainloop()