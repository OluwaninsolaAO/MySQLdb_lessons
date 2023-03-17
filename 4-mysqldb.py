#!/usr/bin/env python3
"""Fetch One-at-a-Time"""

from db_connect import db

cur = db.cursor()
cur.execute("SELECT * FROM users WHERE id = %s", (15,))
result = cur.fetchone()
print("id: {} -- name: {}".format(result[0], result[1]))
cur.close()  # close all cursors
db.close()  # close all databases
