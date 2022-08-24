import tkinter as tk
import json
import glovar


def saveinfo(win, name, notes, types, x, y):
    a = int(types)
    if a  == 1:
        typess = "will watch"
    elif a == 2:
        typess = "watching"
    else:
        typess = "watched"
    
    if not(glovar.firsttimetouse):
        with open("userAcg\\"+glovar.loginacc+"\\acginfo.json") as f:
            jsons = json.load(f)
            names = list(jsons.keys())

    if name == "":
        warn = tk.Label(win, text="Name is empty!", fg="red")
        warn.place(x=int(x*0.65), y=int(y*0.2))
    elif name in names:
        warn2 = tk.Label(win, text="It has been added!", fg="red")
        warn2.place(x=int(x*0.2), y=int(y*0.1))
    else:
        with open("userACG\\"+glovar.loginacc+"\\acginfo.json", "r") as f:
            fl = json.load(f)
        with open("userACG\\"+glovar.loginacc+"\\acginfo.json", "w") as f:
            fl[name] = {"name":name, "note":notes, "state":typess}
            json.dump(fl, fp=f, indent=4, ensure_ascii=False)

        suc = tk.Label(win, text="OK! You can continue to add.", fg="orange")
        suc.place(x=int(x*0.7), y=int(y*0.6), anchor="n")

def add(win, x, y):
    addwin = tk.Toplevel()
    addwin.title("Add")
    addwin.resizable(False, False)
    addwin.iconphoto(True, tk.PhotoImage(file="gui\\icon.png"))

    left = int((addwin.winfo_screenwidth()-x)/2)
    top = int((addwin.winfo_screenheight()-y)/2.5)
    addwin.geometry(f"{x}x{y}+{left}+{top}")

    names = tk.Label(addwin, text="Name:")
    notes = tk.Label(addwin, text="Notes:")

    names.place(x=int(x*0.05), y=int(y*0.2))
    notes.place(x=int(x*0.05), y=int(y*0.35))

    inputname = tk.Entry(addwin, bg="white", bd=1, width=int(x/16))
    inputnotes = tk.Entry(addwin, bg="white", bd=1, width=int(x/10))

    inputname.place(x=int(x*0.2), y=int(y*0.2))
    inputnotes.place(x=int(x*0.2), y=int(y*0.35))

    V = tk.IntVar()
    V.set(1)

    new = tk.Radiobutton(addwin, text="will watch", variable=V, value=1)
    looking = tk.Radiobutton(addwin, text="watching", variable=V, value=2)
    looked = tk.Radiobutton(addwin, text="watched", variable=V, value=3)

    new.place(x=int(x*0.2), y=int(y*0.55))
    looking.place(x=int(x*0.2), y=int(y*0.65))
    looked.place(x=int(x*0.2), y=int(y*0.75))

    save = tk.Button(addwin, bg="white", bd=1, text="Save", command=lambda:saveinfo(addwin, inputname.get(), inputnotes.get(), V.get(), x, y))
    save.place(x=int(x*0.8), y=int(y*0.75))






