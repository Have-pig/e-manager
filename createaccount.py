import tkinter as tk
import dealPic
import saveuserinfojson
import json


def warn(win, x, y):
    warninfo = tk.Label(win, bg="white", text="The passwords are different", fg="orange")
    warninfo.place(x=int(x*0.05), y=int(y*0.84))
    dellist.append(warninfo)

def noemptyname(win, x, y):
    warnname = tk.Label(win, bg="white", text='The "name" shouldn`t be empty', fg="orange")
    warnname.place(x=int(x*0.37), y=int((y*0.34)))
    dellist.append(warnname)

def done(win,x,y):
    donenotice = tk.Label(win, bg="white", text="Saved! Close to log in", fg="green")
    donenotice.place(x=int(x*0.46), y=int(y*0.84))
    dellist.append(donenotice)

def noemptypass(win, x, y):
    warnpass = tk.Label(win, bg="white", text='The "password" shouldn`t be empty', fg="orange")
    warnpass.place(x=int(x*0.37), y=int(y*0.56))
    dellist.append(warnpass)

def acchasbeen(win, x, y):
    warnexistence = tk.Label(win, bg="white", text="The account has been created", fg="orange")
    warnexistence.place(x=int(x*0.291), y=int(y*0.82))
    dellist.append(warnexistence)

def checkinfo(win, x, y, username, pass1, pass2):
    if dellist:
        for i in dellist:
            i.destroy()

    with open("userinfo.json") as f:
        jsons = json.load(f)
        userlist = jsons.keys()
        userlist = list(userlist)

    if "user"+username in userlist:
        acchasbeen(win, x, y)
    elif (pass1==pass2) and (username != "") and (pass1 != ""):
        saveuserinfojson.saveinfo(username, pass1)
        done(win, x, y)
    elif username == "":
        noemptyname(win, x, y)
    elif (pass1 == "") or (pass2 == ""):
        noemptypass(win, x, y)
    else:
        warn(win, x, y)

def create():
    global dellist
    dellist = []
    newscreen = tk.Toplevel()
    newscreen.title("Welcome!")

    height = int(newscreen.winfo_screenheight()*0.6)
    realH = int(height*0.5)
    realW = int(realH/2*3)
    left = int((newscreen.winfo_screenwidth()-realW)/2)
    top = int((newscreen.winfo_screenheight()-realH)/2.15)
    newscreen.geometry(f"{realW}x{realH}+{left}+{top}")
    newscreen.resizable(False, False)
    newscreen.iconphoto(True, tk.PhotoImage(file='gui\\icon.png'))
    
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