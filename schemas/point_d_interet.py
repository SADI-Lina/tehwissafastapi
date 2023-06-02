from pydantic import BaseModel

class PointDInteretBase(BaseModel):
    description: str
    nom: str
    nbr_visites: int
    adresse_id: int
    theme_id: int
    categorie_id: int

class PointDInteretCreate(PointDInteretBase):
    pass

class PointDInteret(PointDInteretBase):
    id: int

    class Config:
        orm_mode = True