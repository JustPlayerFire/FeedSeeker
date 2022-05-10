import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    group_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    bad_hashtags = sqlalchemy.Column(sqlalchemy.String, nullable=True)