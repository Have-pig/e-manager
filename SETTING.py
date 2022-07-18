import tkinter as tk
import glovar
from mainusegui import delhello
from ACCPASS import delaccpass
from ACG import delacg
from TOOL import deltool


def setting(win, y):
    if glovar.hellos:
        delhello
    else:
        if glovar.domaintype == "ACG":
            delacg()
        elif glovar.domaintype == "TOOL":
            deltool()
        elif glovar.domaintype == "ACCPASS":
            delaccpass()


def delsetting():
    pass