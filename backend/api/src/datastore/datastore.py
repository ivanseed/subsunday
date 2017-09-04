from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, mapper, scoped_session

from .mappings import all_mappings


class DataStore:

    def __init__(self, uri):
        self.metadata = MetaData()

        for mapping in all_mappings:
            cls, table = mapping(self.metadata)
            mapper(cls, table)

        self.engine = create_engine(uri)

        Session = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )
        self.session = Session()

    def populate(self):
        self.metadata.drop_all(self.engine)
        self.metadata.create_all(self.engine)
