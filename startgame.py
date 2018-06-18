#!/usr/bin/python3.5

# This is the entry point for the backend.
# This is the place to get avilable players and to login.

from tornado import template, ioloop, web
import json
from functions.BattleField import *



class CheckerHandler(web.RequestHandler):
    @web.asynchronous
    def get(self):
        print(self.get_argument('showPlayers'))
        if not self.get_secure_cookie("mycookie"):
            self.set_secure_cookie("mycookie", "myvalue")
        #print("pi1 " + str(pi1))
        #do_find_one(self,pi1)
        d = {
            'first_name': 'Guido',
            'second_name': 'Rossum',
            'titles': ['BDFL', 'Developer'],
        }

        self.write(json.dumps(d))
        self.finish()  # Without this the client's request will hang

if __name__ == "__main__":
    application = web.Application([
        (r"/", CheckerHandler),
    ])
    application.listen(4444)
    ioloop.IOLoop.current().start()
