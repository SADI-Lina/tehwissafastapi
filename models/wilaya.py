from sqlalchemy import Column, Integer, Text
from config.db import Base

class Wilaya(Base):
    __tablename__ = "wilaya"

    code = Column(Integer, primary_key=True)
    designation = Column(Text)