from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Evenement(Base):
    __tablename__ = "evenement"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(Text)
    adresse = Column(Text)
    type_event = Column(Text)
    id_point_in = Column(Integer, ForeignKey("point_d_interet.id"))

    point_d_interet = relationship("PointDInteret", backref="evenements")