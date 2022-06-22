from PIL import Image
import os


def getPic(winH, files):
    useimage = Image.open(files)
    y = int(winH*0.5)
    x = int((y/2*3))
    purposesize = (x, y)
    box = (0, 0, 1620, 1080)
    dealpic = useimage.resize(purposesize, box=box)
    filepath = os.getcwd()+"\\"+files+"used.png"
    dealpic.save(filepath)

    return filepath