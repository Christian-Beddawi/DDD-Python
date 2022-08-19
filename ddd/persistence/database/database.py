import sqlalchemy as db
from sqlalchemy import create_engine


engine = create_engine('sqlite:///college.db', echo=True)

conn = engine.connect()

metadata = db.MetaData()
Student = db.Table('students', metadata, autoload=True, autoload_with=engine)


# Base = automap_base()
# engine, suppose it has two tables 'user' and 'address' set up
#db_engine_creator = Container.Container.db_engine()
#engine = db_engine_creator.create_engine_once("sqlite:///college.db")
# reflect the tables
#Base.prepare(engine, reflect=True)
# mapped classes are now created with names by default
# matching that of the table name.
#Student = Base.classes.students
