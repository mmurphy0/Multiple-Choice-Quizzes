import tkinter as tk
from tkinter import Toplevel, messagebox
import datetime
from datetime import datetime

def question17():
    def q17_correct():
        correct()
        question18()

    def q17_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Charles Leclerc')
        question18()

    global question17_win

    question17_win = Toplevel()
    question17_win.geometry('320x90+0+0')
    question17_win.resizable(False,False)
    question17_win.title('F1 2025 Quiz - Q17')

    question17_label = tk.Label(
        question17_win,
        text='Which driver did not win the Abu Dhabu Grand Prix?',
        font=('Arial',20)
    )
    question17_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question17_button_a = tk.Button(
        question17_win,
        text='Max Verstappen',
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
        text='Lando Norris',
        font=('Arial'),
        width=15,
        command=q17_incorrect
    )
    question17_button_b.grid(
        row=3,
        column=1
    )

    question17_button_c = tk.Button(
        question17_win,
        text='Oscar Piastri',
        font=('Arial'),
        width=15,
        command=q17_incorrect
    )
    question17_button_c.grid(
        row=4,
        column=1
    )

    question17_button_d = tk.Button(
        question17_win,
        text='Charles Leclerc',
        font=('Arial'),
        width=15,
        command=q17_correct
    )
    question17_button_d.grid(
        row=4,
        column=1
    )

    question16_win.destroy()


