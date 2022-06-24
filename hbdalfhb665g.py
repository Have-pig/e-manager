global kv
kv=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def adadasdg(password):
    letter = ""
    number = ""
    for i in password:
        if str(i) not in kv:
            letter += str(i)
        else:
            number += str(i)
    return number+letter

def oiuyfyiohiu(password):
    letter = ""
    number = ""
    for i in password:
        if str(i) not in kv:
            letter += str(i)
        else:
            number += str(i)
    dealletter = ""
    for i in letter[::-1]:
        dealletter += i
    return dealletter+number

def aouifvafa(password):
    letter = ""
    number = ""
    for i in password:
        if str(i) not in kv:
            letter += str(i)
        else:
            number += str(i)
    dealletter = ""
    dealnumber = ""
    for i in letter[::-1]:
        dealletter += i
    for i in number[::-1]:
        dealnumber += i
    return dealnumber+dealletter