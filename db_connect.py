#!/usr/bin/env python3
"""
This file connects to MySQLdb and creates a `db` object,
written once and can be used and reused anywhere in the
project.
"""

import MySQLdb

db = MySQLdb.connect(host='localhost', user='superuser', password='superuser', db='test_db')
