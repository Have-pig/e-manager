from PIL import Image
import readpic
from random import randint
import os

def getimage(winW, winH):
    piclist = readpic.piclist()
    pic = piclist[randint(0, len(piclist)-1)]
    pic = "picture\\"+pic
    useimage = Image.open(pic)

    if (useimage.width/useimage.height) > (winW/winH):
        wless = True
    else:
        wless = False

    if wless:
        y = useimage.height
        x = int(y*winW/winH)
    else:
        x = useimage.width
        y = int(x*winH/winW)
    
    if wless:
        box = (int((useimage.width-x)/2), 0,int((useimage.width+x)/2), y)
    else:
        box = (0, int((useimage.height-y)/2), x, int((useimage.height+y)/2))

    dealimage = useimage.resize((winW, winH), box=box)
    
    filepath = os.getcwd()+"\\bgused.png"
    dealimage.save(filepath)

    return filepath