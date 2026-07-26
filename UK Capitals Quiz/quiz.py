import tkinter as tk
from tkinter import messagebox, Toplevel
from tkinter import ttk

from time import strftime

import platform

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


def results(question5_win):
    global results_win

    results_win = Toplevel()
    results_win.geometry('+0+0')
    results_win.resizable(False,False)
    results_win.title('UK Capitals Quiz - Results')

    results_title = ttk.Label(
        results_win,
        text='Results',
        style='Title.TLabel'
    )
    results_title.pack()

    results_display = ttk.Label(
        results_win,
        text=(f'Score: {score}/5'),
        style='Title.TLabel'
    )
    results_display.pack()

    continue_button = ttk.Button(
        results_win,
        text='Continue',
        style='Button.TButton',
        width=20,
        command=save
    )
    continue_button.pack(padx=10, pady=10)

    question5_win.destroy()


def question_5(question4_win):
    def q5_correct():
        correct()
        results(question5_win)

    def q5_incorrect():
        messagebox.showinfo('Incorrect','The Answer is Dublin')
        results(question5_win)

    question5_win = Toplevel()
    question5_win.geometry('+0+0')
    question5_win.resizable(False,False)
    question5_win.title('UK Capitals Quiz - Question 5')

    question5_label = ttk.Label(
        question5_win,
        text='What is the capital of Ireland?',
        style='Title.TLabel'
    )
    question5_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question5_button_a = ttk.Button(
        question5_win,
        text='Limerick',
        style='Button.TButton',
        width=10,
        command=q5_incorrect
    )
    question5_button_a.grid(
        row=3,
        column=1
    )

    question5_button_b = ttk.Button(
        question5_win,
        text='Cork',
        style='Button.TButton',
        width=10,
        command=q5_incorrect
    )
    question5_button_b.grid(
        row=3,
        column=2
    )

    question5_button_c = ttk.Button(
        question5_win,
        text='Galway',
        style='Button.TButton',
        width=10,
        command=q5_incorrect
    )
    question5_button_c.grid(
        row=4,
        column=1
    )

    question5_button_d = ttk.Button(
        question5_win,
        text='Dublin',
        style='Button.TButton',
        width=10,
        command=q5_correct
    )
    question5_button_d.grid(
        row=4,
        column=2
    )

    question4_win.destroy()


def question_4(question3_win):
    def q4_correct():
        correct()
        question_5(question4_win)

    def q4_incorrect():
        messagebox.showinfo('Incorrect','The answer is Belfast')
        question_5(question4_win)

    question4_win = Toplevel()
    question4_win.geometry('+0+0')
    question4_win.resizable(False,False)
    question4_win.title('UK Capitals Quiz - Question 4')

    question4_label = ttk.Label(
        question4_win,
        text='What is the capital of Northern Ireland?',
        style='Title.TLabel'
    )
    question4_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question4_button_a = ttk.Button(
        question4_win,
        text='Belfast',
        style='Button.TButton',
        width=10,
        command=q4_correct
    )
    question4_button_a.grid(
        row=3,
        column=1
    )

    question4_button_b = ttk.Button(
        question4_win,
        text='Londonderry',
        style='Button.TButton',
        width=10,
        command=q4_incorrect
    )
    question4_button_b.grid(
        row=3,
        column=2
    )

    question4_button_c = ttk.Button(
        question4_win,
        text='Lisburn',
        style='Button.TButton',
        width=10,
        command=q4_incorrect
    )
    question4_button_c.grid(
        row=4,
        column=1
    )

    question4_button_d = ttk.Button(
        question4_win,
        text='Newtownabbey',
        style='Button.TButton',
        width=10,
        command=q4_incorrect
    )
    question4_button_d.grid(
        row=4,
        column=2
    )

    question3_win.destroy()


