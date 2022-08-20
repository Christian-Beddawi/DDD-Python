from mongoengine import connect
# from sqlalchemy import create_engine


class ConnectionCreator:
    def __init__(self, db_path):
        # SQL
        """engine = create_engine(db_path, echo=True)
        self.conn = engine.connect()"""
        # MongoDB
        connect(host=db_path)

