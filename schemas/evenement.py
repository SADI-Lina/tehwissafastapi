from pydantic import BaseModel

class EvenementBase(BaseModel):
    nom: str
    description : str
    type_event_id: int
    id_wilaya: int

class EvenementCreate(EvenementBase):
    pass

class Evenement(EvenementBase):
    id: int

    class Config:
        orm_mode = True