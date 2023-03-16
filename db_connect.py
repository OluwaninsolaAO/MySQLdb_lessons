#!/usr/bin/env python3
import MySQLdb

db = MySQLdb.connect(host='localhost', user='superuser', password='superuser', db='test_db')
cur = db.cursor()
