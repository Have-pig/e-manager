import tkinter as tk
import glovar
import mainusegui
import ACCPASS 
import SETTING
import TOOL


def acg(win, y, x):
    if glovar.hellos:
        mainusegui.canvasn.delete(mainusegui.hello)
    else:
        if glovar.domaintype == "ACCPASS":
            pass
        elif glovar.domaintype == "TOOL":
            pass
        elif glovar.domaintype == "SETTING":
            pass

    searches = tk.Entry(win, bg="white", width=int((x/25)), bd=1)
    searches.place(x=int(y*3.5/16), y=int(y*0.0625))