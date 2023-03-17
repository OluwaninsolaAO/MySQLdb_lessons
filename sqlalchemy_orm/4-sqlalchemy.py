#!/usr/bin/env python3
"""
For the purpose of letting some basic terms stick,
base_models will not be used in this script at all.

This script uses sqlalchemy to model a database,
create the necessary objects and then update the
database with data.
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import sessionmaker

Base = sqlalchemy.orm.declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker()
session = Session(bind=engine)

class User(Base):
    """
    Defines a simple table structure for users with the
    following fields:
    + id (Integer)
    + name (String(50))
    + age (Integer)
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        """
        A simple representation of the class instance.
        """
        return "[User({}) <name: {}> <age: {}>]".format(self.id, self.name, self.age)

# Create table in database
Base.metadata.create_all(engine)

# Create first user
user_a = User(name='Abraham', age='100')
print(user_a)

# Create second user
user_b = User(name='Sarah', age='90')

# Add users to a pending state, meaning the data has
# not yet been associated to a row in the database
session.add(user_a)
session.add(user_b)

# query user
result = session.query(User).filter_by(name='Abraham').first()
print(result)
