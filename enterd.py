import json
import hbdalfhb665g
import mainusegui
import tkinter as tk


def warn(win, x, y):
    warnword = tk.Label(win, bg="white", text="The information which you input was wrong", fg="orange")
    warnword.place(x=int(x*0.442), y=int(y*0.565))

def check(win, x, y, username, password):
    isTrue = False
    with open("userinfo.json", "r") as f:
        jsons = json.load(f)
        try:
            userinfo = jsons["user{0}".format(username)]
            types = userinfo["type"]
            if types == 0:
                dealpassword = hbdalfhb665g.adadasdg(password)
            elif types == 1:
                    dealpassword = hbdalfhb665g.oiuyfyiohiu(password)
            else:
                dealpassword = hbdalfhb665g.aouifvafa(password)
            if dealpassword == userinfo["password"]:
                isTrue = True
            else:
                warn(win, x, y)
        except:
            warn(win, x, y)
    if isTrue:
        mainusegui.use(win, x, y)