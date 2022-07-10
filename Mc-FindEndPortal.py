import tkinter
import webbrowser as web


def find(x, y, x1, y1, x2, y2, x3, y3):
    """计算两个一次函数的交点以寻找末地传送门"""
    if x == x1 and x2 == x3:
        return "数据错误!"
    elif y == y1 and y2 == y3:
        return "数据错误!"
    elif x == x1 and y2 == y3:
        return [x, "&", y2]
    elif x2 == x3 and y == y1:
        return [x2, "&", y]
    elif x == x1:
        k2 = (y2 - y3) / (x2 - x3)
        b2 = y2 - k2 * x2
        y0 = k2 * x + b2
        return [x, "&", y0]
    elif x2 == x3:
        k1 = (y - y1) / (x - x1)
        b1 = y - k1 * x
        y0 = k1 * x2 + b1
        return [x2, "&", y0]
    elif y == y1:
        k2 = (y2 - y3) / (x2 - x3)
        b2 = y2 - k2 * x2
        x0 = (y - b2) / k2
        return [x0, "&", y]
    elif y2 == y3:
        k1 = (y - y1) / (x - x1)
        b1 = y - k1 * x
        x0 = (y2 - b1) / k1
        return [x0, "&", y2]
    else:
        k1 = (y - y1) / (x - x1)
        b1 = y - k1 * x
        k2 = (y2 - y3) / (x2 - x3)
        b2 = y2 - k2 * x2
        if k1 == k2:
            return "函数不可解!"
        else:
            x0 = round((b2 - b1) / (k1 - k2), 1)
            y0 = round(k1 * x0 + b1, 1)
            return ["(", x0, "&", y0, ")"]


def go():
    """前往b站"""
    web.open("https://space.bilibili.com/341976143")


def start():
    """开始程序主体"""
    windows = tkinter.Tk()
    windows.title("FindEndPortal")
    windows.geometry("500x300")
    co_a = tkinter.StringVar()
    co_a.set("")
    co_b = tkinter.StringVar()
    co_b.set("")
    co_c = tkinter.StringVar()
    co_c.set("")
    co_d = tkinter.StringVar()
    co_d.set("")
    co_e = tkinter.StringVar()
    co_e.set("")
    co_f = tkinter.StringVar()
    co_f.set("")
    co_g = tkinter.StringVar()
    co_g.set("")
    co_h = tkinter.StringVar()
    co_h.set("")
    re = tkinter.StringVar()
    re.set("")

    def clean():
        """清除文本框的内容"""
        co_a.set("")
        co_b.set("")
        co_c.set("")
        co_d.set("")
        co_e.set("")
        co_f.set("")
        co_g.set("")
        co_h.set("")
        re.set("")

    def find_x():
        """为find()函数生成环境"""
        a, b, c, d = co_a.get(), co_b.get(), co_c.get(), co_d.get()
        a, b, c, d = float(a), float(b), float(c), float(d)
        e, f, g, h = co_e.get(), co_f.get(), co_g.get(), co_h.get()
        e, f, g, h = float(e), float(f), float(g), float(h)
        sets = find(a, b, c, d, e, f, g, h)
        re.set(sets)

    tlt = tkinter.Label(windows, text="Minecraft-FindEndPortal", font=("Arial", 15), height=2)
    coo_a = tkinter.Label(windows, text="throw one(x):", font=5)
    coo_b = tkinter.Label(windows, text="throw one(z):", font=5)
    coo_c = tkinter.Label(windows, text=" drop one(x):", font=5)
    coo_d = tkinter.Label(windows, text=" drop one(z):", font=5)
    coo_e = tkinter.Label(windows, text="throw two(x):", font=5)
    coo_f = tkinter.Label(windows, text="throw two(z):", font=5)
    coo_g = tkinter.Label(windows, text=" drop two(x):", font=5)
    coo_h = tkinter.Label(windows, text=" drop two(z):", font=5)
    notice = tkinter.Label(windows, text="""Thanks for using!
        -by HavePig""")
    helps = tkinter.Label(windows, text="""How to use?
    1.Enter the coordinates of the first throw
    2.Enter the coordinates of the first drop
    3.Repeat and enter again""")
    v = tkinter.Label(windows, text="V1.0")
    re_n = tkinter.Label(windows, text=" return(x&z):", font=5)
    b_a = tkinter.Button(windows, text="清除", command=clean)
    b_b = tkinter.Button(windows, text="计算", command=find_x)
    b_c = tkinter.Button(windows, text="HAVE_PIG@bilibili", command=go)
    w_a = tkinter.Entry(windows, textvariable=co_a)
    w_b = tkinter.Entry(windows, textvariable=co_b)
    w_c = tkinter.Entry(windows, textvariable=co_c)
    w_d = tkinter.Entry(windows, textvariable=co_d)
    w_e = tkinter.Entry(windows, textvariable=co_e)
    w_f = tkinter.Entry(windows, textvariable=co_f)
    w_g = tkinter.Entry(windows, textvariable=co_g)
    w_h = tkinter.Entry(windows, textvariable=co_h)
    re_a = tkinter.Entry(windows, textvariable=re)
    tlt.place(x=145, width=210)
    coo_a.place(x=10, width=100, y=40)
    coo_b.place(x=259, width=100, y=40)
    coo_c.place(x=10, width=100, y=60)
    coo_d.place(x=259, width=100, y=60)
    coo_e.place(x=10, width=100, y=80)
    coo_f.place(x=259, width=100, y=80)
    coo_g.place(x=10, width=100, y=100)
    coo_h.place(x=259, width=100, y=100)
    helps.place(x=200, width=260, y=175)
    notice.place(x=393, width=100, y=261)
    v.place(x=-2, width=35, y=280)
    re_n.place(x=10, width=100, y=140)
    b_a.place(x=30, width=70, y=180)
    b_b.place(x=110, width=70, y=180)
    b_c.place(x=50, width=115, y=220)
    w_a.place(x=110, width=130, y=40)
    w_b.place(x=360, width=130, y=40)
    w_c.place(x=110, width=130, y=60)
    w_d.place(x=360, width=130, y=60)
    w_e.place(x=110, width=130, y=80)
    w_f.place(x=360, width=130, y=80)
    w_g.place(x=110, width=130, y=100)
    w_h.place(x=360, width=130, y=100)
    re_a.place(x=110, width=380, y=140)
    tkinter.mainloop()


if __name__ == '__main__':
    start()
