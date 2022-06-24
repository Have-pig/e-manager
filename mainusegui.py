import tkinter as tk


def use(win, x, y):
    win.destroy()

    mainapp = tk.TK()
    mainapp.geometry("{0}x{1}".format(x, y))
    mainapp.title("e_manager")
    mainapp.resizable(False, False)
    mainapp.iconphoto(True, tk.PhotoImage(file="icon.png"))
