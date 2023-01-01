import tkinter as tk
import glovar
import mainusegui
import ACCPASS
import ACG
import TOOL


def setting(win, y, x):
    if glovar.hellos:
        mainusegui.canvasn.delete(mainusegui.hello)
        glovar.hellos = False

    else:
        if glovar.domaintype == "ACG":
            ACG.searches.destroy()
            ACG.next.destroy()
            ACG.addtion.destroy()
            ACG.emptyacg.destroy()
            ACG.updatebut.destroy()

        elif glovar.domaintype == "TOOL":
            TOOL.la.destroy()
            
        elif glovar.domaintype == "ACCPASS":
            ACCPASS.DelAccount.destroy()
            ACCPASS.CancelLation.destroy()
            ACCPASS.ResetPassword.destroy()

    global la
    la = tk.Label(win, text="Please wait", fg="blue", bg="white", font=("宋体", 13))
    la.place(x=int(y*3.5/16), y=int(y*0.0625))

    directlogin = tk.Button(win, text="")

    glovar.domaintype = "SETTING"