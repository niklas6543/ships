#!/usr/bin/python3.5

class Player(object):
    """
    docstring for Player.
    A entity Class for the session handling.
    """
    def __init__(self, name, id=None, cookie=None, sessionStart=None):
        self.name = name
        self.id = id
        self.cookie = cookie
        self.sessionStart = sessionStart

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getSessionStart(self):
        return self.sessionStart

    def getCookie(self):
        return self.cookie

    def setCookie(self, cookie):
        self.cookie = cookie

    def setSessionStart(self, sessionStart):
        self.sessionStart = sessionStart

    def toPublicJson(self):
        re = {
            'id' : self.getId(),
            'name' : self.getName()
        }
        return re
