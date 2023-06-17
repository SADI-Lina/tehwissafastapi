from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.db import Base


class ImageEvent(Base):
    __tablename__ = "image_event"

    id = Column(Integer, primary_key=True, index=True)
    path = Column(String(255))
    event_id = Column(Integer, ForeignKey("evenement.id"))

    event = relationship("Evenement", back_populates="image_event")
