from sqlalchemy import func
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import get_db
from schemas.tourist_user import TouristUserCreate, TouristUser
from models.tourist_user import TouristUser as DBTouristUser

router = APIRouter()

 
@router.post("/register" , response_model= TouristUser)
def create_tourist_user(touriste: TouristUserCreate, db: Session = Depends(get_db)):

    # db_touriste = TouristUser(**touriste.dict())
 
    db_touriste = DBTouristUser(
        ntelephone = touriste.ntelephone,
        adresse_id = touriste.adresse_id, 
        username = touriste.username,
        password = touriste.password,
        nom = touriste.nom,
        prenom = touriste.prenom,
        email = touriste.email    
        )
    db.add(db_touriste)
    db.commit()
    db.refresh(db_touriste)
    return  db_touriste


@router.post("/login",response_model= TouristUser)
def tourist_user_login(touriste: TouristUserCreate, db: Session = Depends(get_db)):
    user = db.query(DBTouristUser).filter(DBTouristUser.username == touriste.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.check_password(touriste.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    return user



@router.post("/register", response_model=TouristUser)
def create_tourist_user(touriste: TouristUserCreate, db: Session = Depends(get_db)):
    # db_touriste = TouristUser(**touriste.dict())

    db_touriste = DBTouristUser(
        ntelephone=touriste.ntelephone,
        adresse_id=touriste.adresse_id,
        username=touriste.username,
        password=touriste.password,
        nom=touriste.nom,
        prenom=touriste.prenom,
        email=touriste.email
    )
    db.add(db_touriste)
    db.commit()
    db.refresh(db_touriste)
    return db_touriste


@router.post("/login")
def tourist_user_login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(DBTouristUser).filter(DBTouristUser.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not user.check_password(password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {"user": user}

@router.get("/statistics/users_count", response_model=int)
def count_users(db: Session = Depends(get_db)):
    count = db.query(func.count(DBTouristUser.id)).scalar()
    return count
