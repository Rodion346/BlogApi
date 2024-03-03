from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, MetaData, String, ForeignKey, UUID
from sqlalchemy.orm import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'user'
    username = Column(String, nullable=False)


class Article(Base):
    __tablename__ = 'article'
    id = Column(UUID, primary_key=True, default=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    id_user = Column(UUID, ForeignKey("user.id"))


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(UUID, primary_key=True, default=True)
    author_id = Column(UUID, ForeignKey("user.id"))
    text = Column(String, nullable=False)
    post_id = Column(UUID, ForeignKey("article.id"))