def question16():
    def q16_correct():
        correct()
        question17()

    def q16_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Mercedes')
        question17()

    global question16_win

    question16_win = Toplevel()
    question16_win.geometry('320x90+0+0')
    question16_win.resizable(False,False)
    question16_win.title('F1 2025 Quiz - Q16')

    question16_label = tk.Label(
        question16_win,
        text="Which team was 4th in the Constructors' Championship?",
        font=('Arial',20)
    )
    question16_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question16_button_a = tk.Button(
        question16_win,
        text='Williams',
        font=('Arial'),
        width=15,
        command=q16_incorrect
    )
    question16_button_a.grid(
        row=3,
        column=1
    )

    question16_button_b = tk.Button(
        question16_win,
        text='Mercedes',
        font=('Arial'),
        width=15,
        command=q16_correct
    )
    question16_button_b.grid(
        row=3,
        column=2
    )

    question16_button_c = tk.Button(
        question16_win,
        text='Ferrari',
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
        text='Red Bull',
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
        messagebox.showinfo('Result','Incorrect, The answer is all of the above')
        question16()

    global question15_win

    question15_win = Toplevel()
    question15_win.geometry('320x90+0+0')
    question15_win.resizable(False,False)
    question15_win.title('F1 2025 Quiz - Q16')

    question15_label = tk.Label(
        question15_win,
        text="Which driver finished ahead of Charles Leclerc in the Drivers' standings?",
        font=('Arial',20),
        width=15,
        command=q15_incorrect
    )
    question15_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question15_button_a = tk.Button(
        question15_win,
        text='Max Verstappen',
        font=('Arial'),
        width=15,
        command=q15_incorrect
    )
    question15_button_a.grid(
        row=3,
        column=1
    )

    question15_button_b = tk.Button(
        question15_win,
        text='Oscar Piastri',
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
        text='Lando Norris',
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
        text='All of the above',
        font=('Arial'),
        width=15,
        command=q15_correct
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
        messagebox.showinfo('Result','Incorrect, The answer is 8')
        question15()

    global question14_win

    question14_win = Toplevel()
    question14_win.geometry('320x90+0+0')
    question14_win.resizable(False,False)
    question14_win.title('F1 2025 Quiz - Q15')

    question14_label = tk.Label(
        question14_win,
        text='How many races did Lando Norris win?',
        font=('Arial',20)
    )
    question14_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question14_button_a = tk.Button(
        question14_win,
        text='4',
        font=('Arial'),
        width=15,
        command=q14_incorrect
    )
    question14_button_a.grid(
        row=3,
        column=1
    )

    question14_button_b = tk.Button(
        question14_win,
        text='6',
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
        text='8',
        font=('Arial'),
        width=15,
        command=q14_correct
    )
    question14_button_c.grid(
        row=4,
        column=1
    )

    question14_button_d = tk.Button(
        question14_win,
        text='10',
        font=('Arial'),
        width=15,
        command=q14_incorrect
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
        messagebox.showinfo('Result','Incorrect, The answer is 4')
        question14()

    global question13_win

    question13_win = Toplevel()
    question13_win.geometry('320x90+0+0')
    question13_win.resizable(False,False)
    question13_win.title('F1 2025 Quiz - Q14')

    question13_label = tk.Label(
        question13_win,
        text="Which number is Lando Norris' ?",
        font=('Arial',20)
    )
    question13_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question13_button_a = tk.Button(
        question13_win,
        text='44',
        font=('Arial'),
        width=15,
        command=q13_incorrect
    )
    question13_button_a.grid(
        row=3,
        column=1
    )

    question13_button_b = tk.Button(
        question13_win,
        text='4',
        font=('Arial'),
        width=15,
        command=q13_correct
    )
    question13_button_b.grid(
        row=3,
        column=2
    )

    question13_button_c = tk.Button(
        question13_win,
        text='55',
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
        text='16',
        font=('Arial'),
        width=15,
        command=q13_incorrect
    )
    question13_button_d.grid(
        row=4,
        column=2
    )

    question13_win.destroy()


def question12():
    def q12_correct():
        correct()
        question13()

    def q12_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Lando Norris')
        question13()

    global question12_win

    question12_win = Toplevel()
    question12_win.geometry('320x90+0+0')
    question12_win.resizable(False,False)
    question12_win.title('F1 2025 Quiz - Q12')
    
    question12_label = tk.Label(
        question12_win,
        text='Which British driver won his first world title?',
        font=('Arial',20)
    )
    question12_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question12_button_a = tk.Button(
        question12_win,
        text='Lewis Hamilton',
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
        text='George Russell',
        font=('Arial'),
        width=15,
        command=q12_incorrect
    )
    question12_button_b.grid(
        row=3,
        column=1
    )

    question12_button_c = tk.Button(
        question12_win,
        text='Lando Norris',
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
        text='Alex Albon',
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
        messagebox.showinfo('Result','Incorrect, The answer is George Russell')
        question12()

    global question11_win

    question11_win = Toplevel()
    question11_win.geometry('320x90+0+0')
    question11_win.resizable(False,False)
    question11_win.title('F1 2025 Quiz - Q11')

    question11_label = tk.Label(
        question11_win,
        text="Which driver was 4th in the Drivers' standings?",
        font=('Arial',20)
    )
    question11_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question11_button_a = tk.Button(
        question11_win,
        text='Charles Leclerc',
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
        text='George Russell',
        font=('Arial'),
        width=15,
        command=q11_correct
    )
    question11_button_b.grid(
        row=3,
        column=1
    )

    question11_button_c = tk.Button(
        question11_win,
        text='Lewis Hamilton',
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
        text='Alex Albon',
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
        messagebox.showinfo('Result','Incorrect, The answer is Red Bull')
        question11()

    global question10_win

    question10_win = Toplevel()
    question10_win.geometry('320x90+0+0')
    question10_win.resizable(False,False)
    question10_win.title('F1 2025 Quiz - Q10')

    question10_label = tk.Label(
        question10_win,
        text="Which team was 3rd in the Constructors' Championship?",
        font=('Arial',20)
    )
    question10_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question10_button_a = tk.Button(
        question10_win,
        text='Red Bull',
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
        text='Ferrari',
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
        text='Williams',
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
        text='Aston Martin',
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
        messagebox.showinfo('Result','Incorrect, The answer is Mercedes')
        question10()

    global question9_win

    question9_win = Toplevel()
    question9_win.geometry('320x90+0+0')
    question9_win.resizable(False,False)
    question9_win.title('F1 2025 Quiz - Q9')

    question9_label = tk.Label(
        question9_win,
        text='Which team did George Russell race for?',
        font=('Arial',20)
    )
    question9_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question9_button_a = tk.Button(
        question9_win,
        text='Ferrari',
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
        text='Mercedes',
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
        text='McLaren',
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
        text='Red Bull',
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
        messagebox.showinfo('Result','Incorrect, The answer is Max Verstappen')
        question9()

    global question8_win

    question8_win = Toplevel()
    question8_win.geometry('320x90+0+0')
    question8_win.resizable(False,False)
    question8_win.title('F1 2025 Quiz - Q8')

    question8_label = tk.Label(
        question8_win,
        text='Which driver won the Abu Dhabi Grand Prix?',
        font=('Arial',20)
    )
    question8_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question8_button_a = tk.Button(
        question8_win,
        text='Lando Norris',
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
        text='Oscar Piastri',
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
        text='Max Verstappen',
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
        text='George Russell',
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
        messagebox.showinfo('Result','Incorrect, The answer is 2')
        question8()

    global question7_win

    question7_win = Toplevel()
    question7_win.geometry('320x90+0+0')
    question7_win.resizable(False,False)
    question7_win.title('F1 2025 Quiz - Q7')

    question7_label = tk.Label(
        question7_win,
        text='How many points seperated Norris and Verstappen?',
        font=('Arial',20)
    )
    question7_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question7_button_a = tk.Button(
        question7_win,
        text='10',
        font=('Arial'),
        width=15,
        command=q7_incorrect
    )
    question7_button_a.grid(
        row=3,
        column=1
    )

    question7_button_b = tk.Button(
        question7_win,
        text='2',
        font=('Arial'),
        width=15,
        command=q7_correct
    )
    question7_button_b.grid(
        row=3,
        column=2
    )

    question7_button_c = tk.Button(
        question7_win,
        text='15',
        font=('Arial'),
        width=15,
        command=q7_incorrect
    )
    question7_button_c.grid(
        row=4,
        column=1
    )

    question7_button_d = tk.Button(
        question7_win,
        text='7',
        font=('Arial'),
        width=15,
        command=q7_incorrect
    )
    question7_button_d.grid(
        row=4,
        column=2
    )

    question6_win.destroy()


def question6():
    def q6_correct():
        correct()
        question7()

    def q6_incorrect():
        messagebox.showinfo('Result',"Incorrect, The answer is Ferrari")
        question7()

    global question6_win

    question6_win = Toplevel()
    question6_win.geometry('320x90+0+0')
    question6_win.resizable(False,False)
    question6_win.title('F1 2025 Quiz - Q6')

    question6_label = tk.Label(
        question6_win,
        text="Which team was 2nd in the Constructors' Championship",
        font=('Arial')
    )
    question6_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question6_button_a = tk.Button(
        question6_win,
        text='Ferrari',
        font=('Arial'),
        width=15,
        command=q6_correct
    )
    question6_button_a.grid(
        row=3,
        column=1
    )

    question6_button_b = tk.Button(
        question6_win,
        text='Mercedes',
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
        text='Red Bull Racing',
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
        text='Williams',
        font=('Arial'),
        width=15,
        command=q6_incorrect
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
        messagebox.showinfo('Result','Incorrect, The answer is Oscar Piastri')
        question6()

    global question5_win

    question5_win = Toplevel()
    question5_win.geometry('320x90+0+0')
    question5_win.resizable(False,False)
    question5_win.title('F1 2025 Quiz - Q6')

    question5_label = tk.Label(
        question5_win,
        text="Who was 3rd in the Driver's Championship?",
        font=('Arial',20)
    )
    question5_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question5_button_a = tk.Button(
        question5_win,
        text='Oscar Piastri',
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
        text='Lewis Hamilton',
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
        text='Fernando Alonso',
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
        text='Alex Albon',
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
        messagebox.showinfo('Result','Incorrect, The answer is Max Verstappen')
        question5()

    global question4_win

    question4_win = Toplevel()
    question4_win.geometry('320x90+0+0')
    question4_win.resizable(False,False)
    question4_win.title('F1 2025 Quiz - Q4')

    question4_label = tk.Label(
        question4_win,
        text="Who was 2nd in the Driver's Championship?",
        font=('Arial',20)
    )
    question4_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question4_button_a = tk.Button(
        question4_win,
        text='Charles Leclerc',
        font=('Arial'),
        width=15,
        command=q4_incorrect
    )
    question4_button_a.grid(
        row=3,
        column=1
    )

    question4_button_b = tk.Button(
        question4_win,
        text='Max Verstappen',
        font=('Arial'),
        width=15,
        command=q4_correct
    )
    question4_button_b.grid(
        row=3,
        column=2
    )

    question4_button_c = tk.Button(
        question4_win,
        text='Oscar Piastri',
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
        text='George Russell',
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
        messagebox.showinfo('Result','Incorrect, The answer is Abu Dhabi GP')
        question4

    global question3_win

    question3_win = Toplevel()
    question3_win.geometry('320x90+0+0')
    question3_win.resizable(False,False)
    question3_win.title('F1 2025 Quiz - Q3')

    question3_label = tk.Label(
        question3_win,
        text="Which race did Lando Norris win the 2025 Driver's Title?",
        font=('Arial',20)
    )
    question3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question3_button_a = tk.Button(
        question3_win,
        text='Monaco GP',
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
        text='Abu Dhabi GP',
        font=('Arial'),
        width=15,
        command=q3_correct
    )
    question3_button_b.grid(
        row=3,
        column=2
    )

    question3_button_c = tk.Button(
        question3_win,
        text='Italian GP',
        font=('Arial'),
        width=15,
        command=q3_incorrect
    )
    question3_button_c.grid(
        row=4,
        column=1
    )

    question3_button_d = tk.Button(
        question3_win,
        text='British GP',
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
        messagebox.showinfo('Result','Incorrect, The answer is McLaren')
        question3

    global question2_win

    question2_win = Toplevel()
    question2_win.geometry('320x90+0+0')
    question2_win.resizable(False,False)
    question2_win.title('F1 2025 Quiz - Q2')

    question2_button_a = tk.Button(
        question2_win,
        text='Mercedes',
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
        text='Ferrari',
        font=('Arial'),
        width=15,
        command=q2_incorrect
    )
    question2_button_b.grid(
        row=3,
        column=2
    )

    question2_button_c = tk.Button(
        question2_win,
        text='Red Bull Racing',
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
        text='McLaren',
        font=('Arial'),
        width=15,
        command=q2_correct
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
        messagebox.showinfo('Result','Incorrect, The answer is Lando Norris')
        question2()

    global question1_win

    question1_win = Toplevel()
    question1_win.geometry('320x90+0+0')
    question1_win.resizable(False,False)
    question1_win.title('F1 2025 Quiz - Q1')

    question1_label = tk.Label(
        question1_win,
        text="Who won the Driver's Championship?",
        font=('Arial',20)
    )
    question1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question1_button_a = tk.Button(
        question1_win,
        text='Max Verstappen',
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
        text='Oscar Piastri',
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
        text='Lando Norris',
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
        text='George Russell',
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
    score += 1
    messagebox.showinfo('Result','Correct!')
    return

root = tk.Tk()
root.geometry('150x60+0+0')
root.resizable(False,False)
root.title('F1 2025 Quiz')

root_title = tk.Label(
    root,
    text='F1 2025 Quiz',
    font=('Arial',20,'bold')
)
root_title.pack()

start_button = tk.Button(
    root,
    text='Start Quiz',
    font=('Arial'),
    width=20
)
start_button.pack()

root.mainloop()