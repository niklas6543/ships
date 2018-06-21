#!/user/bin/python3.5

import db
import Player
import os
import time

TABLE_NAME = "tbl_users"
COOKIE_LENGHT = 128
COOKIE_TIMEOUT_SECONDS = 1

class SessionManager(object):
    """manage the userenities."""
    def __init__(self):
        super(SessionManager, self).__init__()
        self.db = db.DBHandle()

    def clearSessions(self):
        try:
            rotineCurser = self.db.getCurser()
            rotineCurser.callproc('clearSessions', [COOKIE_TIMEOUT_SECONDS])
            rotineCurser.close()
        except Exception as e:
            raise

    def getAvailableUsers(self):
        users = []
        sql = "SELECT * FROM " + TABLE_NAME
        try:
            # stored procdure hat delete session older than now - COOKIE_TIMEOUT_SECONDS
            self.clearSessions()
            cursor = self.db.getCurser()
            cursor.execute(sql)
            results = cursor.fetchall()
            users = SessionManager.parseRows(results)
            cursor.close()
        except Exception as e:
            raise

        return users

    def startSession(self, player):
        player.setSessionStart(time.strftime('%Y-%m-%d %H:%M:%S'))
        sql = "INSERT INTO " + TABLE_NAME + "(name, cookie, session_start) VALUES(%s, %s, %s)"
        cursor = self.db.getCurser()
        cookie = os.urandom(COOKIE_LENGHT)
        player.setCookie(SessionManager.encodeCookie(cookie))
        try:
            cursor.execute(sql, [player.getName(), player.getCookie(), player.getSessionStart()])
            self.db.getDatabaseHandle().commit()
        except Exception as e:
            # Rollback in case there is any error
            self.db.getDatabaseHandle().rollback()
            raise

    def getPlayerByCookie(self, cookie):
        users = []
        sql = "SELECT * FROM " + TABLE_NAME + " WHERE cookie = %s"
        try:
            self.clearSessions()
            cookieCurser = self.db.getCurser()
            cookieCurser.execute(sql, [SessionManager.encodeCookie(cookie)])
            results = cookieCurser.fetchall()
            users = SessionManager.parseRows(results)
            #cookieCurser.close()
        except Exception as e:
            raise

        return users

    # @param is a iterable from row @see parseRow.
    # @return a list of the parses Players.
    @staticmethod
    def parseRows(results):
        users = []
        for row in results:
            users.append(SessionManager.parseRow(row))
        return users

    # @param row is a sesult set from SELECT * FROM tbl_users
    # @retun a parses player object
    @staticmethod
    def parseRow(row):
        return Player.Player(id=row[0], name=row[1], sessionStart=row[2], cookie=row[3])



    # @param cookie the raw bytes from the random function
    # @return the string to write from the database in the player instance.
    @staticmethod
    def encodeCookie(cookie):
        return cookie


    # @param cookie raw data from the database
    # @return the string to write from player instance in the database.
    @staticmethod
    def decodeCookie(cookie):
        return cookie

    def close(self):
        self.db.close()
