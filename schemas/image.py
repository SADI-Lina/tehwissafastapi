from pydantic import BaseModel

class ImageBase(BaseModel):
    path: str

class ImageCreate(ImageBase):
    point_id: int

class Image(ImageBase):
    id: int
    point_id: int
    path: str

    class Config:
        orm_mode = True