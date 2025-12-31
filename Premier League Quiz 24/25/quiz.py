import tkinter as tk
from tkinter import messagebox, Toplevel
import datetime
from datetime import datetime

root = tk.Tk()
root.geometry('257x60+0+0')
root.resizable(False,False)
root.title('Premier League Quiz 24/25')

quiz_title = tk.Label(
    root,
    text='Premier League Quiz 24/25',
    font=('Arial',20,'bold')
)
quiz_title.pack()

startquiz_button = tk.Button(
    root,
    text='Start Quiz',
    font=('Arial'),
    width=40
)
startquiz_button.pack()

root.mainloop()