import tkinter as tk
from win32api import GetSystemMetrics
import dealbgpic
import dealPic
import createaccount
from enterd import check


def start():
    entrance = tk.Tk()
    entrance.title("Hello!")

    width = int(int(GetSystemMetrics(0))*0.6)
    height = int(int(GetSystemMetrics(1))*0.6)
    entrance.resizable(False, False)

    entrance.geometry("{0}x{1}".format(width, height))
    entrance.iconphoto(True, tk.PhotoImage(file='gui\\icon.png'))

    bgfile = dealbgpic.getimage(width, height)
    canvasn = tk.Canvas(entrance, bg='white', height=height, width=width)
    images = tk.PhotoImage(file=bgfile)
    canvasn.create_image(0,0, anchor='nw', image=images)

    loginpath = dealPic.getPic(height, "gui\\LogIn.png")
    logpic = tk.PhotoImage(file=loginpath)
    logx = int(width*0.5)
    logy = int(height*0.5)
    canvasn.create_image(logx, logy, anchor='center', image=logpic)
    canvasn.pack()

    in_name = tk.Entry(entrance, bg="white", fg="blue", width=int(width/29))
    in_word = tk.Entry(entrance, bg="white", show="*", fg="blue", width=int(width/29))

    in_name.place(x=int(width*0.442), y=int(height*0.41))
    in_word.place(x=int(width*0.442), y=int(height*0.519))

    enterd = tk.Button(entrance, text="    Go!    ", bg="white", fg="red", relief='flat', command=lambda:check(entrance, width, height, in_name.get(), in_word.get()))
    signup = tk.Button(entrance, text="A new account?", bg="white", fg="red", relief='flat', command=lambda:createaccount.create(entrance))

    enterd.place(x=int(width*0.618), y=int(height*0.615))
    signup.place(x=int(width*0.32), y=int(height*0.615))

    entrance.mainloop()
