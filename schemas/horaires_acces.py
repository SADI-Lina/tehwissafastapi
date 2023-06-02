from pydantic import BaseModel

class HorairesAccesBase(BaseModel):
    heure_debut: str
    heure_fin: str
    jour_id: int
    id_point_in: int

class HorairesAccesCreate(HorairesAccesBase):
    pass

class HorairesAcces(HorairesAccesBase):
    id: int

    class Config:
        orm_mode = True