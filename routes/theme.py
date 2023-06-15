from typing import List
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from config.db import get_db
from schemas.theme import ThemeCreate, Theme
from models.theme import Theme as DBTheme

router = APIRouter(prefix="/themes", tags=["Themes"])


@router.post("/", response_model=Theme)
def create_theme(theme: ThemeCreate, db: Session = Depends(get_db)):
    db_theme = DBTheme(designation=theme.designation)
    db.add(db_theme)
    db.commit()
    db.refresh(db_theme)
    return db_theme


@router.get("/{theme_id}", response_model=Theme)
def get_theme(theme_id: int, db: Session = Depends(get_db)):
    db_theme = db.query(DBTheme).get(theme_id)
    if db_theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    return db_theme


@router.put("/{theme_id}", response_model=Theme)
def update_theme(theme_id: int, theme: Theme, db: Session = Depends(get_db)):
    db_theme = db.query(DBTheme).get(theme_id)
    if db_theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    db_theme.designation = theme.designation
    db.commit()
    return db_theme


@router.delete("/{theme_id}")
def delete_theme(theme_id: int, db: Session = Depends(get_db)):
    db_theme = db.query(DBTheme).get(theme_id)
    if db_theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    db.delete(db_theme)
    db.commit()
    return {"message": "Theme deleted successfully"}


@router.get("/", response_model=List[Theme])
def get_all_themes(db: Session = Depends(get_db)):
    themes = db.query(DBTheme).all()
    return themes