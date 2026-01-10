import tkinter as tk
from tkinter import Toplevel, messagebox
import datetime
from datetime import datetime

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