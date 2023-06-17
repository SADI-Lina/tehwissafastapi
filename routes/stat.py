from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from config.db import get_db
from routes.commentaire import count_commentaires
from routes.tourist_user import count_users
from routes.point_d_interet import get_point_d_interet_count
from fastapi import APIRouter



router = APIRouter()


@router.get("/api/statistiques", response_class=JSONResponse)
def get_statistics(db: Session = Depends(get_db)):
    feedback = count_commentaires(db)
    utilisateurs = count_users(db)
    lieux = get_point_d_interet_count(db)

    return JSONResponse({'feedback': feedback, 'utilisateurs': utilisateurs, 'lieux': lieux})