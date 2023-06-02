from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Region(Base):
    __tablename__ = "region"

    id = Column(Integer, primary_key=True, autoincrement=True)
    designation = Column(Text)
    adresse_id = Column(Integer, ForeignKey("adresse.id"))

    adresse = relationship("Adresse", backref="regions")