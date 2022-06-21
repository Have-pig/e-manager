import tkinter as tk
from win32api import GetSystemMetrics
import dealpic
import loginPic

def start():
    entrance = tk.Tk()
    entrance.title("hello!")

    width = int(int(GetSystemMetrics(0))*0.6)
    height = int(int(GetSystemMetrics(1))*0.6)
    entrance.resizable(False, False)

    entrance.geometry("{0}x{1}".format(width, height))
    entrance.iconphoto(True, tk.PhotoImage(file='icon.png'))

    bgfile = dealpic.getimage(width, height)
    canvasn = tk.Canvas(entrance, bg='white', height=height, width=width)
    images = tk.PhotoImage(file=bgfile)
    canvasn.create_image(0,0, anchor='nw', image=images)

    loginpath = loginPic.getLogInPic(width, height)
    logpic = tk.PhotoImage(file=loginpath)
    logx = int(width*0.5)
    logy = int(height*0.5)
    canvasn.create_image(logx, logy, anchor='center', image=logpic)
    canvasn.pack()

    in_name = tk.Entry(entrance, bg="white", fg="blue", width=int(width/29))
    in_word = tk.Entry(entrance, bg="white", show="*", fg="blue", width=int(width/29))

    in_name.place(x=int(width*0.442), y=int(height*0.406))
    in_word.place(x=int(width*0.442), y=int(height*0.516))

    entrance.mainloop()
