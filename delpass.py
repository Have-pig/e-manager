import tkinter as tk
import json
import glovar
from rrreeessstttaaarrrtttt import cancellation
from os import rmdir, remove


def DelPass(win, x, y):
    with open("userinfo.json", "r") as f:
        jsons = json.load(f)

    with open("userinfo.json", "w") as f:
        jsons.pop("user"+glovar.loginacc)
        json.dump(jsons, fp=f, indent=4)
    
    remove(path="userACG\\"+glovar.loginacc+"\\acginfo.json")
    rmdir(path="userACG\\"+glovar.loginacc)

    win.destroy()

    warn = tk.Tk()
    warn.title("Succeed!")
    warn.iconphoto(True, tk.PhotoImage(file="gui\\icon.png"))

    left = int((warn.winfo_screenwidth()-x)/2)
    top = int((warn.winfo_screenheight()-y)/2.5)
    warn.geometry(f"{x}x{y}+{left}+{top}")
    warn.resizable(False, False)

    titles = tk.Label(warn, text="Succeed!\nNow you can click the button to restart!", fg="blue", font=("宋体", 13))
    titles.place(x=int(x*0.0575), y=int(y*0.3))

    Rsss = tk.Button(warn, text="Restart", bg="white", fg="red", bd=1, command=lambda:cancellation(warn), font=("宋体", 13))
    Rsss.place(x=int(x*0.4125), y=int(y*0.6))