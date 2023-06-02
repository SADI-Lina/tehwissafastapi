from pydantic import BaseModel

class WilayaBase(BaseModel):
    code: int
    designation: str

class WilayaCreate(WilayaBase):
    pass

class Wilaya(WilayaBase):
    class Config:
        orm_mode = True