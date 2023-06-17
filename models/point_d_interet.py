from sqlalchemy import Column, Integer, Text, ForeignKey, Float
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
    moyenne_etoiles = Column(Float, default=0)
    lng = Column(Float)
    lat = Column(Float)

    adresse = relationship("Adresse", backref="points_d_interet")
    theme = relationship("Theme", backref="points_d_interet")
    categorie = relationship("Categorie", backref="points_d_interet")

    def calculate_average_rating(self):
        total_ratings = 0
        num_comments = len(self.commentaires)

        if num_comments == 0:
            return 0  # Pour éviter une division par zéro

        for commentaire in self.commentaires:
            total_ratings += commentaire.nb_etoile

        average_rating = total_ratings / num_comments
        return average_rating
