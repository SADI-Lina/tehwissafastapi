from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import get_db
from schemas.horaires_acces import HorairesAccesCreate,  HorairesAcces
from models.horaires_acces import HorairesAcces as DBHorairesAcces

router = APIRouter(prefix="/horaires_acces", tags=["HorairesAcces"])


@router.post("/{id_point_in}", response_model=HorairesAcces)
def create_horaire_acces(id_point_in: int,horaire_acces: HorairesAccesCreate, db: Session = Depends(get_db)):
    db_horaire_acces = DBHorairesAcces(
        heure_debut=horaire_acces.heure_debut,
        heure_fin=horaire_acces.heure_fin,
        jour_id=horaire_acces.jour_id,
        id_point_in= id_point_in
    )
    db.add(db_horaire_acces)
    db.commit()
    db.refresh(db_horaire_acces)
    return db_horaire_acces


@router.get("/{horaire_acces_id}", response_model=HorairesAcces)
def get_horaire_acces(horaire_acces_id: int, db: Session = Depends(get_db)):
    db_horaire_acces = db.query(DBHorairesAcces).get(horaire_acces_id)
    if db_horaire_acces is None:
        raise HTTPException(status_code=404, detail="HorairesAcces not found")
    return db_horaire_acces


@router.put("/{horaire_acces_id}", response_model=HorairesAcces)
def update_horaire_acces(horaire_acces_id: int, horaire_acces: HorairesAcces, db: Session = Depends(get_db)):
    db_horaire_acces = db.query(DBHorairesAcces).get(horaire_acces_id)
    if db_horaire_acces is None:
        raise HTTPException(status_code=404, detail="HorairesAcces not found")
    for field, value in horaire_acces.dict(exclude_unset=True).items():
        setattr(db_horaire_acces, field, value)
    db.commit()
    return db_horaire_acces


@router.delete("/{horaire_acces_id}")
def delete_horaire_acces(horaire_acces_id: int, db: Session = Depends(get_db)):
    db_horaire_acces = db.query(DBHorairesAcces).get(horaire_acces_id)
    if db_horaire_acces is None:
        raise HTTPException(status_code=404, detail="HorairesAcces not found")
    db.delete(db_horaire_acces)
    db.commit()
    return {"message": "HorairesAcces deleted successfully"}


@router.get("/", response_model=List[HorairesAcces])
def get_all_horaires_acces(db: Session = Depends(get_db)):
    horaires_acces = db.query(DBHorairesAcces).all()
    return horaires_acces