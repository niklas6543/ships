#!/usr/bin/python3.5

# This is a test for the SessionManager
# if the database is not empty for before this test if mybe fails

from inspect import getsourcefile
import os.path
import sys

# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

import SessionManager
import Player
import time

print("creating sessionManager")
sessionManager = SessionManager.SessionManager()


print("list available users") # doing this first to clear old sessions
for user in sessionManager.getAvailableUsers():
    print('\tid ' + str(user.getId()))
    print('\tname ' + user.getName())
    print('\tcookie lenght ' + str(len(user.getCookie())))
    print('\tsessionStart ' + str(user.getSessionStart()) + '\n')

print("creating 3 players")
player0 = Player.Player(None, "testUser0", None, time.time())
player1 = Player.Player(None, "testUser1", None, time.time())
player2 = Player.Player(None, "testUser2", None, time.time())

print("starts a session for each of them")
sessionManager.startSession(player0)
sessionManager.startSession(player1)
sessionManager.startSession(player2)

print("list available users")
for user in sessionManager.getAvailableUsers():
    print('\tid ' + str(user.getId()))
    print('\tname ' + user.getName())
    print('\tcookie lenght ' + str(len(user.getCookie())))
    print('\tsessionStart ' + str(user.getSessionStart()) + '\n')

print('find user ' + player0.getName() +' by cookie ')

#print(player0.getCookie())
foundPlayer = sessionManager.getPlayerByCookie(player1.getCookie())

print('found ' + str(len(foundPlayer)) + ' players')

if len(foundPlayer) >= 1:
    print('found player ' + foundPlayer[0].getName())
else:
    print("no player found")

print('closing sessionManager')
sessionManager.close()
