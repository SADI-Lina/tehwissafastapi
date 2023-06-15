from sqlalchemy import Column, Integer, Text
from config.db import Base

class TypeEvent(Base):
    __tablename__ = "type_event"

    id = Column(Integer, primary_key=True, autoincrement=True)
    designation = Column(Text)