import tkinter as tk
from tkinter import messagebox, Toplevel
from time import strftime

score = int(0)

def save():
    def reset():
        global score
        score = 0
        results_win.destroy()
    
    time = strftime('%H:%M:%S &D')

    with open('UK Capitals Quiz/scorebook.txt','a') as file:
        file.write(str(time) + '\n' + (f'Score: {score}/5') + '\n' + '--------------------' + '\n')
        messagebox.showinfo('Confirmation','Results saved successfully')
    
    reset()


def results():
    global results_win

    results_win = Toplevel()
    results_win.geometry('200x82+0+0')
    results_win.resizable(False,False)
    results_win.title('UK Capitals Quiz - Results')

    results_title = tk.Label(
        results_win,
        text='Results',
        font=('Arial',20,'bold')
    )
    results_title.pack()

    results_display = tk.Label(
        results_win,
        text=(f'Score: {score}/5'),
        font=('Arial',15)
    )
    results_display.pack()

    continue_button = tk.Button(
        results_win,
        text='Continue',
        width=20,
        command=save
    )
    continue_button.pack()

    question5_win.destroy()


def question_5():
    def q5_correct():
        correct()
        results()

    def q5_incorrect():
        messagebox.showinfo('Incorrect','The Answer is Dublin')
        results()

    global question5_win

    question5_win = Toplevel()
    question5_win.geometry('270x90+0+0')
    question5_win.resizable(False,False)
    question5_win.title('UK Capitals Quiz - Question 5')

    question5_label = tk.Label(
        question5_win,
        text='What is the capital of Ireland?',
        font=('Arial',20)
    )
    question5_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question5_button_a = tk.Button(
        question5_win,
        text='Limerick',
        font=('Arial'),
        width=10,
        command=q5_incorrect
    )
    question5_button_a.grid(
        row=3,
        column=1
    )

    question5_button_b = tk.Button(
        question5_win,
        text='Cork',
        font=('Arial'),
        width=10,
        command=q5_incorrect
    )
    question5_button_b.grid(
        row=3,
        column=2
    )

    question5_button_c = tk.Button(
        question5_win,
        text='Galway',
        font=('Arial'),
        width=10,
        command=q5_incorrect
    )
    question5_button_c.grid(
        row=4,
        column=1
    )

    question5_button_d = tk.Button(
        question5_win,
        text='Dublin',
        font=('Arial'),
        width=10,
        command=q5_correct
    )
    question5_button_d.grid(
        row=4,
        column=2
    )

    question4_win.destroy()


def question_4():
    def q4_correct():
        correct()
        question_5()

    def q4_incorrect():
        messagebox.showinfo('Incorrect','The answer is Belfast')
        question_5()

    global question4_win

    question4_win = Toplevel()
    question4_win.geometry('352x90+0+0')
    question4_win.resizable(False,False)
    question4_win.title('UK Capitals Quiz - Question 4')

    question4_label = tk.Label(
        question4_win,
        text='What is the capital of Northern Ireland?',
        font=('Arial',20)
    )
    question4_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question4_button_a = tk.Button(
        question4_win,
        text='Belfast',
        font=('Arial'),
        width=10,
        command=q4_correct
    )
    question4_button_a.grid(
        row=3,
        column=1
    )

    question4_button_b = tk.Button(
        question4_win,
        text='Londonderry',
        font=('Arial'),
        width=10,
        command=q4_incorrect
    )
    question4_button_b.grid(
        row=3,
        column=2
    )

    question4_button_c = tk.Button(
        question4_win,
        text='Lisburn',
        font=('Arial'),
        width=10,
        command=q4_incorrect
    )
    question4_button_c.grid(
        row=4,
        column=1
    )

    question4_button_d = tk.Button(
        question4_win,
        text='Newtownabbey',
        font=('Arial'),
        width=10,
        command=q4_incorrect
    )
    question4_button_d.grid(
        row=4,
        column=2
    )

    question3_win.destroy()