def question_3(question2_win):
    def q3_correct():
        correct()
        question_4(question3_win)

    def q3_incorrect():
        messagebox.showinfo('Incorrect','The answer is Edinburgh')
        question_4(question3_win)

    question3_win = Toplevel()
    question3_win.geometry('+0+0')
    question3_win.resizable(False,False)
    question3_win.title('UK Capitals Quiz - Question 3')

    question3_label = ttk.Label(
        question3_win,
        text='What is the capital of Scotland?',
        style='Title.TLabel',
    )
    question3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question3_button_a = ttk.Button(
        question3_win,
        text='Glasgow',
        style='Button.TButton',
        width=10,
        command=q3_incorrect
    )
    question3_button_a.grid(
        row=3,
        column=1
    )

    question3_button_b = ttk.Button(
        question3_win,
        text='Edinburgh',
        style='Button.TButton',
        width=10,
        command=q3_correct
    )
    question3_button_b.grid(
        row=3,
        column=2
    )

    question3_button_c = ttk.Button(
        question3_win,
        text='Aberdeen',
        style='Button.TButton',
        width=10,
        command=q3_incorrect
    )
    question3_button_c.grid(
        row=4,
        column=1
    )

    question3_button_d = ttk.Button(
        question3_win,
        text='Inverness',
        style='Button.TButton',
        width=10,
        command=q3_incorrect
    )
    question3_button_d.grid(
        row=4,
        column=2
    )

    question2_win.destroy()

def question_2(question1_win):
    def q2_correct():
        correct()
        question_3(question2_win)
    
    def q2_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Cardiff')
        question_3(question2_win)

    question2_win = Toplevel()
    question2_win.geometry('+0+0')
    question2_win.resizable(False,False)
    question2_win.title('UK Capitals Quiz - Question 2')

    question2_label = ttk.Label(
        question2_win,
        text='What is the capital of Wales?',
        style='Title.TLabel'
    )
    question2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question2_button_a = ttk.Button(
        question2_win,
        text='Swansea',
        style='Button.TButton',
        width=10,
        command=q2_incorrect
    )
    question2_button_a.grid(
        row=3,
        column=1
    )

    question2_button_b = ttk.Button(
        question2_win,
        text='Flint',
        style='Button.TButton',
        width=10,
        command=q2_incorrect
    )
    question2_button_b.grid(
        row=3,
        column=2
    )

    question2_button_c = ttk.Button(
        question2_win,
        text='Cardiff',
        style='Button.TButton',
        width=10,
        command=q2_correct
    )
    question2_button_c.grid(
        row=4,
        column=1
    )

    question2_button_d = ttk.Button(
        question2_win,
        text='Llandudno',
        style='Button.TButton',
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
        question_2(question1_win)
    
    def q1_incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is London')
        question_2(question1_win)

    question1_win = Toplevel()
    question1_win.geometry('+0+0')
    question1_win.resizable(False,False)
    question1_win.title('UK Capitals Quiz - Question 1')

    question1_label = ttk.Label(
        question1_win,
        style='Title.TLabel',
        text='What is the capital of England?',
    )
    question1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question1_button_a = ttk.Button(
        question1_win,
        text='London',
        style='Button.TButton',
        width=10,
        command=q1_correct
    )
    question1_button_a.grid(
        row=3,
        column=1
    )

    question1_button_b = ttk.Button(
        question1_win,
        text='Liverpool',
        style='Button.TButton',
        width=10,
        command=q1_incorrect
    )
    question1_button_b.grid(
        row=4,
        column=1
    )

    question1_button_c = ttk.Button(
        question1_win,
        text='Manchester',
        style='Button.TButton',
        width=10,
        command=q1_incorrect
    )
    question1_button_c.grid(
        row=3,
        column=2
    )

    question1_button_d = ttk.Button(
        question1_win,
        text='Birmingham',
        style='Button.TButton',
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

def initiate_styles():
    button_style = ttk.Style()
    title_style = ttk.Style()

    current_os = platform.system()

    if current_os == 'Windows':
        button_style.theme_use('vista')
        button_style.configure(
            'Button.TButton',
            font=('Arial',10),
            bg='White',
            fg='Black'
        )

        title_style.configure(
            'Title.TLabel',
            font=('Arial',15,'bold')
        )

    elif current_os == 'Darwin':
        button_style.configure(
            'Button.TButton',
            font=('Arial')
        )

        title_style.configure(
            'Title.TLabel',
            font=('Arial',20,'bold')
        )

root = tk.Tk()
root.geometry('+0+0')
root.resizable(False,False)
root.title('UK Capitals Quiz')

initiate_styles()

root_title = ttk.Label(
    root,
    style='Title.TLabel',
    text='UK Capitals Quiz'
)
root_title.pack()

start_button = ttk.Button(
    root,
    style='Button.TButton',
    text='Start Quiz',
    command=question_1
)
start_button.pack()

root.mainloop()