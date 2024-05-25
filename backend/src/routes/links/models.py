from config.database import Base
from sqlalchemy import Column, String, Integer


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(String(255))
    short_link = Column(String(5), unique=True, index=True)
