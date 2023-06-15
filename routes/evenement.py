from typing import List
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from config.db import get_db
from schemas.evenement import EvenementCreate, Evenement
from models.evenement import Evenement as DBEvenement

from models.wilaya import Wilaya as DBWilaya

router = APIRouter(prefix="/evenements", tags=["Evenements"])


@router.post("/", response_model=Evenement)
def create_evenement(evenement: EvenementCreate, db: Session = Depends(get_db)):
    db_evenement = DBEvenement(
        nom=evenement.nom,
        type_event_id=evenement.type_event_id,
        id_wilaya=evenement.id_wilaya
    )
    db.add(db_evenement)
    db.commit()
    db.refresh(db_evenement)
    return db_evenement


@router.get("/{evenement_id}", response_model=Evenement)
def get_evenement(evenement_id: int, db: Session = Depends(get_db)):
    db_evenement = db.query(DBEvenement).get(evenement_id)
    if db_evenement is None:
        raise HTTPException(status_code=404, detail="Evenement not found")
    return db_evenement


@router.put("/{evenement_id}", response_model=Evenement)
def update_evenement(evenement_id: int, evenement: Evenement, db: Session = Depends(get_db)):
    db_evenement = db.query(DBEvenement).get(evenement_id)
    if db_evenement is None:
        raise HTTPException(status_code=404, detail="Evenement not found")
    db_evenement.nom = evenement.nom
    db_evenement.type_event_id = evenement.type_event_id
    db_evenement.id_wilaya = evenement.id_wilaya
    db.commit()
    return db_evenement


@router.delete("/{evenement_id}")
def delete_evenement(evenement_id: int, db: Session = Depends(get_db)):
    db_evenement = db.query(DBEvenement).get(evenement_id)
    if db_evenement is None:
        raise HTTPException(status_code=404, detail="Evenement not found")
    db.delete(db_evenement)
    db.commit()
    return {"message": "Evenement deleted successfully"}


@router.get("/", response_model=List[Evenement])
def get_all_evenements(db: Session = Depends(get_db)):
    evenements = db.query(DBEvenement).all()
    return evenements



@router.get("/by-wilaya/{wilaya_code}", response_model=List[Evenement])
def get_evenements_by_wilaya(wilaya_code: int, db: Session = Depends(get_db)):
    evenements = db.query(DBEvenement).filter(DBEvenement.id_wilaya == wilaya_code).all()
    if not evenements:
        raise HTTPException(status_code=404, detail="No evenements found for the specified wilaya")
    return evenements