import tkinter as tk
import dealbgpic
import dealPic
import createaccount
from enterd import check
from os.path import isfile, exists
from os import makedirs


def start():
    if not(exists("used")):
        makedirs("used")
    if not(isfile("option.json")):
        f = open("option.json", "w")
        f.write("{}")
        f.close()
    if not(isfile("userinfo.json")):
        f = open("userinfo.json", "w")
        f.write("{}")
        f.close()
    else:
        with open("userinfo.json", "r") as fl:
            fll = str(fl.read())
            if len(fll) < 2:
                rewrite = True
            elif (fll[0] != "{") or (fll[-1] != "}"):
                rewrite = True
            else:
                rewrite = False
        if rewrite:
            with open("userinfo.json", "w") as f:
                f.write("{}")

    entrance = tk.Tk()
    entrance.title("Hello!")

    width = int(entrance.winfo_screenwidth()*0.6)
    height = int(entrance.winfo_screenheight()*0.6)
    entrance.resizable(False, False)

    left = int((entrance.winfo_screenwidth()-width)/2)
    top = int((entrance.winfo_screenheight()-height)/2.5)
    entrance.geometry(f"{width}x{height}+{left}+{top}")
    entrance.iconphoto(True, tk.PhotoImage(file='gui\\icon.png'))

    bgfile = dealbgpic.getimage(width, height)
    canvasn = tk.Canvas(entrance, bg='white', height=height, width=width)
    images = tk.PhotoImage(file=bgfile)
    canvasn.create_image(0,0, anchor='nw', image=images)

    loginpath = dealPic.getPic(height, "LogIn.png")
    logpic = tk.PhotoImage(file=loginpath)
    logx = int(width*0.5)
    logy = int(height*0.5)
    canvasn.create_image(logx, logy, anchor='center', image=logpic)
    canvasn.pack()

    in_name = tk.Entry(entrance, bg="white", fg="blue", width=int(width/29), bd=0)
    in_word = tk.Entry(entrance, bg="white", show="*", fg="blue", width=int(width/29), bd=0)

    in_name.place(x=int(width*0.442), y=int(height*0.41))
    in_word.place(x=int(width*0.442), y=int(height*0.519))

    enterd = tk.Button(entrance, text="    Go!    ", bg="white", fg="red", relief='flat', command=lambda:check(entrance, width, height, in_name.get(), in_word.get()))
    signup = tk.Button(entrance, text="A new account?", bg="white", fg="red", relief='flat', command=createaccount.create)

    enterd.place(x=int(width*0.618), y=int(height*0.615))
    signup.place(x=int(width*0.32), y=int(height*0.615))

    entrance.mainloop()