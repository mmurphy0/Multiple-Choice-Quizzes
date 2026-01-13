import tkinter as tk
from tkinter import Toplevel, messagebox
import datetime
from datetime import datetime

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