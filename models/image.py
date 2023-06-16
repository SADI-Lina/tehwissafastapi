from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from config.db import Base
from .point_d_interet import PointDInteret

class Image(Base):
    __tablename__ = "image"

    id = Column(Integer, primary_key=True, autoincrement=True)
    point_id = Column(Integer, ForeignKey("point_d_interet.id"))
    path = Column(Text)

    point = relationship(PointDInteret, backref="images")