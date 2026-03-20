import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

import time
from time import strftime

def question15(question14_win):
    def q15_correct():
        correct()
        question16(question15_win)

    def q15_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is False')
        question16(question15_win)

    question15_win = Toplevel()
    question15_win.geometry('+0+0')
    question15_win.resizable(False,False)
    question15_win.title('The Office (US) Quiz - Q15')

    q15_label = tk.Label(
        question15_win,
        text='Stanley Hudson enjoys participating in meetings',
        font=('Arial',20)
    )
    q15_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q15_button_a = tk.Button(
        question15_win,
        text='True',
        font=('Arial'),
        width=15,
        command=q15_incorrect
    )
    q15_button_a.grid(
        row=3,
        column=1
    )

    q15_button_b = tk.Button(
        question15_win,
        text='False',
        font=('Arial'),
        width=15,
        command=q15_correct
    )
    q15_button_b.grid(
        row=3,
        column=2
    )

    question14_win.destroy()

def question14(question13_win):
    def q14_correct():
        correct()
        question15(question14_win)

    def q14_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Threat Level Midnight')
        question15(question14_win)

    question14_win = Toplevel()
    question14_win.geometry('+0+0')
    question14_win.resizable(False,False)
    question14_win.title('The Office (US) Quiz - Q14')

    q14_label = tk.Label(
        question14_win,
        text="What is Michael Scott's movie called?",
        font=('Arial',20)
    )
    q14_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q14_button_a = tk.Button(
        question14_win,
        text='Scranton Justice',
        font=('Arial'),
        width=15,
        command=q14_incorrect
    )
    q14_button_a.grid(
        row=3,
        column=1
    )

    q14_button_b = tk.Button(
        question14_win,
        text='Secret Agent Michael',
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
        text='Threat Level Midnight',
        font=('Arial'),
        width=15,
        command=q14_correct
    )
    q14_button_c.grid(
        row=4,
        column=1
    )

    q14_button_d = tk.Button(
        question14_win,
        text='Agent Scarn',
        font=('Arial'),
        width=15,
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
        messagebox.showinfo('Resukt','Incorrect, The answer is Deangelo Vickers')
        question14(question13_win)

    question13_win = Toplevel()
    question13_win.geometry('+0+0')
    question13_win.resizable(False,False)
    question13_win.title('The Office (US) Quiz - Q13')

    q13_label = tk.Label(
        question13_win,
        text='Who becomes regional manager after Michael?',
        font=('Arial',20)
    )
    q13_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q13_button_a = tk.Button(
        question13_win,
        text='Deangelo Vickers',
        font=('Arial'),
        width=15,
        command=q13_correct
    )
    q13_button_a.grid(
        row=3,
        column=1
    )

    q13_button_b = tk.Button(
        question13_win,
        text='Andy Bernard',
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
        text='Jim Halpert',
        font=('Arial'),
        width=15,
        command=q13_incorrect
    )
    q13_button_c.grid(
        row=4,
        column=1
    )

    q13_button_d = tk.Button(
        question13_win,
        text='Dwight Schrute',
        font=('Arial'),
        width=15,
        command=q13_incorrect
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
        messagebox.showinfo('Result',"Incorrect, The answer is Poor Richard's")
        question13(question12_win)

    question12_win = Toplevel()
    question12_win.geometry('+0+0')
    question12_win.resizable(False,False)
    question12_win.title('The Office (US) Quiz - Q12')

    q12_label = tk.Label(
        question12_win,
        text='Which bar do the staff often visit?',
        font=('Arial',20)
    )
    q12_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q12_button_a = tk.Button(
        question12_win,
        text='The Electric City Bar',
        font=('Arial'),
        width=15,
        command=q12_incorrect
    )
    q12_button_a.grid(
        row=3,
        column=1
    )

    q12_button_b = tk.Button(
        question12_win,
        text="Poor Richard's",
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
        text='Scranton Pub',
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
        text='The Paper Mill',
        font=('Arial'),
        width=15,
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
        messagebox.showinfo('Result','Incorrect, The answer is True')
        question12(question11_win)

    question11_win = Toplevel()
    question11_win.geometry('+0+0')
    question11_win.resizable(False,False)
    question11_win.title('The Office (US) Quiz - Q11')

    q11_label = tk.Label(
        question11_win,
        text='Ryan Howard is a temp at the start of the show?',
        font=('Arial',20)
    )
    q11_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q11_button_a = tk.Button(
        question11_win,
        text='True',
        font=('Arial'),
        width=15,
        command=q11_correct
    )
    q11_button_a.grid(
        row=3,
        column=1
    )

    q11_button_b = tk.Button(
        question11_win,
        text='False',
        font=('Arial'),
        width=15,
        command=q11_incorrect
    )
    q11_button_b.grid(
        row=3,
        column=2
    )

    question10_win.destroy()

def question10(question9_win):
    def q10_correct():
        correct()
        question11(question10_win)

    def q10_incorrect():
        messagebox.showinfo('Result', 'Incorrect, The answer is chili')
        question11(question10_win)

    question10_win = Toplevel()
    question10_win.geometry('+0+0')
    question10_win.resizable(False,False)
    question10_win.title('The Office (US) Quiz - Q10')

    q10_label = tk.Label(
        question10_win,
        text='What food did Kevin Malone spill?',
        font=('Arial',20)
    )
    q10_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q10_button_a = tk.Button(
        question10_win,
        text='Soup',
        font=('Arial'),
        width=15,
        command=q10_incorrect
    )
    q10_button_a.grid(
        row=3,
        column=1
    )

    q10_button_b = tk.Button(
        question10_win,
        text='Stew',
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
        text='Spaghetti',
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
        text='Chili',
        font=('Arial'),
        width=15,
        command=q10_correct
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
        correct()
        question10(question9_win)

    question9_win = Toplevel()
    question9_win.geometry('+0+0')
    question9_win.resizable(False,False)
    question9_win.title('The Office (US) Quiz - Q9')

    q9_label = tk.Label(
        question9_win,
        text='Which character said "Bears. Beets. Battlestar Galactica"?',
        font=('Arial',20)
    )
    q9_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q9_button_a = tk.Button(
        question9_win,
        text='Dwight Schrute',
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
        text='Creed Bratton',
        font=('Arial'),
        width=15,
        command=q9_incorrect
    )
    q9_button_b.grid(
        row=3,
        column=2
    )

    q9_button_c = tk.Button(
        question9_win,
        text='Jim Halpert',
        font=('Arial'),
        width=15,
        command=q9_correct
    )
    q9_button_c.grid(
        row=4,
        column=1
    )

    q9_button_d = tk.Button(
        question9_win,
        text='Michael Scott',
        font=('Arial'),
        width=15,
        command=q9_incorrect
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
        messagebox.showinfo('Result','Incorrect, The answer is True')
        question9(question8_win)

    question8_win = Toplevel()
    question8_win.geometry('+0+0')
    question8_win.resizable(False,False)
    question8_win.title('The Office (US) Quiz - Q8')

    q8_label = tk.Label(
        question8_win,
        text='Kelly Kapoor works in Customer Service?',
        font=('Arial',20)
    )
    q8_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q8_button_a = tk.Button(
        question8_win,
        text='True',
        font=('Arial'),
        width=15,
        command=q8_correct
    )
    q8_button_a.grid(
        row=3,
        column=1
    )

    q8_button_b = tk.Button(
        question8_win,
        text='False',
        font=('Arial'),
        width=15,
        command=q8_incorrect
    )
    q8_button_b.grid(
        row=3,
        column=2
    )

    question7_win.destroy()

def question7(question6_win):
    def q7_correct():
        correct()
        question8(question7_win)

    def q7_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Stamford')
        question8(question7_win)

    question7_win = Toplevel()
    question7_win.geometry('+0+0')
    question7_win.resizable(False,False)
    question7_win.title('The Office (US) Quiz - Q7')

    q7_label = tk.Label(
        question7_win,
        text='Jim Halpert transferred to which branch in Season 3?',
        font=('Arial',20)
    )
    q7_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q7_button_a = tk.Button(
        question7_win,
        text='Stamford',
        font=('Arial'),
        width=15,
        command=q7_correct
    )
    q7_button_a.grid(
        row=3,
        column=1
    )

    q7_button_b = tk.Button(
        question7_win,
        text='Utica',
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
        text='Buffalo',
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
        text='Nashua',
        font=('Arial'),
        width=15,
        command=q7_incorrect
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
        messagebox.showinfo('Result','Incorrect, The answer is Roy Anderson')
        question7(question6_win)

    question6_win = Toplevel()
    question6_win.geometry('+0+0')
    question6_win.resizable(False,False)
    question6_win.title('The Office (US) Quiz - Q6')

    q6_label = tk.Label(
        question6_win,
        text="What is the name of Pam's fiancé in early seasons",
        font=('Arial',20)
    )
    q6_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q6_button_a = tk.Button(
        question6_win,
        text='Gabe Lewis',
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
        text='Todd Packer',
        font=('Arial'),
        width=15,
        command=q6_incorrect
    )
    q6_button_b.grid(
        row=3,
        column=2
    )

    q6_button_c = tk.Button(
        question6_win,
        text='Bob Vance',
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
        text='Roy Anderson',
        font=('Arial'),
        width=15,
        command=q6_correct
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
        messagebox.showinfo('Result','Incorrect, The answer is True')
        question6(question5_win)

    question5_win = Toplevel()
    question5_win.geometry('+0+0')
    question5_win.resizable(False,False)
    question5_win.title('The Office (US) Quiz - Q5')

    q5_label = tk.Label(
        question5_win,
        text='Angela Martin is a vegetarian?',
        font=('Arial',20)
    )
    q5_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q5_button_a = tk.Button(
        question5_win,
        text='True',
        font=('Arial'),
        width=15,
        command=q5_correct
    )
    q5_button_a.grid(
        row=3,
        column=1
    )

    q5_button_b = tk.Button(
        question5_win,
        text='False',
        width=15,
        command=q5_incorrect
    )
    q5_button_b.grid(
        row=3,
        column=2
    )

    question4_win.destroy()

def question4(question3_win):
    def q4_correct():
        correct()
        question5(question4_win)
    
    def q4_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Banjo')
        question5(question4_win)
    
    question4_win = Toplevel()
    question4_win.geometry('+0+0')
    question4_win.resizable(False,False)
    question4_win.title('The Office (US) Quiz - Q4')

    q4_label = tk.Label(
        question4_win,
        text='Which instrument does Andy Bernard often play?',
        font=('Arial',20)
    )
    q4_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q4_button_a = tk.Button(
        question4_win,
        text='Piano',
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
        text='Banjo',
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
        text='Violin',
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
        text='Guitar',
        font=('Arial'),
        width=15,
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

    def q3_incorrect(question2_win):
        messagebox.showinfo('Result','Incorrect, The answer is Michael Scott')
        question4(question3_win)

    question3_win = Toplevel()
    question3_win.geometry('+0+0')
    question3_win.resizable(False,False)
    question3_win.title('The Office (US) Quiz - Q3')

    q3_label = tk.Label(
        question3_win,
        text='Who is the Regional Manager at the start of the show?',
        font=('Arial',20)
    )
    q3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q3_button_a = tk.Button(
        question3_win,
        text='Michael Scott',
        font=('Arial'),
        width=15,
        command=q3_correct
    )
    q3_button_a.grid(
        row=3,
        column=1
    )

    q3_button_b = tk.Button(
        question3_win,
        text='Dwight Schrute',
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
        text='Jim Halpert',
        font=('Arial'),
        width=15,
        command=q3_incorrect
    )
    q3_button_c.grid(
        row=4,
        column=1
    )

    q3_button_d = tk.Button(
        question3_win,
        text='Andy Bernard',
        font=('Arial'),
        width=15,
        command=q3_incorrect
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
        messagebox.showinfo('Result','Incorrect, The answer is True')
        question3(question2_win)

    question2_win = Toplevel()
    question2_win.geometry('+0+0')
    question2_win.resizable(False,False)
    question2_win.title('The Office (US) Quiz - Q2')

    q2_label = tk.Label(
        question2_win,
        text='Dwight Schrute owns a large beet farm?',
        font=('Arial',20)
    )
    q2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q2_button_a = tk.Button(
        question2_win,
        text='True',
        font=('Arial'),
        width=15,
        command=q2_correct
    )
    q2_button_a.grid(
        row=3,
        column=1
    )

    q2_button_b = tk.Button(
        question2_win,
        text='False',
        font=('Arial'),
        width=15,
        command=q2_incorrect
    )
    q2_button_b.grid(
        row=3,
        column=2
    )

    question1_win.destroy()

def question1():
    def q1_correct():
        correct()
        question2(question1_win)

    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Dunder Mifflin')
        question2(question1_win)

    question1_win = Toplevel()
    question1_win.geometry('+0+0')
    question1_win.resizable(False,False)
    question1_win.title('The Office (US) Quiz - Q1')

    q1_label = tk.Label(
        question1_win,
        text='What is the name of the paper company?',
        font=('Arial',20)
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = tk.Button(
        question1_win,
        text='Penn Paper',
        font=('Arial'),
        width=15,
        command=q1_incorrect
    )
    q1_button_a.grid(
        row=3,
        column=1
    )

    q1_button_b = tk.Button(
        question1_win,
        text='Scranton Paper Co.',
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
        text='Dunder Mifflin',
        font=('Arial'),
        width=15,
        command=q1_correct
    )
    q1_button_c.grid(
        row=4,
        column=1
    )

    q1_button_d = tk.Button(
        question1_win,
        text='Northeast Paper',
        font=('Arial'),
        width=15,
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

root_win = tk.Tk()
root_win.geometry('')
root_win.resizable(False,False)
root_win.title('The Office (US) Quiz')

root_label = tk.Label(
    root_win,
    text='The Office (US) Quiz',
    font=('Arial',20,'bold')
)
root_label.pack()

startquiz_button = tk.Button(
    root_win,
    text='Start',
    font=('Arial'),
    width=20,
    command=question1
)
startquiz_button.pack()

root_win.mainloop()