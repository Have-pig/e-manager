import tkinter as tk
import glovar
import mainusegui
import ACG
import TOOL
import SETTING
from respass import ResetPass
from delpass import DelPass
from rrreeessstttaaarrrtttt import cancellation


def accpass(win, y, x):
    if glovar.hellos:
        mainusegui.canvasn.delete(mainusegui.hello)
        glovar.hellos = False

    else:
        if glovar.domaintype == "ACG":
            ACG.searches.destroy()
            ACG.next.destroy()
            ACG.addtion.destroy()

        elif glovar.domaintype == "TOOL":
            TOOL.la.destroy()

        elif glovar.domaintype == "SETTING":
            SETTING.la.destroy()
            

    global ResetPassword
    global DelAccount
    global CancelLation
    isx = int(x*0.4)
    isy= int(y*0.4)
    ResetPassword = tk.Button(win, text="Reset password", bg="white", bd=1, command=lambda:ResetPass(isx, isy))
    DelAccount = tk.Button(win, text="Delete account", bg="white",  bd=1, command=lambda:DelPass(win, isx, isy))
    CancelLation = tk.Button(win, text="Cancellation", bg="white", bd=1, command=lambda:cancellation(win))

    ResetPassword.place(x=int(y*3.5/16), y=int(y*0.0325))
    DelAccount.place(x=int(y*3.5/16), y=int(y*0.1325))
    CancelLation.place(x=int(y*3.5/16), y=int(y*0.2325))

    glovar.domaintype = "ACCPASS"