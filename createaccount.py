import tkinter as tk
import dealPic
from win32api import GetSystemMetrics
import saveuserinfojson


def warn(win, x, y):
    warninfo = tk.Label(win, bg="white", text="The passwords are different", fg="orange")
    warninfo.place(x=int(x*0.05), y=int(y*0.84))

def noemptyname(win, x, y):
    warnname = tk.Label(win, bg="white", text='The "name" shouldn`t be empty', fg="orange")
    warnname.place(x=int(x*0.37), y=int((y*0.34)))

def done(win,x,y):
    donenotice = tk.Label(win, bg="white", text="Saved! Restart to log in", fg="green")
    donenotice.place(x=int(x*0.46), y=int(y*0.84))

def noemptypass(win, x, y):
    warnpass = tk.Label(win, bg="white", text='The "password" shouldn`t be empty', fg="orange")
    warnpass.place(x=int(x*0.37), y=int(y*0.56))

def checkinfo(win, x, y, username, pass1, pass2):
    if (pass1==pass2) and (username != "") and (pass1 != ""):
        saveuserinfojson.saveinfo(username, pass1)
        done(win, x, y)
    elif username == "":
        noemptyname(win, x, y)
    elif (pass1 == "") or (pass2 == ""):
        noemptypass(win, x, y)
    else:
        warn(win, x, y)


def create(win):

    win.destroy()

    newscreen = tk.Tk()
    newscreen.title("Welcome!")

    height = int(int(GetSystemMetrics(1))*0.6)
    realH = int(height*0.5)
    realW = int(realH/2*3)
    newscreen.geometry("{0}x{1}".format(realW, realH))
    newscreen.resizable(False, False)
    newscreen.iconphoto(False, tk.PhotoImage(file='gui\\newicon.png'))
    
    canvasn = tk.Canvas(newscreen, width=realW, height=realH)

    newaccpicfilepath = dealPic.getPic(height, "newacc.png")
    pic = tk.PhotoImage(file=newaccpicfilepath)
    canvasn.create_image(0,0, anchor="nw", image=pic)

    canvasn.pack()

    in_name = tk.Entry(newscreen, bg="white", fg="blue", width=int(height/16.4), bd=0)
    in_word = tk.Entry(newscreen, bg="white", show="*", fg="blue", width=int(height/16.4), bd=0)
    in_word2 = tk.Entry(newscreen, bg="white", show="*", fg="blue", width=int(height/16.4), bd=0)

    in_name.place(x=int(realW*0.362), y=int(realH*0.254))
    in_word.place(x=int(realW*0.362), y=int(realH*0.465))
    in_word2.place(x=int(realW*0.362), y=int(realH*0.671))

    SaveInfo = tk.Button(newscreen, text="Create!", bg="white", fg="red", relief='flat', command=lambda:checkinfo(newscreen, realW, realH, in_name.get(), in_word.get(), in_word2.get()))
    SaveInfo.place(x=int(realW*0.81), y=int(realH*0.82))

    newscreen.mainloop()
