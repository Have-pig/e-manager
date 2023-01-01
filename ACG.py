import tkinter as tk
import glovar
import mainusegui
import ACCPASS 
import SETTING
import TOOL
import json
from addacg import add


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
    searches.place(x=int(y*3.7/16), y=int(y*0.0625))

    global next
    next = tk.Button(win, bg="white", text="Search", fg="blue", bd=1)
    next.place(x=int(x*0.43), y=int(y*0.054))

    global addtion
    ix = int(x*0.4)
    iy = int(y*0.4)
    addtion = tk.Button(win, bg="white", bd=1, text="Add", fg="blue", command=lambda:add(win, ix, iy))
    addtion.place(x=int(x*0.5), y=int(y*0.054))

    global updatebut
    updatebut = tk.Button(win, bg="white", bd=1, text="Update", fg="green", command=win.update)
    updatebut.place(x=int(x*0.55), y=int(y*0.054))

    global emptyacg
    emptyacg = tk.Label(win, bg="white", bd=0, text="You haven't added animation yet!", fg="orange", font=("宋体", 13))

    if glovar.firsttimetouse:
        emptyacg.place(x=int(x*0.4), y=int(y*0.5))
    else:
        with open("userACG\\"+glovar.loginacc+"\\acginfo.json", "r") as f:
            jsons = json.load(f)

        alls = jsons.values()

        groups = 1
        times = 0
        re = []
        Grouplist = []
        for i in alls:
            re.append(i)
            times += 1
            if times == 7:
                exec(f"global Group{groups}")
                exec(f"Group{groups} = re[:]")
                exec(f"Grouplist.append(Group{groups})")
                times = 0
                groups += 1
                re = []
            elif list(alls).index(i) == len(alls)-1:
                exec(f"global Group{groups}")
                exec(f"Group{groups} = re[:]")
                exec(f"Grouplist.append(Group{groups})")
 
        page = 1
        global lI
        # for i in Grouplist:
        #     for j in i:


    glovar.domaintype = "ACG"