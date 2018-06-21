#!/usr/bin/python3.5

# This is the entry point for the backend.
# This is the place to get avilable players and to login.

from tornado import template, ioloop, web
import json
#from functions.BattleField import *
from functions import SessionManager
from functions import Player



class CheckerHandler(web.RequestHandler):

    def initialize(self):
        self.sessionManager = SessionManager.SessionManager()

    def on_finish(self):
        self.sessionManager.close()

    @web.asynchronous
    def post(self):
        print("nice")
        if self.get_argument('name', default=None) is not None:
            print(self.get_argument('name', default=None))
            player = Player.Player(name=self.get_argument('name'))
            self.sessionManager.startSession(player)
            #self.set_secure_cookie(SessionManager.COOKIE_NAME, player.getCookie())
        self.finish()

    @web.asynchronous
    def get(self):
        #print(self.get_argument('show'))

        if self.get_argument('show',  default=None) is not None:
            players = self.sessionManager.getAvailableUsers()
            for player in players:
                self.write(json.dumps(player.toPublicJson()))
        else:
            d = True

        #if not self.get_secure_cookie("mycookie"):
            #self.set_secure_cookie("mycookie", "myvalue")


        self.finish()  # Without this the client's request will hang

if __name__ == "__main__":
    application = web.Application([
        (r"/", CheckerHandler),
    ])
    application.listen(4444)
    ioloop.IOLoop.current().start()
