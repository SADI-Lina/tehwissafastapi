from pydantic import BaseModel

class AdresseBase(BaseModel):
    wilaya_id: int
    info_supp: str


class AdresseCreate(AdresseBase):
    pass

class Adresse(AdresseBase):
    id: int

    class Config:
        orm_mode = True   

