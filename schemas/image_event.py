from pydantic import BaseModel


class ImageEventCreate(BaseModel):
    path: str
    event_id: int