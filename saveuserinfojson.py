import json
from random import randint
import hbdalfhb665g


def saveinfo(username, password):

    thistype = randint(0, 2)
    if thistype == 0:
        dealpassword = hbdalfhb665g.adadasdg(password)
    elif thistype == 1:
        dealpassword = hbdalfhb665g.oiuyfyiohiu(password)
    else:
        dealpassword = hbdalfhb665g.aouifvafa(password)

    with open("userinfo.json", "r") as f:
        jsons = json.load(f)

    with open("userinfo.json", "w") as f:
        jsons["user{0}".format(username)] = {"password":dealpassword, "type":thistype}
        json.dump(jsons, fp=f, indent=4, ensure_ascii=False)