import tkinter as tk
import glovar
from mainusegui import delhello
from ACG import delacg
from TOOL import deltool
from SETTING import delsetting


def accpass(win, y):
    if glovar.hellos:
        delhello()
    else:
        if glovar.domaintype == "ACG":
            delacg()
        elif glovar.domaintype == "TOOL":
            deltool()
        elif glovar.domaintype == "SETTING":
            delsetting()


def delaccpass():
    pass