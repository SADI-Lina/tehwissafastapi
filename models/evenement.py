from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Evenement(Base):
    __tablename__ = "evenement"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(Text)
    description = Column(Text)
    type_event_id = Column(Integer, ForeignKey("type_event.id"))
    id_wilaya = Column(Integer, ForeignKey("wilaya.code"))

    image_event = relationship("ImageEvent", back_populates="event")
    type_event = relationship("TypeEvent", backref="evenements")
    wilaya = relationship("Wilaya", backref="evenements")