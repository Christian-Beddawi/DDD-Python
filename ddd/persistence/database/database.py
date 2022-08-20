# import sqlalchemy as db
# from sqlalchemy import create_engine
import datetime

from mongoengine import *

# *******SQLAlchemy*******
"""engine = create_engine('sqlite:///college.db', echo=True)
metadata = db.MetaData()
Student = db.Table('students', metadata, autoload=True, autoload_with=engine)"""


# *******MongoEngine*******
class Students(DynamicDocument):
    id: IntField()
    first_name: StringField(required=True)
    last_name: StringField(required=True)
    dob: datetime

    def _init__(self, first_name, last_name, id=None, dob=None):
        self.id = id,
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
"""
Base = automap_base()
#engine, suppose it has two tables 'user' and 'address' set up
db_engine_creator = Container.Container.db_engine()
engine = db_engine_creator.create_engine_once("sqlite:///college.db")
#reflect the tables
Base.prepare(engine, reflect=True)
#mapped classes are now created with names by default
#matching that of the table name.
student = Base.classes.students
"""
