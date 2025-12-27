import tkinter as tk
from tkinter import Toplevel, messagebox
import datetime
from datetime import datetime

score = 0

def question9():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is The Reds')

    global question9_win

    question9_win = Toplevel()
    question9_win.geometry('280,90'),
    question9_win.minsize(280,90)
    question9_win.maxsize(280,90)
    question9_win.title('Liverpool FC Quiz - Question 9')

    question9_label = tk.Label(
        question9_win,
        text="What is Liverpool's nickname?",
        font=('Arial',20)
    )
    question9_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question9_button_a = tk.Button(
        question9_win,
        text='The Red Devils',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question9_button_a.grid(
        row=3,
        column=1
    )

    question9_button_b = tk.Button(
        question9_win,
        text='The Gunners',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question9_button_b.grid(
        row=3,
        column=2
    )

    question9_button_c = tk.Button(
        question9_win,
        text='The Reds',
        font=('Arial'),
        width=10,
        command=correct
    )
    question9_button_c.grid(
        row=4,
        column=1
    )

    question9_button_d = tk.Button(
        question9_win,
        text='The Foxes',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question9_button_d.grid(
        row=4,
        column=2
    )

    question8_win.destroy()


def question8():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is Red')

    global question8_win

    question8_win = Toplevel()
    question8_win.geometry('280,90')
    question8_win.minsize(280,90)
    question8_win.maxsize(280,90)
    question8_win.title('Liverpool FC Quiz - Question 8')

    question8_label = tk.Label(
        question8_win,
        text='Which Liverpool player famously slipped during a match against Chelsea?',
        font=('Arial',20)
    )
    question8_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question8_button_a = tk.Button(
        question8_win,
        text='Jamie Carragher',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question8_button_a.grid(
        row=3,
        column=1
    )

    question8_button_b = tk.Button(
        question8_win,
        text='Steven Gerrard',
        font=('Arial'),
        width=10,
        command=correct
    )
    question8_button_b.grid(
        row=3,
        column=2
    )

    question8_button_c = tk.Button(
        question8_win,
        text='Jordan Henderson',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question8_button_c.grid(
        row=4,
        column=1
    )

    question8_button_d = tk.Button(
        question8_win,
        text='Xabi Alonso',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question8_button_d.grid(
        row=4,
        column=2
    )

    question7_win.destroy()


def question7():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is Red')

    global question7_win

    question7_win = Toplevel()
    question7_win.geometry('280x90')
    question7_win.maxsize(280,90)
    question7_win.minsize(280,90)
    question7_win.title('Liverpool FC Quiz - Question 7')

    question7_label = tk.Label(
        question7_win,
        text="What colour is Liverpool's home kit?",
        font=('Arial',20),
    )
    question7_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question7_button_a = tk.Button(
        question7_win,
        text='Blue',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question7_button_a.grid(
        row=3,
        column=1
    )

    question7_button_b = tk.Button(
        question7_win,
        text='White',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question7_button_b.grid(
        row=3,
        column=2
    )

    question7_button_c = tk.Button(
        question7_win,
        text='Red',
        font=('Arial'),
        width=10,
        command=correct
    )
    question7_button_c.grid(
        row=4,
        column=1
    )

    question7_button_d = tk.Button(
        question7_win,
        text='Black',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question7_button_d.grid(
        row=4,
        column=2
    )

    question6_win.destroy()
    

def question6():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is Ian Rush')

    global question6_win

    question6_win = Toplevel()
    question6_win.geometry('280,90')
    question6_win.minsize(280,90)
    question6_win.maxsize(280,90)
    question6_win.title('Liverpool FC Quiz - Question 6')

    question6_label = tk.Label(
        question6_win,
        text="Who is Liverpool's all-time top goal scorer?",
        font=('Arial')
    )
    question6_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question6_button_a = tk.Button(
        question6_win,
        text='Ian Rush',
        font=('Arial'),
        width=10,
        command=correct
    )
    question6_button_a.grid(
        row=3,
        column=1
    )

    question6_button_b = tk.Button(
        question6_win,
        text='Steven Gerrard',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question6_button_b.grid(
        row=3,
        column=2
    )

    question6_button_c = tk.Button(
        question6_win,
        text='Mohammed Salah',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question6_button_c.grid(
        row=4,
        column=1
    )

    question6_button_d = tk.Button(
        question6_win,
        text='Robbie Fowler',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question6_button_d.grid(
        row=4,
        column=2
    )

    question5_win.destroy()


def question5():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is 6')

    global question5_win

    question5_win = Toplevel()
    question5_win.geometry('280x90')
    question5_win.minsize(280,90)
    question5_win.maxsize(280,90)
    question5_win.title('Liverpool FC Quiz - Question 5')

    question5_label = tk.Label(
        question5_win,
        text='How many times have Liverpool won the Champions League? as of 2025',
        font=('Arial',20),
    )
    question5_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question5_button_a = tk.Button(
        question5_win,
        text='4',
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
        text='5',
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
        text='6',
        font=('Arial'),
        width=10,
        command=correct
    )
    question5_button_c.grid(
        row=4,
        column=1
    )

    question5_button_d = tk.Button(
        question5_win,
        text='7',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question5_button_d.grid(
        row=4,
        column=2
    )

    question4_win.destroy()


def question4():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is Jurgen Klopp')

    global question4_win

    question4_win = Toplevel()
    question4_win.geometry('280x90')
    question4_win.minsize(280,90)
    question4_win.maxsize(280,90)
    question4_win.title('Liverpool FC Quiz - Question 4')

    question4_label = tk.Label(
        question4_win,
        text="Which Liverpool manager won the Champions League in 2019?",
        font=('Arial',20),
    )
    question4_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question4_button_a = tk.Button(
        question4_win,
        text='Jurgen Klopp',
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
        text='Brendan Rogers',
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
        text='Rafa Benítez',
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
        text='Kenny Dalglish',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question4_button_d.grid(
        row=4,
        column=2
    )

    question3_win.destroy()


def question3():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect',"The answer is You'll never walk alone")

    global question3_win

    question3_win = Toplevel()
    question3_win.geometry('280x90')
    question3_win.minsize(280,90)
    question3_win.maxsize(280,90)
    question3_win.title('Liverpool FC Quiz - Question 3')

    question3_label = tk.Label(
        question3_win,
        text="What's Liverpool's Walkout Anthem?",
        font=('Arial',20)
    )
    question3_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question3_button_a = tk.Button(
        question3_win,
        text='Blue Moon',
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
        text="You'll Never Walk Alone",
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
        text='Sweet Caroline',
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
        text='Wonderwall',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question3_button_d.grid(
        row=4,
        column=2
    )

    question2_win.destroy()

def question2():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1

    def incorrect():
        messagebox.showinfo('Incorrect','The answer is Anfield')

    global question2_win

    question2_win = Toplevel()
    question2_win.geometry('280x90')
    question2_win.minsize('280x90')
    question2_win.maxsize('280x90')
    question2_win.title('Liverpool FC Quiz - Question 2')

    question2_label = tk.Label(
        question2_win,
        text='What is the name of Liverpools home stadium?',
        font=('Arial',20)
    )
    question2_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question2_button_a = tk.Button(
        question2_win,
        text='Hill Dickinson',
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
        text='Old Trafford',
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
        text='Wembley',
        font=('Arial'),
        width=10,
        command=incorrect
    )
    question2_button_c.grid(
        row=4,
        column=2
    )

    question2_button_d = tk.Button(
        question2_win,
        text='Anfield',
        font=('Arial'),
        width=10,
        command=correct
    )
    question2_button_d.grid(
        row=4,
        column=2
    )

    question1_win.destroy()


def question1():
    def correct():
        global score
        messagebox.showinfo('Result','Correct!')
        score += 1
    
    def incorrect():
        messagebox.showinfo('Result','Incorrect, The answer is 1892')

    global question1_win

    question1_win = Toplevel()
    question1_win.geometry('345x90')
    question1_win.minsize(345,90)
    question1_win.maxsize(345,90)
    question1_win.title('Liverpool FC Quiz - Question 1')

    question1_label = tk.Label(
        question1_win,
        text='What year was Liverpool FC founded?',
        font=('Arial',20)
    )
    question1_label.grid(
        row=1,
        column=1,
        columnspan=2
    )

    question1_button_a = tk.Button(
        question1_win,
        text='1888',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question1_button_a.grid(
        row=3,
        column=1
    )

    question1_button_b = tk.Button(
        question1_win,
        text='1890',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question1_button_b.grid(
        row=3,
        column=2
    )

    question1_button_c = tk.Button(
        question1_win,
        text='1892',
        font=('Arial'),
        width=15,
        command=correct
    )
    question1_button_c.grid(
        row=4,
        column=1
    )

    question1_button_d = tk.Button(
        question1_win,
        text='1896',
        font=('Arial'),
        width=15,
        command=incorrect
    )
    question1_button_d.grid(
        row=4,
        column=2
    )


root = tk.Tk()
root.geometry('200x60')
root.minsize(200,60)
root.maxsize(200,60)
root.title('Liverpool FC Quiz')

quiz_title = tk.Label(
    root,
    text='Liverpool FC Quiz',
    font=('Arial',20,'bold')
)
quiz_title.pack()

startquiz_button = tk.Button(
    root,
    text='Start Quiz',
    font=('Arial'),
    width=20,
    command=question1
)
startquiz_button.pack()

root.mainloop()