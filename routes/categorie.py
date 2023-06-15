from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import get_db
from schemas.categorie import CategorieCreate, Categorie
from models.categorie import Categorie as DBCategorie

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/", response_model=Categorie)
def create_categorie(categorie: CategorieCreate, db: Session = Depends(get_db)):
    db_categorie = DBCategorie(designation=categorie.designation)
    db.add(db_categorie)
    db.commit()
    db.refresh(db_categorie)
    return db_categorie


@router.get("/{categorie_id}", response_model=Categorie)
def get_categorie(categorie_id: int, db: Session = Depends(get_db)):
    db_categorie = db.query(DBCategorie).get(categorie_id)
    if db_categorie is None:
        raise HTTPException(status_code=404, detail="Categorie not found")
    return db_categorie


@router.put("/{categorie_id}", response_model=Categorie)
def update_categorie(categorie_id: int, categorie: Categorie, db: Session = Depends(get_db)):
    db_categorie = db.query(DBCategorie).get(categorie_id)
    if db_categorie is None:
        raise HTTPException(status_code=404, detail="Categorie not found")
    db_categorie.designation = categorie.designation
    db.commit()
    return db_categorie


@router.delete("/{categorie_id}")
def delete_categorie(categorie_id: int, db: Session = Depends(get_db)):
    db_categorie = db.query(DBCategorie).get(categorie_id)
    if db_categorie is None:
        raise HTTPException(status_code=404, detail="Categorie not found")
    db.delete(db_categorie)
    db.commit()
    return {"message": "Categorie deleted successfully"}


@router.get("/", response_model=List[Categorie])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(DBCategorie).all()
    return categories