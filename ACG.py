import tkinter as tk
import glovar
from mainusegui import delhello
from ACCPASS import delaccpass
from SETTING import delsetting
from TOOL import deltool


def acg(win, y):
    if glovar.hellos:
        delhello()
    else:
        if glovar.domaintype == "ACCPASS":
            delaccpass()
        elif glovar.domaintype == "TOOL":
            deltool()
        elif glovar.domaintype == "SETTING":
            delsetting()


def delacg():
    pass