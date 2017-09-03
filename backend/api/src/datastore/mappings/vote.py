from sqlalchemy import Table, Column, Integer, String

from models import Vote

def vote_mapping(metadata):
    vote_table = Table('vote', metadata,
        Column('id',       Integer,     primary_key=True           ),
        Column('username', String(255), nullable=False, unique=True),
        Column('game',     String(255), nullable=False             ),
    )

    return (Vote, vote_table)
