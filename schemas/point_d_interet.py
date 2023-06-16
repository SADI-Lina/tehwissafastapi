from typing import Optional
from pydantic import BaseModel

class PointDInteretBase(BaseModel):
    description: str
    nom: str
    Dimanche: str = ""
    Lundi: str = ""
    Mardi: str = ""
    Mercredi: str = ""
    Jeudi: str = ""
    Vendredi: str = ""
    Samedi: str = ""
    nbr_visites: int
    moyenne_etoiles: float
    adresse_id: int
    theme_id: int
    categorie_id: int

class PointDInteretCreate(PointDInteretBase):
    pass

class PointDInteret(PointDInteretBase):
    id: int

    class Config:
        orm_mode = True

