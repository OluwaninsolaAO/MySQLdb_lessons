#!/usr/bin/env python3
"""Exceptions & Errors"""

import MySQLdb
from db_connect import db

cur = db.cursor()
try:
	cur.execute("SELECT * FROM outoftheblue")
	rows = cur.fetchall()
	for row in rows:
		print(row)
except MySQLdb.Error as e:
	try:
		print("MySQL Error {}: {}".format(e[0], e[1]))
	except (IndexError, TypeError):
		print("MySQL Error {}".format(e))
