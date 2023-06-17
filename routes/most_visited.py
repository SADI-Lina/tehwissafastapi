from sqlalchemy import func
from sqlalchemy.orm import joinedload
from fastapi.responses import JSONResponse
from fastapi import Depends
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.point_d_interet import PointDInteretCreate, PointDInteret
from models.point_d_interet import PointDInteret as DBPointDInteret
from models.adresse import Adresse
from models.image import Image
from fastapi import APIRouter
from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc
from sqlalchemy.orm import joinedload
from fastapi.responses import JSONResponse
from typing import Dict, List, Union
from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi import APIRouter, Depends, HTTPException

from config.db import get_db
from models.point_d_interet import PointDInteret as DBPointDInteret
from models.adresse import Adresse as DBAdresse
from models.image import Image as DBImage


router = APIRouter()


@router.get("/api/statistics/most_visited", response_model=List[Dict[str, Union[str, str, str]]])
def get_most_visited_points_with_details(db: Session = Depends(get_db)):
    points = db.query(DBPointDInteret).order_by(desc(DBPointDInteret.nbr_visites)).limit(6).all()

    points_with_details = []
    for point in points:
        wilaya = db.query(DBAdresse).get(point.adresse_id).wilaya.designation
        first_image_path = db.query(DBImage).filter_by(point_id=point.id).first().path

        point_details = {
            "point_name": point.nom,
            "wilaya": wilaya,
            "image_path": first_image_path
        }
        points_with_details.append(point_details)

    return points_with_details