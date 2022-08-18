from sqlalchemy import create_engine


class EngineCreator:
    def __init__(self, config):
        self.config = config

    def create_engine_once(self):
        engine = create_engine(self.config, echo=True)
        print('self.config', self.config)
        # from seedwork.infrastructure.database import Base
        #
        # # TODO: it seems like a hack, but it works...
        # Base.metadata.bind = engine
        return engine