from pydantic import BaseModel

class EvenementBase(BaseModel):
    nom: str
    adresse: str
    type_event: str
    id_point_in: int

class EvenementCreate(EvenementBase):
    pass

class Evenement(EvenementBase):
    id: int

    class Config:
        orm_mode = True