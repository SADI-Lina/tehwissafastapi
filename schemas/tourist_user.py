from pydantic import BaseModel

class TouristUserBase(BaseModel):
    ntelephone: int
    adresse_id: int
    username: str
    password: str
    nom: str
    prenom: str
    email: str

class TouristUserCreate(TouristUserBase):
    pass

class TouristUser(TouristUserBase):
    id: int

    class Config:
        orm_mode = True  