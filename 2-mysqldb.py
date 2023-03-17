#!/usr/bin/env python3
"""
Multiple Substitution Query.
"""

from db_connect import db

cur = db.cursor()
cur.execute("SELECT * FROM users WHERE id BETWEEN %s AND %s", ( 5 , 15 ))
rows = cur.fetchall()
for row in rows:
	print(row)
cur.close()  # close all cursors
db.close()  # close all databases
