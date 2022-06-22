import json


def check(username, password):
    alluser = json.load("usernfo.json")
    usernames = alluser.key()
    passwords = alluser.value()