#!/usr/bin/python3.5

import MySQLdb

server = "localhost"
username = "battleship"
password = "test123"
databasename = "db_battleship"

class DBHandle(object):
    """docstring for DBHandle."""
    def __init__(self):
        self.db = MySQLdb.connect(server, username, password, databasename)

    def getCurser(self):
        return self.db.cursor()

    # to disconnect from server
    def close(self):
        self.db.close()

    def getDatabaseHandle(self):
        return self.db
