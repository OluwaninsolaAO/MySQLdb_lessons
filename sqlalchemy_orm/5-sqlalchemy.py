#!/usr/bin/env python3
"""Add multiple objects at once into the database/Update Object"""

from base_model import User
from base_model import Session

# create a local session, can as well be in base_model
session = Session()

session.add_all([
    User(name='Abraham', age='100'),
    User(name='Sarah', age='90'),
    User(name='Isaac', age='0')
    ])

# Show all pending data waiting to be commited
print("Pending: {}".format(session.new))

# Retrieve Isaac and update his age to `1`
Isaac = session.query(User).filter_by(name='Isaac').first()
print("Our Isaac: {}".format(Isaac))
Isaac.age = 1
print("New Changes: {}".format(session.dirty))

# Save new changes
session.commit()
