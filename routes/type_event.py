from typing import List
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from config.db import get_db
from schemas.type_event import TypeEventCreate, TypeEvent
from models.type_event import TypeEvent as DBTypeEvent

router = APIRouter(prefix="/type_events", tags=["Type Events"])


@router.post("/", response_model=TypeEvent)
def create_type_event(type_event: TypeEventCreate, db: Session = Depends(get_db)):
    db_type_event = DBTypeEvent(designation=type_event.designation)
    db.add(db_type_event)
    db.commit()
    db.refresh(db_type_event)
    return db_type_event


@router.get("/{type_event_id}", response_model=TypeEvent)
def get_type_event(type_event_id: int, db: Session = Depends(get_db)):
    db_type_event = db.query(DBTypeEvent).get(type_event_id)
    if db_type_event is None:
        raise HTTPException(status_code=404, detail="Type Event not found")
    return db_type_event


@router.put("/{type_event_id}", response_model=TypeEvent)
def update_type_event(type_event_id: int, type_event: TypeEvent, db: Session = Depends(get_db)):
    db_type_event = db.query(DBTypeEvent).get(type_event_id)
    if db_type_event is None:
        raise HTTPException(status_code=404, detail="Type Event not found")
    db_type_event.designation = type_event.designation
    db.commit()
    return db_type_event


@router.delete("/{type_event_id}")
def delete_type_event(type_event_id: int, db: Session = Depends(get_db)):
    db_type_event = db.query(DBTypeEvent).get(type_event_id)
    if db_type_event is None:
        raise HTTPException(status_code=404, detail="Type Event not found")
    db.delete(db_type_event)
    db.commit()
    return {"message": "Type Event deleted successfully"}


@router.get("/", response_model=List[TypeEvent])
def get_all_type_events(db: Session = Depends(get_db)):
    type_events = db.query(DBTypeEvent).all()
    return type_events