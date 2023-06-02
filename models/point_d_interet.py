from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class PointDInteret(Base):
    __tablename__ = "point_d_interet"

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text)
    nom = Column(Text)
    nbr_visites = Column(Integer, default=0)
    adresse_id = Column(Integer, ForeignKey("adresse.id"))
    theme_id = Column(Integer, ForeignKey("theme.id"))
    categorie_id = Column(Integer, ForeignKey("categorie.id"))

    adresse = relationship("Adresse", backref="points_d_interet")
    theme = relationship("Theme", backref="points_d_interet")
    categorie = relationship("Categorie", backref="points_d_interet")
