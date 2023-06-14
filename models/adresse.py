from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from .wilaya import Wilaya

class Adresse(Base):
    __tablename__ = "adresse"

    id = Column(Integer, primary_key=True, autoincrement=True)
    wilaya_id = Column(Integer, ForeignKey("wilaya.code"))
    info_supp = Column(Text)

    wilaya = relationship("Wilaya", backref="adresses")