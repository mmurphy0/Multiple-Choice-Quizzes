import tkinter as tk
from tkinter import messagebox, Toplevel
from time import strftime

def question18(question17_win):
    def q18_correct():
        correct()
        question19(question18_win)

    def q18_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is False')
        question19(question18_win)

    question18_win = Toplevel()
    question18_win.geometry('380x50+0+0')
    question18_win.resizable(False,False)
    question18_win.title('Oasis Quiz - Q18')

    q18_label = tk.Label(
        question18_win,
        text="Be Here Now is Oasis' best-selling album",
        font=('Arial',20)
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
        command=q18_incorrect
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
        command=q18_correct
    )
    q18_button_b.grid(
        row=3,
        column=2
    )

    question17_win.destroy()

def question17(question16_win):
    def q17_correct():
        correct()
        question18(question17_win)

    def q17_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Half the World Away')
        question18(question17_win)
    
    question17_win = Toplevel()
    question17_win.geometry('380x90+0+0')
    question17_win.resizable(False,False)
    question17_win.title('Oasis Quiz - Q17')

    q17_label = tk.Label(
        question17_win,
        text='Which song was used for The Royle Family?',
        font=('Arial',20)
    )
    q17_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q17_button_a = tk.Button(
        question17_win,
        text='Half the World Away',
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
        text='Live Forever',
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
        text='Whatever',
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
        text="Don't Look Back in Anger",
        font=('Arial'),
        width=15,
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
        messagebox.showinfo('Result','Incorrect, The answer is Be Here Now')
        question17(question16_win)

    question16_win = Toplevel()
    question16_win.geometry('380x90+0+0')
    question16_win.resizable(False,False)
    question16_win.title('Oasis Quiz - Q16')

    q16_label = tk.Label(
        question16_win,
        text='Which album was released in 1997?',
        font=('Arial',20)
    )
    q16_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q16_button_a = tk.Button(
        question16_win,
        text='Definitely Maybe',
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
        text="(What's The Story) Morning Glory?",
        font=('Arial'),
        width=15,
        command=q16_incorrect
    )
    q16_button_b.grid(
        row=3,
        column=2
    )

    q16_button_c = tk.Button(
        question16_win,
        text='Standing on the Shoulder of Giants',
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
        text='Be Here Now',
        font=('Arial'),
        width=15,
        command=q16_correct
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
        messagebox.showinfo('Result','Incorrect, The answer is Paul Arthurs')
        question16(question15_win)

    question15_win = Toplevel()
    question15_win.geometry('380x90+0+0')
    question15_win.resizable(False,False)
    question15_win.title('Oasis Quiz - Q15')

    q15_label = tk.Label(
        question15_win,
        text='Who was known as "Bonehead"?',
        font=('Arial',20),
    )
    q15_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q15_button_a = tk.Button(
        question15_win,
        text='Gem Archer',
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
        text='Andy Bell',
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
        text='Paul Arthurs',
        font=('Arial'),
        width=15,
        command=q15_correct
    )
    q15_button_c.grid(
        row=4,
        column=1
    )

    q15_button_d = tk.Button(
        question15_win,
        text='Johnny Marr',
        font=('Arial'),
        width=15,
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
        messagebox.showinfo('Result','Incorrect, The answer is False')
        question15(question14_win)

    question14_win = Toplevel()
    question14_win.geometry('380x90+0+0')
    question14_win.resizable(False,False)
    question14_win.title('Oasis Quiz - Q14')

    q14_label = tk.Label(
        question14_win,
        text='Did Andy Bell join before Definitely Maybe?',
        font=('Arial',20)
    )
    q14_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q14_button_a = tk.Button(
        question14_win,
        text='True',
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
        text='False',
        font=('Arial'),
        width=15,
        command=q14_correct
    )
    q14_button_b.grid(
        row=3,
        column=2
    )

    question13_win.destroy()

def question13(question12_win):
    def q13_correct():
        correct()
        question14(question13_win)
    
    def q13_incorrect():
        messagebox.showinfo('Result',"Incorrect, The answer is (What's the story) Morning Glory")
        question14(question13_win)

    question13_win = Toplevel()
    question13_win.geometry('380x90+0+0')
    question13_win.resizable(False,False)
    question13_win.title('Oasis Quiz - Q14')

    q13_label = tk.Label(
        question13_win,
        text='Which album is Champagne Supernova from?',
        font=('Arial',20)
    )
    q13_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q13_button_a = tk.Button(
        question13_win,
        text='Be Here Now',
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
        text='Definitely Maybe',
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
        text='Heathen Chemistry',
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
        text="(What's the Story) Morning Glory?",
        font=('Arial'),
        width=15,
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
        messagebox.showinfo('Result','Incorrect, The answer is Roll With It')
        question13(question12_win)

    question12_win = Toplevel()
    question12_win.geometry('380x90+0+0')
    question12_win.resizable(False,False)
    question12_win.title('Oasis Quiz - Q12')

    q12_label = tk.Label(
        question12_win,
        text='Which song has the lyrics "You gotta roll with it"?',
        font=('Arial',20),
    )
    q12_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q12_button_a = tk.Button(
        question12_win,
        text='Morning Glory',
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
        text='Cigarettes & Alcohol',
        font=('Arial'),
        width=15,
        command=q12_incorrect
    )
    q12_button_b.grid(
        row=3,
        column=2
    )

    q12_button_c = tk.Button(
        question12_win,
        text='Roll With It',
        font=('Arial'),
        width=15,
        command=q12_correct
    )
    q12_button_c.grid(
        row=4,
        column=1
    )

    q12_button_d = tk.Button(
        question12_win,
        text='Shakermaker',
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
        messagebox.showinfo('Result',"Incorrect, The answer is Rock 'n' Roll Star")
        question12(question11_win)

    question11_win = Toplevel()
    question11_win.geometry('380x90+0+0')
    question11_win.resizable(False,False)
    question11_win.title('Oasis Quiz - Q11')

    q11_label = tk.Label(
        question11_win,
        text='Which song opens Definitely Maybe?',
        font=('Arial',20)
    )
    q11_label.grid(
        row=1,
        column=2,
        columnspan=2
    )

    q11_button_a = tk.Button(
        question11_win,
        text='Supersonic',
        font=('Arial'),
        width=15,
        command=q11_incorrect
    )
    q11_button_a.grid(
        row=3,
        column=1
    )

    q11_button_b = tk.Button(
        question11_win,
        text="Rock 'n' Roll Star",
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
        text='Columbia',
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
        text='Bring it on Down',
        font=('Arial'),
        width=15,
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
        messagebox.showinfo('Result','Incorrect, The answer is True')
        question11(question10_win)
    
    question10_win = Toplevel()
    question10_win.geometry('380x90+0+0')
    question10_win.resizable(False,False)
    question10_win.title('Oasis Quiz - Q10')

    q10_label = tk.Label(
        question10_win,
        text='Did Oasis play 2 nights at Knebworth in 1996?',
        font=('Arial',20)
    )
    q10_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q10_button_a = tk.Button(
        question10_win,
        text='True',
        font=('Arial'),
        width=15,
        command=q10_correct
    )
    q10_button_a.grid(
        row=3,
        column=2
    )

    q10_button_b = tk.Button(
        question10_win,
        text='False',
        font=('Arial'),
        width=15,
        command=q10_incorrect
    )
    q10_button_b.grid(
        row=3,
        column=2
    )

    question9_win.destroy()

def question9(question8_win):
    def q9_correct():
        correct()
        question10(question9_win)

    def q9_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Guitar')
        question10(question9_win)

    question9_win = Toplevel()
    question9_win.geometry('380x90+0+0')
    question9_win.resizable(False,False)
    question9_win.title('Oasis Quiz - Q10')

    q9_label = tk.Label(
        question9_win,
        text='Which instrument did Noel Gallagher mainly play?',
        font=('Arial',20)
    )
    q9_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q9_button_a = tk.Button(
        question9_win,
        text='Drums',
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
        text='Bass',
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
        text='Guitar',
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
        text='Keyboard',
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
        messagebox.showinfo('Result','Incorrect, The answer is Some Might Say')
        question9(question8_win)

    question8_win = Toplevel()
    question8_win.geometry('380x90+0+0')
    question8_win.resizable(False,False)
    question8_win.title('Oasis Quiz - Q8')

    q8_label = tk.Label(
        question8_win,
        text='Which song was their 1st UK number 1?',
        font=('Arial',20)
    )
    q8_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q8_button_a = tk.Button(
        question8_win,
        text='Some Might Say',
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
        text='Supersonic',
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
        text='Live Forever',
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
        text='Wonderwall',
        font=('Arial'),
        width=15,
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
        messagebox.showinfo('Result','Incorrect, The answer is Liam Gallagher')
        question8(question7_win)

    question7_win = Toplevel()
    question7_win.geometry('380x90+0+0')
    question7_win.resizable(False,False)
    question7_win.title('Oasis Quiz - Q7')

    q7_label = tk.Label(
        question7_win,
        text='Who was the lead singer of Oasis?',
        font=('Arial',20)
    )
    q7_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q7_button_a = tk.Button(
        question7_win,
        text='Noel Gallagher',
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
        text='Liam Gallagher',
        font=('Arial'),
        width=15,
        command=q7_correct
    )
    q7_button_b.grid(
        row=3,
        column=2
    )

    q7_button_c = tk.Button(
        question7_win,
        text='Paul Arthurs',
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
        text='Andy Bell',
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
        messagebox.showinfo('Result','Incorrect, The answer is True')
        question7(question6_win)

    question6_win = Toplevel()
    question6_win.geometry('380x50+0+0')
    question6_win.resizable(False,False)
    question6_win.title('Oasis Quiz - Q6')

    q6_label = tk.Label(
        question6_win,
        text='Did Noel Gallagher write the majority of Oasis songs?',
        font=('Arial',20)
    )
    q6_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q6_button_a = tk.Button(
        question6_win,
        text='True',
        font=('Arial'),
        width=15,
        command=q6_correct
    )
    q6_button_a.grid(
        row=3,
        column=1
    )

    q6_button_b = tk.Button(
        question6_win,
        text='False',
        font=('Arial'),
        width=15,
        command=q6_incorrect
    )
    q6_button_b.grid(
        row=3,
        column=2
    )

    question5_win.destroy()

def question5(question4_win):
    def q5_correct():
        correct()
        question6(question5_win)

    def q5_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Tony McCarroll')
        question6(question5_win)

    question5_win = Toplevel()
    question5_win.geometry('380x90+0+0')
    question5_win.resizable(False,False)
    question5_win.title('Oasis Quiz - Q5')

    q5_label = tk.Label(
        question5_win,
        text="Who was Oasis' original drummer?",
        font=('Arial'),
    )
    q5_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q5_button_a = tk.Button(
        question5_win,
        text='Alan White',
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
        text='Zak Starkey',
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
        text='Chris Sharrock',
        font=('Arial'),
        width=15,
        command=q5_incorrect
    )
    q5_button_c.grid(
        row=4,
        column=1
    )

    q5_button_d = tk.Button(
        question5_win,
        text='Tony McCarroll',
        font=('Arial'),
        width=15,
        command=q5_correct
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
        messagebox.showinfo('Result','Incorrect, The answer is Definitely Maybe')
        question5(question4_win)

    question4_win = Toplevel()
    question4_win.geometry('380x90+0+0')
    question4_win.resizable(False,False)
    question4_win.title('Oasis Quiz - Q4')

    q4_label = tk.Label(
        question4_win,
        text="What was Oasis' debut album?",
        font=('Arial',20)
    )
    q4_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q4_button_a = tk.Button(
        question4_win,
        text='Definitely Maybe',
        font=('Arial'),
        width=15,
        command=q4_correct
    )
    q4_button_a.grid(
        row=3,
        column=1
    )

    q4_button_b = tk.Button(
        question4_win,
        text='Be Here Now',
        font=('Arial'),
        width=15,
        command=q4_incorrect
    )
    q4_button_b.grid(
        row=3,
        column=2
    )

    q4_button_c = tk.Button(
        question4_win,
        text="(What's the story) Morning Glory?",
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
        text='Standing on the Shoulder of Giants',
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

    def q3_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Manchester')
        question4(question3_win)

    question3_win = Toplevel()
    question3_win.geometry('380x90+0+0')
    question3_win.resizable(False,False)
    question3_win.title('Oasis Quiz - Q3')

    q3_label = tk.Label(
        question3_win,
        text='Which city did they originate from?',
        font=('Arial',20)
    )
    q3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q3_button_a = tk.Button(
        question3_win,
        text='Liverpool',
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
        text='Sheffield',
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
        text='Manchester',
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
        text='London',
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
    question2_win.geometry('380x50+0+0')
    question2_win.resizable(False,False)
    question2_win.title('Oasis Quiz - Q2')

    q2_label = tk.Label(
        question2_win,
        text='Did Oasis Reunite?',
        font=('Arial',20),
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
        messagebox.showinfo('Result','Incorrect, The answer is 1991')
        question2(question1_win)

    question1_win = Toplevel()
    question1_win.geometry('380x90+0+0')
    question1_win.resizable(False,False)
    question1_win.title('Oasis Quiz - Q1')

    q1_label = tk.Label(
        question1_win,
        text='What year were Oasis formed?',
        font=('Arial'),
    )
    q1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    q1_button_a = tk.Button(
        question1_win,
        text='1988',
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
        text='1991',
        font=('Arial'),
        width=15,
        command=q1_correct
    )
    q1_button_b.grid(
        row=3,
        column=2
    )

    q1_button_c = tk.Button(
        question1_win,
        text='1993',
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
        text='1990',
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

score = 0

root = tk.Tk()
root.geometry('150x60+0+0')
root.resizable(False,False)
root.title('Oasis Quiz')

root_label = tk.Label(
    root,
    text='Oasis Quiz',
    font=('Arial',20,'bold')
)
root_label.pack()

startquiz_button = tk.Button(
    root,
    text='Start',
    font=('Arial'),
    width=20,
    command=question1
)
startquiz_button.pack()

root.mainloop()