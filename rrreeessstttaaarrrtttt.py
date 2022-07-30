from sys import executable, exit, argv
from os import execl


def cancellation(win):
    win.destroy()

    execl(executable, executable, *argv)
    exit()