import tkinter as tk
import json
import glovar
from rrreeessstttaaarrrtttt import cancellation


def DelPass(win, x, y):
    with open("userinfo.json", "r") as f:
        jsons = json.load(f)

    with open("userinfo.json", "w") as f:
        jsons.pop("user"+glovar.loginacc)
        json.dump(jsons, fp=f, indent=4)

    win.destroy()

    warn = tk.Tk()
    warn.title("Succeed!")
    warn.iconphoto(True, tk.PhotoImage(file="gui\\icon.png"))
    warn.geometry("{0}x{1}".format(int(x*0.4), int(y*0.4)))
    warn.resizable(False, False)

    titles = tk.Label(warn, text="Succeed!\nNow you can click the button to restart!", fg="blue", font=("宋体", 13))
    titles.place(x=int(x*0.023), y=int(y*0.12))

    Rsss = tk.Button(warn, text="Restart", bg="white", fg="red", bd=1, command=lambda:cancellation(warn), font=("宋体", 13))
    Rsss.place(x=int(x*0.165), y=int(y*0.32))
