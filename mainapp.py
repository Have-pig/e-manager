import tkinter as tk
from PIL import Image
from os import getcwd
from ACG import acg
from TOOL import tool
from SETTING import setting
from ACCPASS import accpass


class domain:
    def __init__(self, win, y, x,func) -> None:
        self.win = win
        self.y = y
        self.x = x
        self.do = func

    def next(self, event):
        self.do(self.win, self.y, self.x)

def dealpic(y, name):
    use = Image.open("gui\\"+name)
    purposesizes = (int(y/16*3), int(y/8))
    box = (0, 0, 270, 180)
    dealed = use.resize(purposesizes, box=box)
    savefile = getcwd()+"\\used\\"+name[:-4]+"used.png"
    dealed.save(savefile)

    return savefile

def next(win, ys, xs):
    ACG = tk.Canvas(win, width=int(ys*3/16), height=int(ys/8))
    ACCPASS = tk.Canvas(win, width=int(ys*3/16), height=int(ys/8))
    TOOL = tk.Canvas(win, width=int(ys*3/16), height=int(ys/8))
    SETTING = tk.Canvas(win, width=int(ys*3/16), height=int(ys/8))

    ACGPicfile = dealpic(ys, "ACG.png")
    ACCPASSfile = dealpic(ys, "mima.png")
    TOOLfile = dealpic(ys, "tool.png")
    SETTINGfile = dealpic(ys, "setting.png")

    ACGpic = tk.PhotoImage(file=ACGPicfile)
    ACCPASSpic = tk.PhotoImage(file=ACCPASSfile)
    TOOLpic = tk.PhotoImage(file=TOOLfile)
    SETTINGpic = tk.PhotoImage(file=SETTINGfile)

    ACG.create_image(0, 0, anchor="nw", image=ACGpic)
    ACCPASS.create_image(0, 0, anchor="nw", image=ACCPASSpic)
    TOOL.create_image(0, 0, anchor="nw", image=TOOLpic)
    SETTING.create_image(0, 0, anchor="nw", image=SETTINGpic)

    acgg = domain(win, ys, xs, acg)
    accpasss = domain(win, ys, xs, accpass)
    tooll = domain(win, ys, xs, tool)
    settingg = domain(win, ys, xs, setting)
    ACG.bind("<ButtonRelease-1>", acgg.next)
    ACCPASS.bind("<ButtonRelease-1>", accpasss.next)
    TOOL.bind("<ButtonRelease-1>", tooll.next)
    SETTING.bind("<ButtonRelease-1>", settingg.next)

    ACG.place(x=0, y=int(ys/16*3))
    ACCPASS.place(x=0, y=int(ys/16*3+ys/7.9))
    TOOL.place(x=0, y=int(int(ys/16*3+ys*2/7.9)))
    SETTING.place(x=0, y=int(int(ys/16*3+ys*3/7.9)))