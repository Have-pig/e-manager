import tkinter as tk
from rrreeessstttaaarrrtttt import cancellation
import json
import hbdalfhb665g
import glovar
from random import randint


def saveinfo(win, password, x, y):
    warn = tk.Label(win, bg="white", fg="red", text="Empty!")
    if password == "":
        warn.place(x=int(x*0.38), y=int(y*0.7))
    else:
        with open("userinfo.json", "r") as f:
            jsons = json.load(f)

        thistype = randint(0, 2)
        if thistype == 0:
            dealpassword = hbdalfhb665g.adadasdg(password)
        elif thistype == 1:
            dealpassword = hbdalfhb665g.oiuyfyiohiu(password)
        else:
            dealpassword = hbdalfhb665g.aouifvafa(password)

        with open("userinfo.json", "w") as f:
            jsons["user{0}".format(glovar.loginacc)] = {"password":dealpassword, "type":thistype}
            json.dump(jsons, fp=f, indent=4)

            title = tk.Label(win, bg="white", fg="green", text="Succeed!")
            title.place(anchor="center", x=int(x*0.5), y=int(y*0.85))


def ResetPass(x, y):

    resset = tk.Toplevel()
    resset.title("Reset")
    resset.resizable(False, False)
    resset.iconphoto(True, tk.PhotoImage(file="gui\\icon.png"))

    resset.geometry("{0}x{1}".format(int(x*0.4), int(y*0.4)))

    innewpass = tk.Entry(resset, bg="white", fg="green", width=int(x/29), bd=1)
    save = tk.Button(resset, bg="white", fg="red", text="   Save   ", bd=1, command=lambda:saveinfo(resset, innewpass.get(), int(x*0.4), int(y*0.4)))
    innewpass.place(x=int(x*0.2), y=int(y*0.12), anchor="center")
    save.place(anchor="center", x=int(x*0.2), y=int(y*0.24))

    resset.mainloop()