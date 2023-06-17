from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from config.db import get_db
from schemas.adresse import AdresseCreate, Adresse
from models.adresse import Adresse as DBAdresse

router = APIRouter( tags=["Adresses"])




@router.get("/adresse", response_model=List[Adresse])
def get_all_adresse(db: Session = Depends(get_db)):
    points = db.query(DBAdresse).all()
    return points


@router.post("/adresse", response_model=Adresse)
def create_Adresset(adresse: AdresseCreate, db: Session = Depends(get_db)):
    db_adresse = DBAdresse(
        wilaya_id=adresse.wilaya_id,
        info_supp=adresse.info_supp
    )
    db.add(db_adresse)
    db.commit()
    db.refresh(db_adresse)
    return db_adresse

@router.get("/adresse/{adresse_id}", response_model=Adresse)
def get_adresse(adresse_id: int, db: Session = Depends(get_db)):
    db_adresse = db.query(DBAdresse).get(adresse_id)
    if db_adresse is None:
        raise HTTPException(status_code=404, detail="Adresse not found")
    return db_adresse

@router.put("/adresse/{adresse_id}", response_model=Adresse)
def update_adresse(adresse_id: int, adresse: Adresse, db: Session = Depends(get_db)):
    db_adresse = db.query(DBAdresse).get(adresse_id)
    if db_adresse is None:
        raise HTTPException(status_code=404, detail="Adresse not found")
    for field, value in adresse.dict(exclude_unset=True).items():
        setattr(db_adresse, field, value)
    db.commit()
    return db_adresse

@router.delete("/adresse/{adresse_id}")
def delete_adresse(adresse_id: int, db: Session = Depends(get_db)):
    db_adresse = db.query(DBAdresse).get(adresse_id)
    if db_adresse is None:
        raise HTTPException(status_code=404, detail="Adresse not found")
    db.delete(db_adresse)
    db.commit()
    return {"message": "Adresse deleted successfully"}




from typing import List

def get_adresses(db: Session) -> List[Adresse]:
    return db.query(Adresse).all()

@router.get("/adresse/{adresse_id}/wilaya", response_model=str)
def get_wilaya_of_point(adresse_id: int, db: Session = Depends(get_db)):
    db_adresse = db.query(DBAdresse).get(adresse_id)
    if db_adresse is None:
        raise HTTPException(status_code=404, detail="Adresse not found")

    wilaya = db_adresse.wilaya
    if wilaya is None:
        raise HTTPException(status_code=404, detail="Wilaya not found")

    return wilaya.designation