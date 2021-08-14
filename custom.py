import tkinter as tk
from tkinter import Label, Toplevel, ttk


class MyApp(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.attributes('-alpha', 1)
        self.attributes('-topmost', False)
        self.resizable(False, False)
        self.title('App custom maker')
        self.set_ui()

    def set_ui(self):
        exit = ttk.Button(self, text='Button', command = self.open_new_win)
        exit.pack(fill=tk.X)

    def open_new_win(self):
        exit1 = ttk.Button(self, text='exit', command = self.app_exit)
        exit1.pack(fill=tk.X)
        Label(Toplevel(root), text='Hi')


    def app_exit(self):
        self.destroy()

root = MyApp()
root.mainloop()
