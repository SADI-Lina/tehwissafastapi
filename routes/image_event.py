from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import get_db
from models.image_event import ImageEvent
from schemas.image_event import ImageEventCreate

router = APIRouter()


@router.post("/api/image_event", status_code=201)
def create_image_event(image_event: ImageEventCreate, db: Session = Depends(get_db)):
    new_image_event = ImageEvent(**image_event.dict())
    db.add(new_image_event)
    db.commit()
    db.refresh(new_image_event)
    return new_image_event
