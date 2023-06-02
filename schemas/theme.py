from pydantic import BaseModel

class ThemeBase(BaseModel):
    designation: str

class ThemeCreate(ThemeBase):
    pass

class Theme(ThemeBase):
    id: int

    class Config:
        orm_mode = True