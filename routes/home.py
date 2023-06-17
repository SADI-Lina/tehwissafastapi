from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from models.point_d_interet import PointDInteret as DBPointDInteret
from models.evenement import Evenement as DBEvenement
router = APIRouter()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from models.point_d_interet import PointDInteret as DBPointDInteret
from models.evenement import Evenement as DBEvenement
from models.adresse import Adresse as DBAdresse
from models.image_event import ImageEvent as DBImageEvent
from sqlalchemy.orm import joinedload

router = APIRouter()





from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db import get_db
from models.point_d_interet import PointDInteret as DBPointDInteret
from models.evenement import Evenement as DBEvenement
from models.image_event import ImageEvent as DBImageEvent
from models.image import Image as DBImage
from models.adresse import Adresse as DBAdresse
from sqlalchemy import desc
from typing import Dict, List, Union
from models.adresse import Adresse as DBAdresse
from sqlalchemy import desc
from typing import Dict, List, Union
from typing import Dict, List, Union

from models.image import Image as DBImage

router = APIRouter()








@router.get("/api/home", response_model=Dict[str, List[Dict[str, Union[int, str]]]])
def home(db: Session = Depends(get_db)):
    restaurants = (
        db.query(DBPointDInteret)
        .join(DBAdresse, DBPointDInteret.adresse_id == DBAdresse.id)
        .filter(DBPointDInteret.categorie_id == 5)
        .limit(6)
        .all()
    )
    hotels = (
        db.query(DBPointDInteret)
        .join(DBAdresse, DBPointDInteret.adresse_id == DBAdresse.id)
        .filter(DBPointDInteret.categorie_id == 6)
        .limit(6)
        .all()
    )
    centre_commerciales = (
        db.query(DBPointDInteret)
        .join(DBAdresse, DBPointDInteret.adresse_id == DBAdresse.id)
        .filter(DBPointDInteret.categorie_id == 7)
        .limit(6)
        .all()
    )
    events = (
        db.query(DBEvenement)
        .join(DBAdresse, DBEvenement.id_wilaya == DBAdresse.wilaya_id)
        .join(DBImageEvent, DBEvenement.id == DBImageEvent.event_id)
        .limit(6)
        .all()
    )

    restaurants_with_details = []
    for restaurant in restaurants:
        wilaya = restaurant.adresse.wilaya.designation
        first_image_path = db.query(DBImage).filter_by(point_id=restaurant.id).first().path

        restaurant_details = {
            "nom": restaurant.nom,
            "description": restaurant.description,
            "wilaya": wilaya,
            "image_path": first_image_path
        }
        restaurants_with_details.append(restaurant_details)

    hotels_with_details = []
    for hotel in hotels:
        wilaya = hotel.adresse.wilaya.designation
        first_image_path = db.query(DBImage).filter_by(point_id=hotel.id).first().path

        hotel_details = {
            "nom": hotel.nom,
            "description": hotel.description,
            "wilaya": wilaya,
            "image_path": first_image_path
        }
        hotels_with_details.append(hotel_details)

    centre_commerciales_with_details = []
    for centre_commercial in centre_commerciales:
        wilaya = centre_commercial.adresse.wilaya.designation
        first_image_path = db.query(DBImage).filter_by(point_id=centre_commercial.id).first().path

        centre_commercial_details = {
            "nom": centre_commercial.nom,
            "description": centre_commercial.description,
            "wilaya": wilaya,
            "image_path": first_image_path
        }
        centre_commerciales_with_details.append(centre_commercial_details)

    events_with_details = []
    for event in events:
        wilaya = event.adresse.wilaya.designation
        first_image_path = db.query(DBImageEvent).filter_by(point_id=event.id).first().path

        event_details = {
            "nom": event.nom,
            "description": event.description,
            "wilaya": wilaya,
            "image_path": first_image_path
        }
        events_with_details.append(event_details)

    data = {
        "restaurants": restaurants_with_details,
        "hotels": hotels_with_details,
        "centre_commerciales": centre_commerciales_with_details,
        "events": events_with_details
    }

    return data