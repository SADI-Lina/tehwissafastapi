from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

from .region import Region

class RegionalUser(Base):
    __tablename__ = "regional_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ntelephone = Column(Integer)
    region_id = Column(Integer, ForeignKey("region.id"))
    username = Column(Text)
    password = Column(Text)
    nom = Column(Text)
    prenom = Column(Text)
    email = Column(Text)

    region = relationship("Region", backref="regional_users")