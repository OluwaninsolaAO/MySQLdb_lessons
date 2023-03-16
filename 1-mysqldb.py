#!/usr/bin/env python3
"""
Execute Insert / Single Substitution Query
"""

from db_connect import db

cur = db.cursor()
users = ['John', 'Maxwell', 'Joel', 'David', 'Abraham']
for user in users:
	cur.execute("INSERT INTO users (name) VALUES (%s)", (user,))
	print("New User: {}, with ID: {}".format(user, cur.lastrowid))
db.commit()
