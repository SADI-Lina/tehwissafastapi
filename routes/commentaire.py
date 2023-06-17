from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

from config.db import get_db
from schemas.commentaire import CommentaireCreate, Commentaire
from models.commentaire import Commentaire as DBCommentaire
from models.point_d_interet import PointDInteret
from models.point_d_interet import PointDInteret as DBPointDInteret
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
router = APIRouter(tags=["Commentaire"])

@router.post("/commentaire", response_model=Commentaire)
def create_commentaire(commentaire: CommentaireCreate, db: Session = Depends(get_db)):

    db_commentaire = DBCommentaire(
        id_touriste=commentaire.id_touriste,
        contenu=commentaire.contenu,
        nb_etoile=commentaire.nb_etoile,
        id_point_in=commentaire.id_point_in
    )
    db.add(db_commentaire)
    db.commit()
    db.refresh(db_commentaire)

    # Mettre à jour la moyenne des nombres d'étoiles du lieu touristique
    point_d_interet = db_commentaire.point_d_interet
    average_rating = point_d_interet.calculate_average_rating()
    point_d_interet.moyenne_etoiles = average_rating
    db.commit()

    return db_commentaire

def get_comments_by_point_id(db: Session, point_id: int) -> List[DBCommentaire]:
    comments = db.query(DBCommentaire).filter(DBCommentaire.id_point_in == point_id).all()
    return comments

@router.get("/commentaire/{point_id}", response_model=List[Commentaire])
def get_commentaires_by_point_id(point_id: int, db: Session = Depends(get_db)):
    comments = get_comments_by_point_id(db, point_id)
    if not comments:
        raise HTTPException(status_code=404, detail="No comments found for the specified point of interest")
    return comments

@router.get("/statistics/commentaires_count", response_model=int)
def count_commentaires(db: Session = Depends(get_db)):
    count = db.query(func.count(DBCommentaire.id)).scalar()
    return count