from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base
from .adresse import Adresse
from .theme import Theme
from .categorie import Categorie
class PointDInteret(Base):
    __tablename__ = "point_d_interet"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text)
    nom = Column(Text)
    nbr_visites = Column(Integer, default=0)
    Dimanche = Column(Text, nullable=True)
    Lundi = Column(Text, nullable=True)
    Mardi = Column(Text, nullable=True)
    Mercredi = Column(Text, nullable=True)
    Jeudi = Column(Text, nullable=True)
    Vendredi = Column(Text, nullable=True)
    Samedi = Column(Text, nullable=True)
    adresse_id = Column(Integer, ForeignKey("adresse.id"))
    theme_id = Column(Integer, ForeignKey("theme.id"))
    categorie_id = Column(Integer, ForeignKey("categorie.id"))

    adresse = relationship("Adresse", backref="points_d_interet")
    theme = relationship("Theme", backref="points_d_interet")
    categorie = relationship("Categorie", backref="points_d_interet")
