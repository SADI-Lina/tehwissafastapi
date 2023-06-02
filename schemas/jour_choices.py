from pydantic import BaseModel

class JourChoicesBase(BaseModel):
    id: int
    label: str

class JourChoicesCreate(JourChoicesBase):
    pass

class JourChoices(JourChoicesBase):
    class Config:
        orm_mode = True