def question_3():
    def q3_correct():
        correct()
        question_4()

    def q3_incorrect():
        messagebox.showinfo('Incorrect','The answer is Edinburgh')
        question_4()

    global question3_win

    question3_win = Toplevel()
    question3_win.geometry('285x90+0+0')
    question3_win.resizable(False,False)
    question3_win.title('UK Capitals Quiz - Question 3')

    question3_label = tk.Label(
        question3_win,
        text='What is the capital of Scotland?',
        font=('Arial',20)
    )
    question3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question3_button_a = tk.Button(
        question3_win,
        text='Glasgow',
        font=('Arial'),
        width=10,
        command=q3_incorrect
    )
    question3_button_a.grid(
        row=3,
        column=1
    )

    question3_button_b = tk.Button(
        question3_win,
        text='Edinburgh',
        font=('Arial'),
        width=10,
        command=q3_correct
    )
    question3_button_b.grid(
        row=3,
        column=2
    )

    question3_button_c = tk.Button(
        question3_win,
        text='Aberdeen',
        font=('Arial'),
        width=10,
        command=q3_incorrect
    )
    question3_button_c.grid(
        row=4,
        column=1
    )

    question3_button_d = tk.Button(
        question3_win,
        text='Inverness',
        font=('Arial'),
        width=10,
        command=q3_incorrect
    )
    question3_button_d.grid(
        row=4,
        column=2
    )

    question2_win.destroy()


def question_2():
    def q2_correct():
        correct()
        question_3()
    
    def q2_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Cardiff')
        question_3()

    global question2_win

    question2_win = Toplevel()
    question2_win.geometry('265x90+0+0')
    question2_win.resizable(False,False)
    question2_win.title('UK Capitals Quiz - Question 2')

    question2_label = tk.Label(
        question2_win,
        text='What is the capital of Wales?',
        font=('Arial',20)
    )
    question2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question2_button_a = tk.Button(
        question2_win,
        text='Swansea',
        font=('Arial'),
        width=10,
        command=q2_incorrect
    )
    question2_button_a.grid(
        row=3,
        column=1
    )

    question2_button_b = tk.Button(
        question2_win,
        text='Flint',
        font=('Arial'),
        width=10,
        command=q2_incorrect
    )
    question2_button_b.grid(
        row=3,
        column=2
    )

    question2_button_c = tk.Button(
        question2_win,
        text='Cardiff',
        font=('Arial'),
        width=10,
        command=q2_correct
    )
    question2_button_c.grid(
        row=4,
        column=1
    )

    question2_button_d = tk.Button(
        question2_win,
        text='Llandudno',
        font=('Arial'),
        width=10,
        command=q2_incorrect
    )
    question2_button_d.grid(
        row=4,
        column=2
    )

    question1_win.destroy()


def question_1():
    def q1_correct():
        correct()
        question_2()
    
    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is London')
        question_2()

    global question1_win

    question1_win = Toplevel()
    question1_win.geometry('282x90+0+0')
    question1_win.resizable(False,False)
    question1_win.title('UK Capitals Quiz - Question 1')

    question1_label = tk.Label(
        question1_win,
        text='What is the capital of England?',
        font=('Arial',20)
    )
    question1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question1_button_a = tk.Button(
        question1_win,
        text='London',
        font=('Arial'),
        width=10,
        command=q1_correct
    )
    question1_button_a.grid(
        row=3,
        column=1
    )

    question1_button_b = tk.Button(
        question1_win,
        text='Liverpool',
        font=('Arial'),
        width=10,
        command=q1_incorrect
    )
    question1_button_b.grid(
        row=4,
        column=1
    )

    question1_button_c = tk.Button(
        question1_win,
        text='Manchester',
        font=('Arial'),
        width=10,
        command=q1_incorrect
    )
    question1_button_c.grid(
        row=3,
        column=2
    )

    question1_button_d = tk.Button(
        question1_win,
        text='Birmingham',
        font=('Arial'),
        width=10,
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
root.geometry('170x60+0+0')
root.resizable(False,False)
root.title('UK Capitals Quiz')

root_title = tk.Label(
    root,
    text='UK Capitals Quiz',
    font=('Arial',20,'bold')
)
root_title.pack()

start_button = tk.Button(
    root,
    text='Start Quiz',
    font=('Arial'),
    command=question_1
)
start_button.pack()

root.mainloop()