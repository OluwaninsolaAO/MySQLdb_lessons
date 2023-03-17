Welcome to the SQLAlchemy section of this Github repository! In this section, you will find a detailed lesson plan that will guide you through the process of learning how to use SQLAlchemy.

The lesson plan is organized into several modules, each focusing on a specific aspect of SQLAlchemy. Each module includes a set of exercises and examples that will help you to practice and reinforce the concepts learned in that module.

## Askin ChatGPT: What dependencies/modules do I need to import to use `sqlalchemy.orm.delcarative_base()` in my python programme?

To use sqlalchemy.orm.declarative_base() in your Python program, you need to import the following modules:

```
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
```

Here is a brief description of each of these modules:

+ `declarative_base`: This module provides a base class for declarative class definitions, which is used to define the ORM (Object-Relational Mapping) classes. It is imported from sqlalchemy.ext.declarative.
+ `Column`: This module provides the data types that are used to define the columns in the database tables. It is imported from sqlalchemy.
+ `Integer and String`: These are data types that can be used with the Column module to define the type of data that a particular column can hold. They are also imported from sqlalchemy.
+ `create_engine`: This module creates a new database engine instance. It is imported from sqlalchemy.
+ `sessionmaker`: This module provides a factory for creating new session objects. It is imported from sqlalchemy.orm.


Here is an example of how to use declarative_base():
```
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Example(Base):
    __tablename__ = 'example_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
```

In this example, we define a new declarative class `Example` that inherits from `Base`, which is created using `declarative_base()`. We then define the columns of the `example_table` using the `Column` module, and create a new database `engine` instance using `create_engine()`. Finally, we create a new `session` object using `sessionmaker()`.
