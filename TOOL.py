import tkinter as tk
import glovar
import mainusegui
import ACCPASS
import SETTING
import ACG


def tool(win, y, x):
    if glovar.hellos:
        mainusegui.canvasn.delete(mainusegui.hello)
        glovar.hellos = False

    else:
        if glovar.domaintype == "ACG":
            ACG.searches.destroy()
            ACG.next.destroy()
            ACG.addtion.destroy()

        elif glovar.domaintype == "ACCPASS":
            ACCPASS.DelAccount.destroy()
            ACCPASS.CancelLation.destroy()
            ACCPASS.ResetPassword.destroy()

        elif glovar.domaintype == "SETTING":
            SETTING.la.destroy()
    
    global la
    la = tk.Label(win, text="Please wait", fg="blue", bg="white", font=("宋体", 13))
    la.place(x=int(y*3.5/16), y=int(y*0.0625))

    glovar.domaintype = "TOOL"
