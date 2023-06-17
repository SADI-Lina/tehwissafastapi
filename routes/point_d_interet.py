from typing import List
from fastapi import APIRouter, Depends, FastAPI, HTTPException , Form
from sqlalchemy.orm import Session
from sqlalchemy import desc
from config.db import get_db
from schemas.point_d_interet import PointDInteretCreate, PointDInteret
from models.point_d_interet import PointDInteret as DBPointDInteret
from sqlalchemy import func

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)



router = APIRouter(tags=["PointDInterets"])


@router.post("/points_d_interet", response_model=PointDInteret)
def create_point_d_interet(point: PointDInteretCreate, db: Session = Depends(get_db)):
    # Check if theme_id and adresse_id are provided and assign valid values if necessary
    theme_id = point.theme_id if point.theme_id is not None else 0  # Assuming 0 as a default theme_id
    adresse_id = point.adresse_id if point.adresse_id is not None else 0  # Assuming 0 as a default adresse_id

    db_point = DBPointDInteret(
        description=point.description,
        nom=point.nom,
        Dimanche=point.Dimanche,
        Lundi=point.Lundi,
        Mardi=point.Mardi,
        Mercredi=point.Mercredi,
        Jeudi=point.Jeudi,
        Vendredi=point.Vendredi,
        Samedi=point.Samedi,
        nbr_visites=point.nbr_visites,
        adresse_id=adresse_id,
        theme_id=theme_id,
        categorie_id=point.categorie_id,
        lng=point.lng,
        lat=point.lat
    )
    db.add(db_point)
    db.commit()
    db.refresh(db_point)

    db_point.moyenne_etoiles = 0  # Set the average rating, defaulting to 0 if no ratings exist

    db.commit()
    return db_point


@router.get("/points_d_interet", response_model=List[PointDInteret])
def get_all_points_d_interet(db: Session = Depends(get_db)):
    points = db.query(DBPointDInteret).all()
    return points


@router.get("/points_d_interet/filtre_cat/{categorie_id}", response_model=List[PointDInteret])
def get_points_d_interet_by_category(categorie_id: int, db: Session = Depends(get_db)):
    points = db.query(DBPointDInteret).filter(DBPointDInteret.categorie_id == categorie_id).all()
    
    if not points:
        raise HTTPException(status_code=404, detail="No points of interest found for the specified category")
    
    return points



@router.get("/points_d_interet/filtre_them/{theme_id}", response_model=List[PointDInteret])
def get_points_d_interet_by_theme(theme_id: int, db: Session = Depends(get_db)):
    points = db.query(DBPointDInteret).filter(DBPointDInteret.theme_id == theme_id).all()
    
    if not points:
        raise HTTPException(status_code=404, detail="No points of interest found for the specified theme")
    
    return points


from sqlalchemy import or_

@router.get("/points_d_interet/recherche/{keywords}", response_model=List[PointDInteret])
def search_point_d_interet(keywords: str, db: Session = Depends(get_db)):
    search_results = db.query(DBPointDInteret).filter(
        or_(
            DBPointDInteret.description.ilike(f"%{keywords}%"),
            DBPointDInteret.nom.ilike(f"%{keywords}%")
        )
    ).all()

    return search_results


@router.get("/points_d_interet/{point_id}", response_model=PointDInteret)
def get_point_d_interet(point_id: int, db: Session = Depends(get_db)):
    db_point = db.query(DBPointDInteret).get(point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point of Interest not found")
    db_point.nbr_visites += 1  # Increment nbr_visites by 1
    db.commit()
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

@router.get("/statistics/most_visited", response_model=List[PointDInteret])
def get_most_visited_points(db: Session = Depends(get_db)):
    points = db.query(DBPointDInteret).order_by(desc(DBPointDInteret.nbr_visites)).limit(6).all()
    return points

@router.get("/statistics/recommendations", response_model=List[PointDInteret])
def get_recommendations(db: Session = Depends(get_db)):
    points = db.query(DBPointDInteret).order_by(desc(DBPointDInteret.moyenne_etoiles)).limit(6).all()

    if not points:
        raise HTTPException(status_code=404, detail="No recommended points of interest found")

    return points

@router.get("/statistics/point_d_interet_count", response_model=int)
def get_point_d_interet_count(db: Session = Depends(get_db)):
    count = db.query(func.count(DBPointDInteret.id)).scalar()
    return count

