from pydantic import BaseModel

class RegionalUserBase(BaseModel):
    ntelephone: int
    region_id: int
    username: str
    password: str
    nom: str
    prenom: str
    email: str

class RegionalUserCreate(RegionalUserBase):
    pass

class RegionalUser(RegionalUserBase):
    id: int

    class Config:
        orm_mode = True