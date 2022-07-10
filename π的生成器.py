
#===导入模块===
import tkinter
import random
import math

#===创建窗口===
win=tkinter.Tk()
win.geometry('400x180')
win.title('π自定义生成器')

#===输入输出的创建和归零===
write_seed=tkinter.StringVar()
write_seed.set('')
look_str=tkinter.StringVar()
look_str.set('')

#===定义蒙特卡洛算法函数===
def startloading():
    a=write_seed.get()
    a=int(a)
    import random
    import math
    b=0
    for i in range(1,int(a)+1):
        x=random.random()
        y=random.random()
        c=math.sqrt(x**2+y**2)
        if c<=1:
            b+=1
    d=4*(b/a)
    look_str.set(d)

#===定义退出按钮===
def _quit():
    win.quit()
    win.destroy()

#===定义清空按钮===
def delss():
    write_seed.set('')
    look_str.set('')

#===窗口设计===
#--标注文本--
str_one=tkinter.Label(win,text='投点数：',width=80)
str_two=tkinter.Label(win,text='输出口：',width=80)
str_three=tkinter.Label(win,text='就是个屑py',width=80)
str_four=tkinter.Label(win,text='无输入值就计算，后台报错',width=100)
#--输入框--
a_input=tkinter.Entry(win,width=270,textvariable=write_seed)
b_input=tkinter.Entry(win,width=270,textvariable=look_str)
#--设计3个按钮--
quitss=tkinter.Button(win,text='退出',command=_quit)
delsss=tkinter.Button(win,text='清空',command=delss)
star=tkinter.Button(win,text='计算',command=startloading)
#--窗口布局--
str_one.place(x=20,y=20,width=80,height=20)
str_two.place(x=20,y=50,width=80,height=20)

str_three.place(x=310,y=150,width=80,height=20)
str_four.place(x=235,y=130,width=150,height=20)

a_input.place(x=110,y=20,width=270,height=20)
b_input.place(x=110,y=50,width=270,height=20)
quitss.place(x=20,y=90,width=110,height=30)
delsss.place(x=270,y=90,width=110,height=30)
star.place(x=145,y=90,width=110,height=30)

#===进入消息循环===
win.mainloop

