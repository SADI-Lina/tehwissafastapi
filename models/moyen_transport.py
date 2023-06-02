from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class MoyenTransport(Base):
    __tablename__ = "moyen_transport"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_pi = Column(Integer, ForeignKey("point_d_interet.id"))
    designation = Column(Text)

    point_d_interet = relationship("PointDInteret", backref="moyens_transport")

