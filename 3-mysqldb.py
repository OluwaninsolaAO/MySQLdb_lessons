#!/usr/bin/env python3
"""Execute Select"""

from db_connect import db

cur = db.cursor()
numrows = cur.execute("SELECT * FROM users")
print("Selected {} rows".format(numrows))
print("Selected {} rows".format(cur.rowcount))
