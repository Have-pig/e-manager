from os import listdir

def piclist():
    filelist = listdir('picture')
    
    r = []
    for i in filelist:
        r.append(i)

    return r