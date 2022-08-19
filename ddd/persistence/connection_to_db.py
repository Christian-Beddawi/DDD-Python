from sqlalchemy import create_engine


class ConnectionCreator:
    def __init__(self, config):
        self.config = config
        engine = create_engine(self.config, echo=True)
        self.conn = engine.connect()
