#!/usr/bin/env python3
"""
This script describes some fixed variables that will be used
accross all other example scripts in this project.
"""
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = sqlalchemy.orm.declarative_base()
engine = create_engine('sqlite:///:memory:')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return "[User: <name: {}> <age: {}>".format(self.name, self.age)
