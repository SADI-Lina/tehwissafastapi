from sqlalchemy import Column, Integer, Text
from config.db import Base

class JourChoices(Base):
    __tablename__ = "jour_choices"

    id = Column(Integer, primary_key=True)
    label = Column(Text)
