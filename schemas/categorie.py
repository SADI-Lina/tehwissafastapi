from pydantic import BaseModel

class CategorieBase(BaseModel):
    designation: str

class CategorieCreate(CategorieBase):
    pass

class Categorie(CategorieBase):
    id: int

    class Config:
        orm_mode = True