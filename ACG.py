import tkinter as tk
import glovar
import mainusegui
import ACCPASS 
import SETTING
import TOOL


def acg(win, y, x):
    if glovar.hellos:
        mainusegui.canvasn.delete(mainusegui.hello)
        glovar.hellos = False
        
    else:
        if glovar.domaintype == "ACCPASS":
            ACCPASS.DelAccount.destroy()
            ACCPASS.CancelLation.destroy()
            ACCPASS.ResetPassword.destroy()

        elif glovar.domaintype == "TOOL":
            TOOL.la.destroy()

        elif glovar.domaintype == "SETTING":
            SETTING.la.destroy()

    global searches
    searches = tk.Entry(win, bg="white", width=int((x/25)), bd=1)
    searches.place(x=int(y*3.5/16), y=int(y*0.0625))

    glovar.domaintype = "ACG"