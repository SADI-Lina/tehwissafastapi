from pydantic import BaseModel

class PhotoBase(BaseModel):
    url: str

class PhotoCreate(PhotoBase):
    point_id: int

class Photo(PhotoBase):
    id: int
    point_id: int

    class Config:
        orm_mode = True