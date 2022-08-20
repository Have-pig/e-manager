import tkinter as tk
import glovar
import mainusegui
import ACCPASS 
import SETTING
import TOOL
import json


def acg(win, y, x):
    glovar.acgbe = False


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
    searches.place(x=int(y*3.7/16), y=int(y*0.0625))

    global next
    next = tk.Button(win, bg="white", text="Search", fg="blue", bd=1)
    next.place(x=int(x*0.43), y=int(y*0.054))

    global addtion
    addtion = tk.Button(win, bg="white", bd=1, text="Add", fg="blue")
    addtion.place(x=int(x*0.5), y=int(y*0.054))

    global updatebut
    updatebut = tk.Button(win, bg="white", bd=1, text="Update", fg="green", command=win.update)
    updatebut.place(x=int(x*0.55), y=int(y*0.054))

    global emptyacg
    emptyacg = tk.Label(win, bg="white", bd=0, text="You haven't added animation yet!", fg="yellow", font=("宋体", 13))

    if glovar.firsttimetouse:
        emptyacg.place(x=int(x*0.5), y=int(y*0.5))
    else:
        pass

    glovar.domaintype = "ACG"