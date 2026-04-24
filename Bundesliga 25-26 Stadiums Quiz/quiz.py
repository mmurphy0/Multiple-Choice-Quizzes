import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

from time import strftime

root_win = tk.Tk()
root_win.geometry('+0+0')
root_win.resizable(False,False)
root_win.title('Bundesliga 25-26 Stadiums Quiz')

root_label = tk.Label(
    root_win,
    text='Bundesliga 25-26 Stadiums Quiz',
    font=('Arial',20,'bold')
)
root_label.pack()

startquiz_button = tk.Button(
    root_win,
    text='Start',
    font=('Arial')
)
startquiz_button.pack()

root_win.mainloop()
