import tkinter as tk
from tkinter import messagebox, Toplevel
import datetime
from datetime import datetime

root = tk.Tk()
root.geometry('200x80+0+0')
root.resizable(False,False)
root.title('Premier League Quiz')

quiz_title = tk.Label(
    root,
    text='Premier League Quiz 24/25',
    font=('Arial',20,'bold')
)
quiz_title.pack()

startquiz_button = tk.Button(
    root,
    text='Start Quiz',
)