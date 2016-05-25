# -*- coding: utf-8 -*-
import sqlite3
def init():
    global DB_CONN, DB_URI
    DB_URI = './db/testCase.db' #For each function to operation database
    DB_CONN = sqlite3.connect('./db/testCase.db')
    pass
