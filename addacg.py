import tkinter as tk


def add(win, x, y):
    addwin = tk.Toplevel()
    addwin.title("Add")
    addwin.resizable(False, False)
    addwin.iconphoto(True, tk.PhotoImage(file="gui\\icon.png"))

    left = int((addwin.winfo_screenwidth()-x)/2)
    top = int((addwin.winfo_screenheight()-y)/2.5)
    addwin.geometry(f"{x}x{y}+{left}+{top}")

    inpution = tk.Entry(addwin, bg="white", bd=1, width=int(x/11.6))
    inpution.place(x=int(x*0.5), y=int(y*0.2))
