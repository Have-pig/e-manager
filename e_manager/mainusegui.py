import tkinter as tk
from PIL import Image
from os import getcwd
from datetime import datetime
from time import strftime
from mainapp import next


def dealmaingui(x, y):
    paths = "gui\\welcome.png"
    use = Image.open(paths)
    purposesizes = (x, y)
    box = (0, 0, 2560, 1440)
    dealpic = use.resize(purposesizes, box=box)
    filepath = getcwd()+"\\welcomeused.png"
    dealpic.save(filepath)

    return filepath

def dealhellopic(x, y):
    a = datetime.now()
    print(a)
    b = strftime("%H", a)
    print(b)
    hour = int(b)
    print(hour)
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
    filepath = getcwd()+"\\"+name
    dealpic.save(filepath)

    return filepath

def dealheadimage(y):
    paths = "gui\\headimage.png"
    use = Image.open(paths)
    purposesizes = (int(y/16*3), int(y/16*3))
    box = (0, 0, 480, 480)
    dealpic = use.resize(purposesizes, box=box)
    filepath = getcwd()+"\\headimageused.png"
    dealpic.save(filepath)

    return filepath


def use(win, x, y):
    win.destroy()

    mainapp = tk.Tk()
    mainapp.geometry("{0}x{1}".format(x, y))
    mainapp.title("e_manager")
    mainapp.resizable(False, False)
    mainapp.iconphoto(True, tk.PhotoImage(file="icon.png"))
    canvasn = tk.Canvas(mainapp, bg="white", width=x, height=y)
    bgpath = dealmaingui(x, y)
    bg = tk.PhotoImage(file=bgpath)
    canvasn.create_image(int(x*0.5), int(y*0.5), anchor="center", image=bg)
    hellopath = dealhellopic(x, y)
    hp = tk.PhotoImage(file=hellopath)
    canvasn.create_image(int(y/16*3), 0, anchor="nw", image=hp)
    canvasn.pack()
    next(mainapp, x, y)

    mainapp.mainloop()