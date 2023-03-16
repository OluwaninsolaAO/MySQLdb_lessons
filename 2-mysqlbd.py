#!/usr/bin/env python3
"""
Multiple Substitution Query.
"""

from db_connect import db

cur = db.cursor()
cur.execute("SELECT * FROM users WHERE id = %s OR id = %s", ( 2 , 3 ))
