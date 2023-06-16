from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.photo import PhotoCreate, Photo
from models.photo import Photo as DBPhoto
from models.point_d_interet import PointDInteret as DBPointDInteret
from PIL import Image
import os
from utils.file_utils import generate_unique_filename

router = APIRouter(prefix="/photos", tags=["Photos"])

def save_photo_file(file: UploadFile):
    # Generate a unique filename using the original filename or other criteria
    unique_filename = generate_unique_filename(file.filename)

    # Define the directory where the images will be saved
    save_directory = "photo"

    # Create the directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Construct the file path for saving the image
    save_path = os.path.join(save_directory, unique_filename)

    # Save the uploaded file to the desired location
    with open(save_path, "wb") as image_file:
        image_file.write(file.file.read())

    # Return the saved file path for further use
    return save_path

@router.post("/{point_id}", response_model=Photo)
def create_photo(point_id: int, file: UploadFile = Depends(), db: Session = Depends(get_db)):
    # Save the photo file to the "photo" directory
    save_path = save_photo_file(file)

    # Create the database record for the photo
    db_photo = DBPhoto(point_id=point_id, url=save_path)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)

    return db_photo

@router.get("/{photo_id}", response_model=Photo)
def get_photo(photo_id: int, db: Session = Depends(get_db)):
    db_photo = db.query(DBPhoto).get(photo_id)
    if db_photo is None:
        raise HTTPException(status_code=404, detail="Photo not found")

    return db_photo

@router.get("/point/{point_id}", response_model=List[Photo])
def get_photos_by_point(point_id: int, db: Session = Depends(get_db)):
    db_point = db.query(DBPointDInteret).get(point_id)
    if db_point is None:
        raise HTTPException(status_code=404, detail="Point of Interest not found")

    return db_point.photos

@router.put("/{photo_id}", response_model=Photo)
def update_photo(photo_id: int, photo: Photo, db: Session = Depends(get_db)):
    db_photo = db.query(DBPhoto).get(photo_id)
    if db_photo is None:
        raise HTTPException(status_code=404, detail="Photo not found")

    # Update the photo attributes
    db_photo.url = photo.url
    db.commit()
    db.refresh(db_photo)

    return db_photo

@router.delete("/{photo_id}")
def delete_photo(photo_id: int, db: Session = Depends(get_db)):
    db_photo = db.query(DBPhoto).get(photo_id)
    if db_photo is None:
        raise HTTPException(status_code=404, detail="Photo not found")

    db.delete(db_photo)
    db.commit()

    return {"message": "Photo deleted successfully"}
