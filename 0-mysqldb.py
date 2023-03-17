#!/usr/bin/env python3
"""
Create a simple table using the db object.
Table Name: users
Fields: id and name
"""

from db_connect import db  # imports db from db_connect

cur = db.cursor()  # get a default cursor class
cur.execute("CREATE TABLE IF NOT EXISTS users ( id INT PRIMARY KEY AUTO_INCREMENT, name CHAR(255) NOT NULL )")  # executes mysql query
cur.close()  # close all cursors
db.close()  # close all databases
