import tkinter as tk
from tkinter import messagebox, Toplevel
import datetime
from datetime import datetime

score = int(0)

def question_5():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        socre += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The Answer is Dublin')

    global question5_win

    question5_win = Toplevel()
    question1_win.geometry('280x90')
    question5_win.minsize(280,90)
    question5_win.maxsize(280,90)

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
        command=incorrect
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
        command=incorrect
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
        command=incorrect
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
        command=correct
    )
    question5_button_d.grid(
        row=4,
        column=2
    )

    question4_win.destroy()


def question_4():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is Belfast')

    global question4_win

    question4_win = Toplevel()
    question4_win.geometry('280x90')
    question4_win.minsize(280,90)
    question4_win.maxsize(280,90)

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
        command=correct
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
        command=incorrect
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
        command=incorrect
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
        command=incorrect
    )
    question4_button_d.grid(
        row=4,
        column=2
    )

    question3_win.destroy()

def question_3():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is Edinburgh')

    global question3_win

    question3_win = Toplevel()
    question3_win.geometry('280x90')
    question3_win.minsize(280,90)
    question3_win.maxsize(280,90)

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
        command=incorrect
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
        command=correct
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
        command=incorrect
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
        command=incorrect
    )
    question3_button_d.grid(
        row=4,
        column=2
    )

    question2_win.destroy()


def question_2():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1
        question_3()
    
    def incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is Cardiff')
        question_3()

    global question2_win

    question2_win = Toplevel()
    question2_win.geometry('280x90')
    question2_win.minsize(280,90)
    question2_win.maxsize(280,90)

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
        command=incorrect
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
        command=incorrect
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
        command=correct
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
        command=incorrect
    )
    question2_button_d.grid(
        row=4,
        column=2
    )

    question1_win.destroy()


def question_1():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1
        question_2()
    
    def incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is London')
        question_2()

    global question1_win

    question1_win = Toplevel()
    question1_win.geometry('280x90')
    question1_win.minsize(280,90)
    question1_win.minsize(280,90)

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
        command=correct
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
        command=incorrect
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
        command=incorrect
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
        command=incorrect
    )
    question1_button_d.grid(
        row=4,
        column=2
    )


root = tk.Tk()
root.geometry('160x60')
root.minsize(160,60)
root.maxsize(160,60)
root.title('Capital City Quiz')

root_title = tk.Label(
    root,
    text='Capital City Quiz',
    font=('Arial',20)
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