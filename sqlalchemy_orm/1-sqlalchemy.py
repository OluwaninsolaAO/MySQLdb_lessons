#!/usr/bin/env python3

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)
Base = sqlalchemy.orm.declarative_base()

print(type(engine))
print(engine)
print(type(Base))
print(Base)
