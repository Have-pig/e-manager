import os

def piclist():
    filelist = os.listdir('picture')
    
    r = []
    for i in filelist:
        r.append(i)

    return r