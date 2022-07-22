import tkinter as tk
import glovar
import mainusegui
import ACG
import TOOL
import SETTING


def accpass(win, y, x):
    if glovar.hellos:
        mainusegui.canvasn.delete(mainusegui.hello)
    else:
        if glovar.domaintype == "ACG":
            pass
        elif glovar.domaintype == "TOOL":
            pass
        elif glovar.domaintype == "SETTING":
            pass
