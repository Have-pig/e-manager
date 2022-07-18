import tkinter as tk
import glovar
from mainusegui import delhello
from ACCPASS import delaccpass
from SETTING import delsetting
from ACG import delacg


def tool(win, y):
    if glovar.hellos:
        delhello()
    else:
        if glovar.domaintype == "ACG":
            delacg()
        elif glovar.domaintype == "ACCPASS":
            delaccpass()
        elif glovar.domaintype == "SETTING":
            delsetting()


def deltool():
    pass