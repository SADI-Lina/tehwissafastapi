from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import get_db
from schemas.commentaire import CommentaireCreate, Commentaire
from models.commentaire import Commentaire as DBCommentaire

router = APIRouter()

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
    return db_commentaire