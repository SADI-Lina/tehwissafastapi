from sqlalchemy import Column, Integer, Text
from config.db import Base

class Categorie(Base):
    __tablename__ = "categorie"

    id = Column(Integer, primary_key=True, autoincrement=True)
    designation = Column(Text)