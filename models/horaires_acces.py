from sqlalchemy import Column, Integer, Time, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from .jour_choices import JourChoices
class HorairesAcces(Base):
    __tablename__ = "horaires_acces"

    id = Column(Integer, primary_key=True, autoincrement=True)
    heure_debut = Column(Time, nullable=False)
    heure_fin = Column(Time, nullable=False)
    jour_id = Column(Integer, ForeignKey("jour_choices.id"), nullable=False)
    id_point_in = Column(Integer, ForeignKey("point_d_interet.id"), nullable=False)

    jour = relationship("JourChoices", backref="horaires_acces")
    point_d_interet = relationship("PointDInteret", backref="horaires_acces")