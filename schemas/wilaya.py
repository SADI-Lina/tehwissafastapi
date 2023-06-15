from pydantic import BaseModel

class WilayaBase(BaseModel):
    code: int
    designation: str
    region_id: int

class WilayaCreate(WilayaBase):
    pass

class Wilaya(WilayaBase):
    class Config:
        orm_mode = True