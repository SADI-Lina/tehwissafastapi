from pydantic import BaseModel
from typing import Optional
from schemas.jour_choices import JourChoices

class HorairesAccesBase(BaseModel):
    heure_debut: str
    heure_fin: str
    jour_id: int

class HorairesAccesCreate(HorairesAccesBase):
    pass

class HorairesAcces(HorairesAccesBase):
    id: int
    jour: JourChoices

    class Config:
        orm_mode = True