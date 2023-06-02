from pydantic import BaseModel

class MoyenTransportBase(BaseModel):
    id_pi: int
    designation: str

class MoyenTransportCreate(MoyenTransportBase):
    pass

class MoyenTransport(MoyenTransportBase):
    id: int

    class Config:
        orm_mode = True