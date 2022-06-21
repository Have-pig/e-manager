from PIL import Image
import os

def getLogInPic(winW, winH):
    useimage = Image.open("LogIn.png")
    y = int(winH*0.5)
    x = int((y/2*3))
    purposesize = (x, y)
    box = (0, 0, 1620, 1080)
    dealpic = useimage.resize(purposesize, box=box)
    filepath = os.getcwd()+"\\loginpicused.png"
    dealpic.save(filepath)

    return filepath