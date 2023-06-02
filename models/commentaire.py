from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class Commentaire(Base):
    __tablename__ = "commentaire"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_touriste = Column(Integer, ForeignKey("tourist_user.id"))
    contenu = Column(Text)
    nb_etoile = Column(Integer)
    id_point_in = Column(Integer, ForeignKey("point_d_interet.id"))

    tourist_user = relationship("TouristUser", backref="commentaires")
    point_d_interet = relationship("PointDInteret", backref="commentaires")