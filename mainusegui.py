import tkinter as tk
from PIL import Image
from os import getcwd
from datetime import datetime
from mainapp import next
import glovar
import os.path as paths
from os import makedirs


def dealmaingui(x, y):
    paths = "gui\\welcome.png"
    use = Image.open(paths)
    purposesizes = (x, y)
    box = (0, 0, 2560, 1440)
    dealpic = use.resize(purposesizes, box=box)
    filepath = getcwd()+"\\used\\welcomeused.png"
    dealpic.save(filepath)

    return filepath

def dealhellopic(x, y):
    a = datetime.now()
    hour = int(a.strftime("%H"))
    if 0 <= hour < 12:
        paths = "gui\\hellomorning.png"
        name = "hellomorningused.png"
    elif 12 <= hour < 18:
        paths = "gui\\helloafternoon.png"
        name = "helloafternoonused.png"
    else:
        paths = "gui\\helloevening.png"
        name = "helloeveningused.png"
    use = Image.open(paths)
    purposesizes = (int(x-(y/16*3)), y)
    box = (0, 0, 2290, 1440)
    dealpic = use.resize(purposesizes, box=box)
    filepath = getcwd()+"\\used\\"+name
    dealpic.save(filepath)

    return filepath

def dealheadimage(y):
    paths = "gui\\headimage.png"
    use = Image.open(paths)
    purposesizes = (int(y/16*2.1), int(y/16*2.1))
    box = (0, 0, 480, 480)
    dealpic = use.resize(purposesizes, box=box)
    filepath = getcwd()+"\\used\\headimageused.png"
    dealpic.save(filepath)

    return filepath


def use(win, x, y):
    win.destroy()

    userpath = "userACG\\"+glovar.loginacc
    if not(paths.exists(userpath)):
        makedirs(userpath)

    userfile = "userACG\\"+glovar.loginacc+"\\acginfo.json"
    if not(paths.isfile(userfile)):
        f = open(userfile, "x")
        f.closed

    mainapp = tk.Tk()
    left = int((mainapp.winfo_screenwidth()-x)/2)
    top = int((mainapp.winfo_screenheight()-y)/2.5)
    mainapp.geometry(f"{x}x{y}+{left}+{top}")
    mainapp.title("e_manager")
    mainapp.resizable(False, False)
    mainapp.iconphoto(True, tk.PhotoImage(file="gui\\icon.png"))

    global canvasn
    canvasn = tk.Canvas(mainapp, bg="white", width=x, height=y)

    bgpath = dealmaingui(x, y)
    bg = tk.PhotoImage(file=bgpath)
    canvasn.create_image(int(x*0.5), int(y*0.5), anchor="center", image=bg)

    hellopath = dealhellopic(x, y)
    hp = tk.PhotoImage(file=hellopath)
    global hello
    hello = canvasn.create_image(int(y/16*3), 0, anchor="nw", image=hp)

    headphotopath = dealheadimage(y)
    headp = tk.PhotoImage(file=headphotopath)
    canvasn.create_image(int(y/16*0.45), int(y/16*0.45), anchor="nw", image=headp)

    canvasn.pack()

    glovar.hellos = True

    next(mainapp, y, x)

    mainapp.mainloop()