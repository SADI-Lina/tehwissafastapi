from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class TouristUser(Base):
    __tablename__ = "tourist_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ntelephone = Column(Integer)
    adresse_id = Column(Integer, ForeignKey("adresse.id"))
    username = Column(Text)
    password = Column(Text)
    nom = Column(Text)
    prenom = Column(Text)
    email = Column(Text)

    adresse = relationship("Adresse", backref="tourist_users")