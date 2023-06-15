from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import point_d_interet , adresse , commentaire , tourist_user
from config.db import engine

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the point router
app.include_router(point_d_interet.router)
app.include_router(adresse.router)
app.include_router(commentaire.router)
app.include_router(tourist_user.router)

# Create the database tables
from models.point_d_interet import Base
from models.adresse import Base
from models.commentaire import Base
from models.tourist_user import Base 

Base.metadata.create_all(bind=engine)