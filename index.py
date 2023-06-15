from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import point_d_interet , adresse , theme , categorie , horaires_acces
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
app.include_router(theme.router)
app.include_router(categorie.router)
app.include_router(horaires_acces.router)

# Create the database tables
from models.point_d_interet import Base
from models.adresse import Base
from models.theme import Base
from models.categorie import Base
from models.horaires_acces import Base

Base.metadata.create_all(bind=engine)