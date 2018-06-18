#!/user/bin/python3.5

import db
import Player
import os
import time

TABLE_NAME = "tbl_users"
COOKIE_LENGHT = 128
COOKIE_TIMEOUT_SECONDS = 1

class SessionManager(object):
    """docstring for SessionManager."""
    def __init__(self):
        super(SessionManager, self).__init__()
        self.db = db.DBHandle()

    # TODO untested
    def getAvailableUsers(self):
        users = []
        sql = "SELECT * FROM " + TABLE_NAME
        try:
            # stored procdure hat delete session older than now - COOKIE_TIMEOUT_SECONDS
            rotineCurser = self.db.getCurser()
            rotineCurser.callproc('clearSessions', [COOKIE_TIMEOUT_SECONDS])
            #self.db.getDatabaseHandle.commit()

            cursor = self.db.getCurser()
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                users.append(Player.Player(id=row[0], name=row[1], sessionStart=row[2], cookie=row[3]))
            cursor.close()
        except Exception as e:
            raise

        return users

    # TODO untested
    def startSession(self, player):

        player.setSessionStart(time.strftime('%Y-%m-%d %H:%M:%S'))
        sql = "INSERT INTO " + TABLE_NAME + "(name, cookie, session_start) VALUES(%s, %s, %s)"
        cursor = self.db.getCurser()
        player.setCookie(os.urandom(COOKIE_LENGHT))
        try:
            cursor.execute(sql, (player.getName(), player.getCookie(), player.getSessionStart()))
            self.db.getDatabaseHandle().commit()
        except Exception as e:
            # Rollback in case there is any error
            self.db.getDatabaseHandle().rollback()
            raise

    def close(self):
        self.db.close()
