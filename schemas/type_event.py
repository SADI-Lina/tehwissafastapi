from pydantic import BaseModel

class TypeEventBase(BaseModel):
    designation: str

class TypeEventCreate(TypeEventBase):
    pass

class TypeEvent(TypeEventBase):
    id: int

    class Config:
        orm_mode = True