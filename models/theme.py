from sqlalchemy import Column, Integer, Text
from config.db import Base

class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True, autoincrement=True)
    designation = Column(Text)
