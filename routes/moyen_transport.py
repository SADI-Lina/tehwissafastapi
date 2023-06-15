from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config.db import get_db
from schemas.moyen_transport import MoyenTransportCreate, MoyenTransport
from models.moyen_transport import MoyenTransport as DBMoyenTransport
from models.point_d_interet import PointDInteret as DBPointDInteret

router = APIRouter(prefix="/moyens_transport", tags=["Moyens de Transport"])


@router.post("/{id_pi}", response_model=MoyenTransport)
def create_moyen_transport(id_pi:int ,moyen_transport: MoyenTransportCreate, db: Session = Depends(get_db)):
    db_moyen_transport = DBMoyenTransport(
        id_pi=id_pi,
        designation=moyen_transport.designation
    )
    db.add(db_moyen_transport)
    db.commit()
    db.refresh(db_moyen_transport)
    return db_moyen_transport


@router.get("/{moyen_transport_id}", response_model=MoyenTransport)
def get_moyen_transport(moyen_transport_id: int, db: Session = Depends(get_db)):
    db_moyen_transport = db.query(DBMoyenTransport).get(moyen_transport_id)
    if db_moyen_transport is None:
        raise HTTPException(status_code=404, detail="Moyen de Transport not found")
    return db_moyen_transport


@router.get("/point/{point_id}", response_model=List[MoyenTransport])
def get_moyens_transport_by_point(point_id: int, db: Session = Depends(get_db)):
    db_point = db.query(DBPointDInteret).get(point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point of Interest not found")
    return db_point.moyens_transport




@router.put("/{moyen_transport_id}", response_model=MoyenTransport)
def update_moyen_transport(moyen_transport_id: int, moyen_transport: MoyenTransport, db: Session = Depends(get_db)):
    db_moyen_transport = db.query(DBMoyenTransport).get(moyen_transport_id)
    if db_moyen_transport is None:
        raise HTTPException(status_code=404, detail="Moyen de Transport not found")
    db_moyen_transport.id_pi = moyen_transport.id_pi
    db_moyen_transport.designation = moyen_transport.designation
    db.commit()
    db.refresh(db_moyen_transport)
    return db_moyen_transport


@router.delete("/{moyen_transport_id}")
def delete_moyen_transport(moyen_transport_id: int, db: Session = Depends(get_db)):
    db_moyen_transport = db.query(DBMoyenTransport).get(moyen_transport_id)
    if db_moyen_transport is None:
        raise HTTPException(status_code=404, detail="Moyen de Transport not found")
    db.delete(db_moyen_transport)
    db.commit()
    return {"message": "Moyen de Transport deleted successfully"}