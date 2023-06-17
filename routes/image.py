from typing import List
from fastapi import APIRouter, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.image import ImageCreate, Image , ImageBase
from models.image import Image as DBImage
from models.point_d_interet import PointDInteret as DBPointDInteret
from config.db import get_db
import os

router = APIRouter(prefix="/images", tags=["Images"])

@router.post("/{point_id}", response_model=Image)
def create_Image(point_id:int ,image: ImageBase, db: Session = Depends(get_db)):
    db_image = DBImage(
        path=image.path,
        point_id=point_id
    )
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

@router.get("/{image_id}", response_model=Image)
def get_image(image_id: int, db: Session = Depends(get_db)):
    db_image = db.query(DBImage).get(image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    return db_image


@router.get("/point/{point_id}", response_model=List[Image])
def get_images_by_point(point_id: int, db: Session = Depends(get_db)):
    db_point = db.query(DBPointDInteret).get(point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point of Interest not found")

    return db_point.images


@router.put("/{image_id}", response_model=Image)
def update_image(image_id: int, image: ImageCreate, db: Session = Depends(get_db)):
    db_image = db.query(DBImage).get(image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    # Update the image attributes
    db_image.path = image.path
    db.commit()
    db.refresh(db_image)

    return db_image


@router.delete("/{image_id}")
def delete_image(image_id: int, db: Session = Depends(get_db)):
    db_image = db.query(DBImage).get(image_id)
    if db_image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    db.delete(db_image)
    db.commit()

    return {"message": "Image deleted successfully"}

@router.get("/point/{point_id}/first_image_path", response_model=str)
def get_first_image_path(point_id: int, db: Session = Depends(get_db)):
    db_point = db.query(DBPointDInteret).get(point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point of Interest not found")

    if not db_point.images:
        raise HTTPException(status_code=404, detail="No images found for the Point of Interest")

    return db_point.images[0].path
