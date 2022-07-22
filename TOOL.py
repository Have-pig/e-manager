import tkinter as tk
import glovar
import mainusegui
import ACCPASS
import SETTING
import ACG


def tool(win, y, x):
    if glovar.hellos:
        mainusegui.canvasn.delete(mainusegui.hello)
    else:
        if glovar.domaintype == "ACG":
            pass
        elif glovar.domaintype == "ACCPASS":
            pass
        elif glovar.domaintype == "SETTING":
            pass
