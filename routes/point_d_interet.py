from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import get_db
from schemas.point_d_interet import PointDInteretCreate, PointDInteret
from models.point_d_interet import PointDInteret as DBPointDInteret

router = APIRouter()

@router.post("/points_d_interet", response_model=PointDInteret)
def create_point_d_interet(point: PointDInteretCreate, db: Session = Depends(get_db)):
    db_point = DBPointDInteret(
        description=point.description,
        nom=point.nom,
        nbr_visites=point.nbr_visites,
        adresse_id=point.adresse_id,
        theme_id=point.theme_id,
        categorie_id=point.categorie_id
    )
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point

@router.get("/points_d_interet/{point_id}", response_model=PointDInteret)
def get_point_d_interet(point_id: int, db: Session = Depends(get_db)):
    db_point = db.query(DBPointDInteret).get(point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point of Interest not found")
    return db_point

@router.put("/points_d_interet/{point_id}", response_model=PointDInteret)
def update_point_d_interet(point_id: int, point: PointDInteret, db: Session = Depends(get_db)):
    db_point = db.query(DBPointDInteret).get(point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point of Interest not found")
    for field, value in point.dict(exclude_unset=True).items():
        setattr(db_point, field, value)
    db.commit()
    return db_point

@router.delete("/points_d_interet/{point_id}")
def delete_point_d_interet(point_id: int, db: Session = Depends(get_db)):
    db_point = db.query(DBPointDInteret).get(point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point of Interest not found")
    db.delete(db_point)
    db.commit()
    return {"message": "Point of Interest deleted successfully"}