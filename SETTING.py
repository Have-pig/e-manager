import tkinter as tk
import glovar
import mainusegui
import ACCPASS
import ACG
import TOOL


def setting(win, y, x):
    if glovar.hellos:
        mainusegui.canvasn.delete(mainusegui.hello)
    else:
        if glovar.domaintype == "ACG":
            pass
        elif glovar.domaintype == "TOOL":
            pass
        elif glovar.domaintype == "ACCPASS":
            pass

