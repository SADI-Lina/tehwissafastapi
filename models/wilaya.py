from sqlalchemy import Column, ForeignKey, Integer, Text
from config.db import Base
from sqlalchemy.orm import relationship
from .region import Region
"""class Wilaya(Base):
    __tablename__ = "wilaya"

    code = Column(Integer, primary_key=True)
    designation = Column(Text)"""



class Wilaya(Base):
    __tablename__ = "wilaya"

    code = Column(Integer, primary_key=True)
    designation = Column(Text)
    region_id = Column(Integer, ForeignKey("region.id"))
    region = relationship("Region", backref="wilayas")    