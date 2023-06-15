from pydantic import BaseModel

class RegionBase(BaseModel):
    designation: str
    "adresse_id: int"


class RegionCreate(RegionBase):
    pass

class Region(RegionBase):
    id: int

    class Config:
        orm_mode = True