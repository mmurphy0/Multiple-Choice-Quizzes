import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

from time import strftime

root = tk.Tk()
root.geometry('+0+0')
root.resizable(False,False)
root.title('Premier League 25/26 Stadiums Quiz')

root_title = tk.Label(
    root,
    text='Premier League 25/26 Stadiums Quiz',
    font=('Arial',20)
)
root_title.pack(anchor='center')

startquiz_button = tk.Button(
    root,
    text='Start',
    font=('Arial'),
    width=15
    # command=question1
)
startquiz_button.pack(anchor='center')

root.mainloop()