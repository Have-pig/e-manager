import json
from random import randint
import hbdalfhb665g


def saveinfo(username, password):

    thistype = randint(0,2)
    if thistype == 0:
        dealpassword = hbdalfhb665g.adadasdg(password)
    elif thistype == 1:
        dealpassword = hbdalfhb665g.oiuyfyiohiu(password)
    else:
        dealpassword = hbdalfhb665g.aouifvafa(password)

    with open("userinfo.json", "r") as f:
        jsons = json.load(f)
        jsonreal = str(jsons)
        jsonlong = len(jsonreal)
        if jsonlong == 0:
            firsttimes = True
        else:
            firsttimes = False

    with open("userinfo.json", "w") as f:
        if firsttimes:
            json.dump({"user{0}".format(username):{"username":username, "password":dealpassword, "type":thistype}}, fp=f, indent=4)
        else:
            jsons["user{0}".format(username)] = {"username":username, "password":dealpassword, "type":thistype}
            json.dump(jsons, fp=f, indent=4)